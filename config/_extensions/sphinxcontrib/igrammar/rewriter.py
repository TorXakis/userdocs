import sys

import docutils.nodes
from antlr4 import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from antlr4.tree.Tree import TerminalNodeImpl

#from sphinxcontrib.igrammar import rule_def_node
import sphinxcontrib.igrammar
from sphinxcontrib.igrammar.ANTLRv4Lexer import ANTLRv4Lexer
from sphinxcontrib.igrammar.ANTLRv4Parser import ANTLRv4Parser
from sphinxcontrib.igrammar.ANTLRv4ParserListener import ANTLRv4ParserListener


# class MyListener(ANTLRv4ParserListener):
# 
#     def __init__(self, rewriter:TokenStreamRewriter):
#         self.rewriter = rewriter
# 
#     # Exit a parse tree produced by ANTLRv4Parser#parserRuleSpec.
#     def exitParserRuleSpec(self, ctx:ANTLRv4Parser.ParserRuleSpecContext):
#         self.rewriter.insertBeforeToken(ctx.RULE_REF().symbol , ":red:`")
#         self.rewriter.insertAfterToken(ctx.RULE_REF().symbol,  '`')
# 
#     # Exit a parse tree produced by ANTLRv4Parser#terminal.
#     def exitTerminal(self, ctx:ANTLRv4Parser.TerminalContext):
#         if ctx.STRING_LITERAL():
#             self.rewriter.insertBeforeToken(ctx.STRING_LITERAL().symbol , ":blue:`")
#             self.rewriter.insertAfterToken(ctx.STRING_LITERAL().symbol,  '`')
#         if ctx.TOKEN_REF():
#             self.rewriter.insertBeforeToken(ctx.TOKEN_REF().symbol , ":blue:`")
#             self.rewriter.insertAfterToken(ctx.TOKEN_REF().symbol,  '`')
# 
#     # Exit a parse tree produced by ANTLRv4Parser#ruleref.
#     def exitRuleref(self, ctx:ANTLRv4Parser.RulerefContext):
#         self.rewriter.insertBeforeToken(ctx.RULE_REF().symbol, ":green:`")
#         self.rewriter.insertAfterToken(ctx.RULE_REF().symbol, '`')
# 

class ListenerGetRules(ANTLRv4ParserListener):

    def __init__(self, rulesDefined):
        self.rulesDefined = rulesDefined


    # parserRuleSpec
    #    : ruleModifiers? RULE_REF argActionBlock? ruleReturns? throwsSpec? localsSpec? rulePrequel* COLON ruleBlock SEMI exceptionGroup
    #    ;
    # Enter a parse tree produced by ANTLRv4Parser#parserRuleSpec.
    def enterParserRuleSpec(self, ctx:ANTLRv4Parser.ParserRuleSpecContext):
        rule=ctx.RULE_REF().getSymbol().text
        self.rulesDefined.append(rule)


    # lexerRuleSpec
    #    : FRAGMENT? TOKEN_REF COLON lexerRuleBlock SEMI
    #    ;
    # Enter a parse tree produced by ANTLRv4Parser#lexerRuleSpec.
    def enterLexerRuleSpec(self, ctx:ANTLRv4Parser.LexerRuleSpecContext):
        rule=ctx.TOKEN_REF().getSymbol().text
        self.rulesDefined.append(rule)


class ListenerGetNodes(ANTLRv4ParserListener):

    def __init__(self, tokenIndex2nodes, namespace, in_full_grammar, rulesDefined, docname):
        self.tokenIndex2nodes = tokenIndex2nodes
        self.namespace=namespace
        self.in_full_grammar = in_full_grammar
        self.rulesDefined = rulesDefined
        self.docname = docname


    # grammarDecl
    #   : grammarType identifier SEMI
    # ;
    # grammarType
    #   : (LEXER GRAMMAR | PARSER GRAMMAR | GRAMMAR)
    # ;
    # Enter a parse tree produced by ANTLRv4Parser#grammarDecl.
    def enterGrammarDecl(self, ctx:ANTLRv4Parser.GrammarDeclContext):
        # type of Grammar (grammarType) 
        grammarType=ctx.grammarType()
        grammarType_tokens=[ child.symbol for child in grammarType.children ]
        for token in grammarType_tokens:
            node = sphinxcontrib.igrammar.grammarType_node(token.text)
            self.tokenIndex2nodes[token.tokenIndex] = [node]

        # name of grammar (identifier)
        token=ctx.identifier().start
        node = sphinxcontrib.igrammar.grammarName_node(token.text)
        self.tokenIndex2nodes[token.tokenIndex] = [node]


    def create_new_node(self,node_class,text):
        new_node = node_class(text)
        new_node['namespace'] = self.namespace
        new_node['in_full_grammar'] = self.in_full_grammar
        new_node['docname']=self.docname
        new_node['rulename']=text
        new_node['rule_defined_local'] = text in self.rulesDefined   # only used by rule and contex references      
        return new_node

    # parserRuleSpec
    #    : ruleModifiers? RULE_REF argActionBlock? ruleReturns? throwsSpec? localsSpec? rulePrequel* COLON ruleBlock SEMI exceptionGroup
    #    ;
    # Enter a parse tree produced by ANTLRv4Parser#parserRuleSpec.
    def enterParserRuleSpec(self, ctx:ANTLRv4Parser.ParserRuleSpecContext):
        symbol_text=ctx.RULE_REF().getSymbol().text
        tokenIndex = ctx.RULE_REF().getSymbol().tokenIndex

        # create new node
        new_node = self.create_new_node(sphinxcontrib.igrammar.rule_def_node,symbol_text)
        self.tokenIndex2nodes[tokenIndex] = [new_node]


    # lexerRuleSpec
    #    : FRAGMENT? TOKEN_REF COLON lexerRuleBlock SEMI
    #    ;
    # Enter a parse tree produced by ANTLRv4Parser#lexerRuleSpec.
    def enterLexerRuleSpec(self, ctx:ANTLRv4Parser.LexerRuleSpecContext):
        symbol_text=ctx.TOKEN_REF().getSymbol().text
        tokenIndex = ctx.TOKEN_REF().getSymbol().tokenIndex

        # create new node
        new_node = self.create_new_node(sphinxcontrib.igrammar.token_def_node,symbol_text)
        self.tokenIndex2nodes[tokenIndex] = [new_node]


    # terminal
    #    : TOKEN_REF elementOptions?
    #    | STRING_LITERAL elementOptions?
    #    ;
    # Enter a parse tree produced by ANTLRv4Parser#terminal.
    def enterTerminal(self, ctx:ANTLRv4Parser.TerminalContext):
        if ctx.STRING_LITERAL():
            tokenIndex = ctx.STRING_LITERAL().getSymbol().tokenIndex
            tokenText = ctx.STRING_LITERAL().getText()

            # create new node
            new_node = sphinxcontrib.igrammar.terminal_node(tokenText)
            self.tokenIndex2nodes[tokenIndex] = [new_node]

        if ctx.TOKEN_REF():
            token_ref: TerminalNodeImpl = ctx.TOKEN_REF()
            tokenText = token_ref.getText()
            tokenIndex = token_ref.getSymbol().tokenIndex

            # create new node
            new_node = self.create_new_node(sphinxcontrib.igrammar.token_ref_node, tokenText)
            self.tokenIndex2nodes[tokenIndex] = [new_node]


    # ruleref
    #    : RULE_REF argActionBlock? elementOptions?
    #    ;
    # Enter a parse tree produced by ANTLRv4Parser#ruleref.
    def enterRuleref(self, ctx:ANTLRv4Parser.RulerefContext):
        rule_ref:TerminalNodeImpl = ctx.RULE_REF()
        rule_label = rule_ref.getText()
        tokenIndex=rule_ref.getSymbol().tokenIndex

        # create new node
        new_node = self.create_new_node(sphinxcontrib.igrammar.rule_ref_node,rule_label)
        self.tokenIndex2nodes[tokenIndex] = [new_node]


def add_nodes(nodes, nodecls, text, with_counter, counter, line_node,hl_lines,linenostart):
    # if not with_counter:
    #     nodes.append(nodecls(text))
    #     return counter # not used!
    # else: 
    # on each newline store a counter_node with an increased counter
    # and split node with text over multiple lines into multiple nodes!
    # note: only text and comments outside the special nodes are split
    #       we assume the special nodes only are on a single line!
    
    lst = text.split("\n")
    if len(lst) == 1:
        line_node.append(nodecls(lst[0]))
        return counter, line_node
    
    #else : 
    newline=docutils.nodes.Text("\n")
    # finish current line(_node), 
    #line_node.append(nodecls(lst[0] + "\n"))
    line_node.append(nodecls(lst[0]))
    #  add it to nodes,
    nodes.append(line_node)
    nodes.append(newline)
    

    for item in lst[1:-1]:
        # create new line(_node) with 1 higher line number
        counter = counter + 1
        line_node = sphinxcontrib.igrammar.line_node()       
        if counter in hl_lines:
            line_node["highlight"] = True
        else:
            line_node["highlight"] = False
        # add line counter in the line contents    
        if with_counter:
            line_node.append(sphinxcontrib.igrammar.counter_node(counter+linenostart-1))
        # add line content    
        #line_node.append(nodecls(item + "\n"))
        line_node.append(nodecls(item))
        # store line in nodes
        nodes.append(line_node)
        nodes.append(newline)
        
        # # create new line_node
        # line_node = sphinxcontrib.igrammar.line_node()
        # counter = counter + 1
        # if counter in hl_lines:
        #     line_node["highlight"] = True
        # else:
        #     line_node["highlight"] = False
        
    # add remain piece of content
    # create new line(_node) with 1 higher line number
    counter = counter + 1
    line_node = sphinxcontrib.igrammar.line_node()
    if counter in hl_lines:
        line_node["highlight"] = True
    else:
        line_node["highlight"] = False
    # add line counter in the line contents    
    if with_counter:
        line_node.append(sphinxcontrib.igrammar.counter_node(counter+linenostart-1))
    # add line content    
    line_node.append(nodecls(lst[-1])) # note: no newline!!

    # if with_counter:
    #     line_node.append(sphinxcontrib.igrammar.counter_node(counter+linenostart-1))
    # line_node.append(nodecls(lst[-1]))
    #counter = counter + 1
    return counter, line_node


def first_parse(walker,tree,env,namespace,in_full_grammar,docname):
    # in first parse get rules in rulesDefined, so we can refer to them in second pass!
    rulesDefined = []
    listener_rules = ListenerGetRules(rulesDefined)
    walker.walk(listener_rules, tree)
    if not hasattr(env, 'ruledefs'):
        env.ruledefs = []  # list of all  ruledef anonymous objects

    for rulename in rulesDefined:
        ruledef = {
            'namespace': namespace,
            'in_full_grammar': in_full_grammar,
            'docname': docname,
            'rulename': rulename
        }
        env.ruledefs.append(ruledef)
    return rulesDefined




def second_parse(walker,tree,namespace, in_full_grammar, rulesDefined,  docname):
    tokenIndex2nodes = {}
    listener_nodes = ListenerGetNodes(tokenIndex2nodes, namespace, in_full_grammar, rulesDefined,  docname)
    walker.walk(listener_nodes, tree)
    return tokenIndex2nodes

def addTextNodes(nodes,text_pieces, with_counter, counter,line_node,hl_lines,linenostart):
    if text_pieces:
        text = "".join(text_pieces)
        text_pieces.clear()
        counter, line_node = add_nodes(nodes, docutils.nodes.Text, text, with_counter, counter,line_node,hl_lines,linenostart)
    return counter, line_node

def tokens2nodes(tokens,tokenIndex2nodes,eofToken,commentChannel,with_counter,hl_lines,linenostart):
    # translate tokens into nodes
    #    - store tokens linked to a special node as that special node
    #    - store the text of the tokens between our special/comment nodes as a text node
    #    - store text on the special comment channel as a comment_node
    nodes = []
    text_pieces = []
    
    counter = 1
    line_node = sphinxcontrib.igrammar.line_node()
    if counter in hl_lines:
        line_node["highlight"] = True
    else:
        line_node["highlight"] = False
    if with_counter:
        # add counter_node 1 at beginning of first line
        line_node.append(sphinxcontrib.igrammar.counter_node(counter+linenostart-1))

    for token in tokens:
        if token.type == eofToken:
            break
        tokenIndex=token.tokenIndex

        # add tokens in comment channel as comment node 
        if token.channel == commentChannel:
            # store text of all none-special tokens  after last special token in a Text node 
            counter, line_node = addTextNodes(nodes, text_pieces, with_counter, counter, line_node,hl_lines,linenostart)
            # add comment in special node comment_node
            text=token.text
            counter, line_node = add_nodes(nodes, sphinxcontrib.igrammar.comment_node, text, with_counter, counter, line_node,hl_lines,linenostart)
            continue

        if tokenIndex in tokenIndex2nodes:
            # reached special token 
            #  - the collected text of all none-special tokens until this special token is stored in  a Text node  
            counter, line_node = addTextNodes(nodes, text_pieces, with_counter, counter, line_node, hl_lines,linenostart)
            #  - add special token as a special node
            line_node.extend(tokenIndex2nodes[tokenIndex])
        else:
            # collect text of none-special token
            text_pieces.append(token.text)

    # store text of all none-special tokens  after last special token in a Text node
    # note: we add '\n' to end of text_pieces to so that also get last line not ending with newline
    counter , line_node = addTextNodes(nodes, text_pieces + ['\n'], with_counter, counter, line_node, hl_lines,linenostart)


    return nodes


def parse_into_docutils_nodes(text, env, namespace, docname, with_counter, hl_lines,linenostart):
    input_stream = InputStream(text)
    lexer = ANTLRv4Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ANTLRv4Parser(stream)

    # detect whether it is a full or partly grammar
    # and parse into tree accordingly using the right start rule
    if "grammar" in text:
        in_full_grammar = True
        tree = parser.grammarSpec()
        if tree.start.text not in ["parser", "lexer", "grammar"]:
            in_full_grammar = False
            # false positive:  grammar keyword used somewhere else in text
    else:
        in_full_grammar = False
        tree = parser.rules()

    # get walker 
    walker = ParseTreeWalker()

    # in first parse get rules in rulesDefined, so we can use it in the second pass
    # to check for a rule reference whether a rule is defined in the current grammar!
    rulesDefined = first_parse(walker, tree, env, namespace, in_full_grammar, docname)

    # second parse : link special docutil nodes to tokens (in tokenIndex2nodes)
    tokenIndex2nodes = second_parse(walker, tree, namespace, in_full_grammar, rulesDefined, docname)

    # translate tokens into nodes
    nodes = tokens2nodes(stream.tokens, tokenIndex2nodes, parser.EOF, lexer.COMMENT, with_counter,hl_lines,linenostart)
    return nodes


# def rewrite(text):
#     input_stream = InputStream(text)
#     lexer = ANTLRv4Lexer(input_stream)
#     stream = CommonTokenStream(lexer)
#     parser = ANTLRv4Parser(stream)
#     tree = parser.grammarSpec()
# 
#     rewriter = TokenStreamRewriter(tokens=stream);
#     listener = MyListener(rewriter)
#     walker = ParseTreeWalker()
#     walker.walk(listener, tree)
# 
#     return rewriter.getDefaultText()
# 
# 
# def main(argv):
#     input_stream = FileStream(argv[1])
#     lexer = ANTLRv4Lexer(input_stream)
#     stream = CommonTokenStream(lexer)
#     parser = ANTLRv4Parser(stream)
#     tree = parser.grammarSpec()
# 
#     rewriter = TokenStreamRewriter(tokens=stream);
#     ##print(rewriter.getText());
#     #print(rewriter.getDefaultText());
# 
#     listener = MyListener(rewriter)
#     walker = ParseTreeWalker()
#     walker.walk(listener, tree)
# 
#     print(rewriter.getDefaultText());
# 
# 
# if __name__ == '__main__':
#     main(sys.argv)
