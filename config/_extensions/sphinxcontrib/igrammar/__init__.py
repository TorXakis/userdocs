from os import path

from docutils.nodes import document
from docutils.nodes import Element, Node
from docutils.parsers.rst import directives, Directive
import docutils
from docutils.parsers.rst.roles import set_classes
from docutils import nodes
from docutils.statemachine import StringList
from sphinx.application import Sphinx
from sphinx.directives.code import container_wrapper
from sphinx.util.docutils import SphinxDirective

import pprint

from sphinx.util.nodes import set_source_info
#from sphinx.util.typing import OptionSpec

from sphinxcontrib.igrammar.rewriter import parse_into_docutils_nodes
from sphinx.locale import __
from sphinx.util import logging, parselinenos

logger = logging.getLogger(__name__)

# used ideas from /usr/local/lib/python3.9/site-packages/sphinx/ext/graphviz.py


# about reference label
#
# https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-ref
#  To support cross-referencing to arbitrary locations in any document, the standard reST labels are used.
#  For this to work label names must be unique throughout the entire documentation.
#
# so what are these 'standard reST labels' :
#
# https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#reference-names
# Simple reference names are single words consisting of alphanumerics plus isolated (no two adjacent)
# internal hyphens, underscores, periods, colons and plus signs; no whitespace or other characters are allowed.
#
# Reference names are whitespace-neutral and case-insensitive. When resolving reference names internally:
#
#  - whitespace is normalized (one or more spaces, horizontal or vertical tabs, newlines, carriage returns,
#                              or form feeds, are interpreted as a single space)
#  - case is normalized (all alphabetic characters are converted to lowercase).
#
# For example, the following hyperlink references are equivalent:
#  - `A HYPERLINK`_
#  - `a    hyperlink`_
#  - `A
#    Hyperlink`_

# WORKS
# self.env.app.env.domaindata["std"]["anonlabels"][<ref_id>] = <file>, <node_id>
# ref id (MUST BE LOWERCASE and Space normalize)
#  <node_id> is id of target node (anchor name in html4 days)



# ref labeling convention:
#   extension prefix to prevent name conflicts in reference names
#
#     node id  => anchor label
#
#     ref label => used in rest
#
#    => both must be unique!
#        only adding prefix to node_id does not help
#        having unique node_id but still having a conflict in ref label does not help
#
#    for generate grammar targets. => add "grammar_" prefix. => ref label becomes long, but that's fine!
#                                     so we less likely get conflict with user choosen ref labels
#    however for self set "name" ref label   => end user should be carefull to choose it unique!
#
#    choosen:
#
#      g-torxakis-full-funcDefs
#      g-torxakis-part-funcDefs
#
#    because:
#      * use - instead of _. (don't use both - and : because of KISS)
#      * g- is clear
#      * full and part clearer then only f or p
#      * follows convention labels go from general to more specific
#          full/part is more specific then torxakis
#        following this convention makes that when sorting the labels
#        labels more close related are nearer in the sort order
#





# def role_rule_ref(name, rawtext, text, lineno, inliner, options={}, content=[]):
#     color="red"
#     target="https://www.nu.nl"
#     node_ref = nodes.reference("", "", refuri=target)
#     node_color = nodes.inline(text=text, classes=[color])
#     node_ref.append(node_color)
#     return [node_ref], []
# 
# 
# def role_rule_def(name, rawtext, text, lineno, inliner, options={}, content=[]):
#     color="blue"
#     node = nodes.inline(text=text, classes=[color])
#     return [node], []
# 
# 
# def role_terminal(name, rawtext, text, lineno, inliner, options={}, content=[]):
#     color="green"
#     node = nodes.inline(text=text, classes=[color])
#     return [node], []



def container_wrapper(directive: SphinxDirective, literal_node: Node, caption: str) -> nodes.container:  # NOQA

    container_node = nodes.container()
    parsed = nodes.Element()
    directive.state.nested_parse(StringList([caption], source=''),
                                 directive.content_offset, parsed)
    # note: parsing like this gives extra paragraph element around parsed caption restcode
    #       which is fine because that gives use a line space between caption and literal block

    if isinstance(parsed[0], nodes.system_message):
        msg = __('Invalid caption: %s' % parsed[0].astext())
        raise ValueError(msg)
    elif isinstance(parsed[0], nodes.Element):
        # blockquote header (four times nested to get same indent as caption in code block)
        caption_node = nodes.block_quote()
        caption_node_1 = nodes.block_quote()
        caption_node_2 = nodes.block_quote()
        caption_node_3 = nodes.block_quote(parsed.rawsource, *parsed.children)
        caption_node += caption_node_1
        caption_node_1 += caption_node_2
        caption_node_2 += caption_node_3

        caption_node.source = literal_node.source
        caption_node.line = literal_node.line

        # we use a hack to place the code_block in latex somewhat closer to the literal block (otherwise doesn't look like caption)
        # https://tex.stackexchange.com/questions/83275/how-to-eliminate-vertical-space-before-and-after-verse-environment
        latex_add_whiteline_before_caption= nodes.raw('',r'\vspace{\baselineskip}', format='latex')
        latex_remove_whiteline_after_caption= nodes.raw('',r'\vspace{-\baselineskip}', format='latex')
        container_node += latex_add_whiteline_before_caption
        container_node += caption_node
        container_node += latex_remove_whiteline_after_caption
        container_node += literal_node
        return container_node
    else:
        raise RuntimeError  # never reached

# https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html?highlight=code-block#directive-option-code-block-linenos
# -> support same options
class Grammar(SphinxDirective):
    has_content = True
    required_arguments = 1

    #option_spec: OptionSpec = {
    option_spec = {
        'linenos': directives.flag,
        'lineno-start': int,
        'emphasize-lines': directives.unchanged_required,
        'caption': directives.unchanged_required,
        'class': directives.class_option,
        'name': directives.unchanged,
    }

    def run(self):
        location = self.state_machine.get_source_and_line(self.lineno)
        # add extra prefix "g-" (for grammar) to namespace to prevent conflicts with other reference labels
        namespace="g-" + self.arguments[0]

        # fetch class option into classes option, and remove class option (historical reasons)
        self.options['classes'] = self.options.get('class', [])
        if 'class' in self.options: del self.options['class']
        # set highlighter class in directive node ; needed for html builder to use pygments highlighter css rules
        self.options['classes'].append("highlight")

        with_counter = 'linenos' in self.options

        linenostart = 1
        if 'lineno-start' in self.options:
            with_counter = True
            linenostart = self.options['lineno-start']

        linespec = self.options.get('emphasize-lines')
        if linespec:
            try:
                nlines = len(self.content)
                hl_lines = parselinenos(linespec, nlines)
                if any(i >= nlines for i in hl_lines):
                    logger.warning(__('line number spec is out of range(1-%d): %r') %
                                   (nlines, self.options['emphasize-lines']),
                                   location=location)

                hl_lines = [x + 1 for x in hl_lines if x < nlines]
            except ValueError as err:
                return [document.reporter.warning(err, line=self.lineno)]
        else:
            hl_lines = []


        # get text from directive    
        self.assert_has_content()
        text = '\n'.join(self.content)

        # parse text antlr listener
        docname=self.env.docname # docname is relative filepath from source/ directory without file extension!
                                 # where self.get_source_info()[0] is absolute path of rst file
        text_nodes = parse_into_docutils_nodes(text,self.env,namespace,docname,with_counter,hl_lines,linenostart)


        # hack to color background in code box in latex/pdf output
        startbox=nodes.raw('', r'\begin{frshaded}', format='latex')
        endbox = nodes.raw('', r'\end{frshaded}', format='latex')
        text_nodes= [startbox] + text_nodes + [endbox]
        

        # literal block preserves preformatted text
        # so all formatting of the text in its child nodes is kept
        #
        # technical detail in latex/html writer in method  visit_literal_block
        # (files sphinx/writers/latex.py and sphinx/writers/html.py):
        #
        #     if node.rawsource == node.astext()
        #     then
        #        handled as codeblock/highlightblock
        #        => gives raw_source to  pygments in builder
        #           and ignores child nodes!!
        #     else
        #        used as literal block which preserves preformatted text
        #        by processing all child nodes (for parsed literal) and preserving their text
        #
        # because we do not want pygments, but a literal block, we
        # do not:
        #    code = '\n'.join(self.content)
        #    node = nodes.literal_block(code,'', *text_nodes, **self.options)
        # but just:
        literal_node = nodes.literal_block("not needed", "", *text_nodes, **self.options)



        ## wrap in container using selfmade container_wrapper with selfmade caption
        caption =  self.options.get('caption')
        if caption:
            caption = "Grammar: " + caption
            try:
                # we use our own container_wrapper with our own implementation of caption and target reference
                #
                # note: we don't use the container_wrapper  in /directives/code.py  adds caption to a literal_node by
                #       wrapping them together in a container node.
                #       This container wrapper is made specially for code-blocks and it doesn't
                #       work correctly for wrapping a self-defined literal block! ( gives broken caption in latex)

                #       The latex builder generates \sphinxVerbatim env with caption \sphinxSetupCaptionForVerbatim for code block,
                #       and \alltt  env with caption \caption. The problem is that \caption gives error with \alltt env
                #       which can only be solved by wrapping it in a float. Captions are only allowed in floats!
                #       However we do not want our verbatim env (alltt) to float, because it is breakable over pages.
                #       Floating should only be used for things which are not breakable over pages!
                #
                # note: we don't use a figure_wrapper  such as done with ./ext/graphviz.py
                #       because the following problems:
                #         - in pdf a long grammar will overflow on a page, and will not break over multiple pages!
                #         - caption is put below figure  => for grammars it is nicer that is put above because they can be long
                #         - in pdf the figure floats to later pages because does not fit, because grammars are big
                #            => better to use a verbatim environment which breaks in pieces over the different pieces, and doesn't
                #               float!  Floating should only be used for stuff which cannot break across pages!!
                literal_node = container_wrapper(self, literal_node, caption)
            except ValueError as exc:
                return [document.reporter.warning(exc, line=self.lineno)]

        if 'name' in self.options:
            #name = self.options.pop('name')
            name = self.options.get('name')

            # Get anchor label and default reference text (text shown for Automatic labeled reference)
            #
            # Do not use caption as reference text because it is a longer description which is too long
            # for an inline reference, and can contain inline rest instructions.
            # Instead use the 'name' option text, which can also act as anchor label after normalizing.
            reference_text=name
            # anchor is  lower cased and whitespace-normalized 'name':
            anchor = nodes.fully_normalize_name(name)
            # note: when using anchor in reference you can use any case variant because anchors are case-invariant
            #       (given anchor is always lowercased which is used as real anchor)

            # # register in standard domain so that we can use sphinx :ref:
            # # src: https://stackoverflow.com/questions/64146870/generating-labels-for-nodes-of-a-custom-directive
            # # for Explicit labeled reference  :ref:`custom reference text <anchor>` => shows "custom reference text" for reference in document
            self.env.domaindata["std"]["anonlabels"][anchor] = self.env.docname, anchor
            # # for Automatic labeled reference :ref:`anchor`   => shows reference_text for reference in document
            self.env.domaindata["std"]["labels"][anchor] = self.env.docname, anchor, reference_text
            #
            # below function does same as above code!
            # note: comment in note_hyperlink_target says
            #
            #            This is only for internal use.  Please don't use this from your extension.
            #            ``document.note_explicit_target()`` or ``note_implicit_target()`` are recommended to
            #            add a hyperlink target to the document.
            #
            #            This only adds a hyperlink target to the StandardDomain.  And this does not add a
            #            node_id to node.  Therefore, it is very fragile to calling this without
            #            understanding hyperlink target framework in both docutils and Sphinx.
            #
            #    however we explicit define a hyperlink target ourselves so we can safely call this function
            #    to register this reference label with its optional default reference_text.
            #    note: also tried to use  note_explicit_target and note_implicit_target functions instead
            #          but I only got note_explicit_target to work, but not note_implicit_target
            #stddomain=self.env.domains['std']
            #stddomain.note_hyperlink_target(anchor, self.env.docname, anchor, reference_text)
            # does both anonlabels and labels

            # create target node
            target_node = nodes.target('', '', ids=[anchor])
            return [target_node, literal_node]

        return [literal_node]





# class RstGrammar(SphinxDirective):
#     has_content = True
# 
#     def run(self):
#         set_classes(self.options)
#         self.assert_has_content()
#         text = '\n'.join(self.content)
# 
#         # parse text with my anltr tokenstreamrewriter
#         rst_text=rewrite(text)
#         text_nodes, messages = self.state.inline_text(rst_text, self.lineno)
# 
#         node = nodes.literal_block(text, '', *text_nodes, **self.options)
#         return [node] 






def merge_ruledefs(app, env, docnames, other):
    if not hasattr(env, 'ruledefs'):
        env.ruledefs = []
    if hasattr(other, 'ruledefs'):
        env.ruledefs.extend(other.ruledefs)

def purge_ruledefs(app, env, docname):
    if not hasattr(env, 'ruledefs'):
        return
    env.ruledefs = [ruledef for ruledef in env.ruledefs if ruledef['docname'] != docname]


def process_ruledefs(app, env):
    """ define dictionary to lookup where a rule is defined in other file.
        This dictionary can only be build when all files are parsed.
        Note: we store a simple list of ruledef info in env per file, so that it can easily be 
              merged and purged in parallel. 
    """
    if not hasattr(env, 'ruledefs'):
        return
    env.grammar_rule2docname={}
    for ruledef in env.ruledefs:
        key=(ruledef['namespace'],ruledef['in_full_grammar'],ruledef['rulename'])
        env.grammar_rule2docname[key]=ruledef['docname']

        # register anchor in environment so that we can use :ref: roles to
        # refer to a grammar rule
        if ruledef['in_full_grammar']:
            anchor = ruledef['namespace'] + "-full-" + ruledef['rulename']
        else:
            anchor = ruledef['namespace'] + "-part-" + ruledef['rulename']
        #env.domaindata["std"]["anonlabels"][anchor.lower()] = ruledef['docname'], anchor
        reference_text=ruledef['rulename']

        #env.domains['std'].note_hyperlink_target(anchor.lower(), ruledef['docname'], anchor, reference_text)

        env.domaindata["std"]["anonlabels"][anchor.lower()] = ruledef['docname'], anchor
        env.domaindata["std"]["labels"][anchor.lower()] = ruledef['docname'], anchor, reference_text




# for each 

#  "grammarType": "purple",
type2color = {
    "grammarType_node": "k", 
    "grammarName_node": "teal",
    "rule_def_node": "blue",
    "rule_ref_node": "green",
    "token_def_node": "brown",
    "token_ref_node": "olive",
    "terminal_node": "brown",
    "comment_node": "darkgray",
    "counter_node": "darkgray"
}


#class line_node(docutils.nodes.inline):
class line_node(nodes.General, nodes.Element):

    def replaceWithNodes(self):
        #color = type2color[self.__class__.__name__]
        # \colorbox{BurntOrange}{orange background}
        #if hasattr(self, 'highlight'):
        #if self["highlight"]:
        if self.has_key("highlight") and self["highlight"]:
        #if self.hasattr("highlight"):
            color="bgblue"
            new_node = docutils.nodes.inline(classes=[color])
        else: 
            new_node = docutils.nodes.inline()

        new_node.extend(self.children)
        self.replace_self(new_node)
        #self.replace_self(self.children)


        #node = nodes.literal_block("not needed", "", *text_nodes, **self.options)
        #return [node]


class text_color_node(nodes.General, nodes.Element):

    def replaceWithNodes(self):
        color = type2color[self.__class__.__name__]
        new_node = docutils.nodes.inline(text=self.rawsource, classes=[color])
        self.replace_self(new_node)

class grammarType_node(text_color_node):
      pass

class grammarName_node(text_color_node):
      pass

class counter_node(text_color_node):

    def replaceWithNodes(self):
        counter=self.rawsource
        self.rawsource="{:3d}  ".format(counter)
        super().replaceWithNodes()

class comment_node(text_color_node):
      pass

class terminal_node(text_color_node):
      pass


class baseRef(nodes.General, nodes.Element):
    
    def replaceWithNodes(self, app,dst_docname):
        
        env = app.builder.env
        # we need to lookup filename of a def in other file  so that we can link to it
        # notes: 
        #   for a part grammar file the other file is full grammar file
        #   for the full  grammar file the other file is a part grammar file
        #   where we assume
        #    - each grammar has only one full grammar file defined
        #    - each rule is only defined at max once in the full grammar file and at max once in a part grammar file
        key = (self['namespace'],not self['in_full_grammar'],self['rulename'])
        dst_docname = None
        if key in env.grammar_rule2docname:
            dst_docname=env.grammar_rule2docname[key]

#class token_ref_node(baseRef):
class token_ref_node(nodes.General, nodes.Element):

    def replaceWithNodes(self, app,dst_docname):
        
        #dst_docname=self['dst_docname']
        new_nodes = []
        
        rule_label = self['rulename']
        src_docname = self['docname']
        rule_defined_local = self['rule_defined_local']
        color = type2color[self.__class__.__name__]
        node_text = docutils.nodes.inline(text=rule_label, classes=[color])

        if rule_defined_local:
            # refer to rule in same grammar page 
            if self['in_full_grammar']:
                anchor = self['namespace'] + "-full-" + rule_label
            else:
                anchor = self['namespace'] + "-part-" + rule_label
            refuri='#' + anchor
            ref_node = docutils.nodes.reference("", "", refuri=refuri)
            ref_node.append(node_text)
            new_nodes.append(ref_node)
        else:
            # refer to rule in full grammar page 
            if dst_docname is None:
                # rule not defined in current grammar and global grammar
                # no reference, only colored text for rule display
                new_nodes.append(node_text)
            else: 
                # refer to rule in full grammar page (assume defined there)
                anchor = self['namespace'] + "-full-" + rule_label
                refuri = app.builder.get_relative_uri(src_docname, dst_docname)  + '#' + anchor
                ref_node = docutils.nodes.reference("", "", refuri=refuri)
                ref_node.append(node_text)
                new_nodes.append(ref_node)

        self.replace_self(new_nodes)

class token_def_node(nodes.General, nodes.Element):

    def replaceWithNodes(self, app,dst_docname):
        new_nodes = []
        rule_label = self['rulename']
        src_docname = self['docname']

        #color = type2color["token_def"]
        color = type2color[self.__class__.__name__]
        node_text = docutils.nodes.inline(text=rule_label, classes=[color])

        # create a target node to link to
        if self['in_full_grammar']:
            targetid = self['namespace'] + "-full-" + rule_label
        else:
            targetid = self['namespace'] + "-part-" + rule_label
        target_node = docutils.nodes.target('', '', ids=[targetid])
        new_nodes.append(target_node)

        if dst_docname is None:
            # no destination found,then no reference node is needed, just use text node
            new_nodes.append(node_text)
        else:
            # create reference node to destination ( which contains text node as child)
            if self['in_full_grammar']:
                anchor = self['namespace'] + "-part-" + rule_label
            else:
                anchor = self['namespace'] + "-full-" + rule_label
            ref_node = docutils.nodes.reference("", "")
            ref_node['refdocname'] = dst_docname
            ref_node['refuri'] = app.builder.get_relative_uri(src_docname, dst_docname) + '#' + anchor
            ref_node.append(node_text)
            new_nodes.append(ref_node)

        self.replace_self(new_nodes)

class rule_ref_node(nodes.General, nodes.Element):

    def replaceWithNodes(self, app,dst_docname):
        new_nodes = []
        rule_label = self['rulename']
        src_docname = self['docname']
        rule_defined_local = self['rule_defined_local']
        color = type2color[self.__class__.__name__]
        node_text = docutils.nodes.inline(text=rule_label, classes=[color])

        if rule_defined_local:
            # refer to rule in same grammar page 
            if self['in_full_grammar']:
                anchor = self['namespace'] + "-full-" + rule_label
            else:
                anchor = self['namespace'] + "-part-" + rule_label
            refuri='#' + anchor
            ref_node = docutils.nodes.reference("", "", refuri=refuri)
            ref_node.append(node_text)
            new_nodes.append(ref_node)
        else:
            # refer to rule in full grammar page 
            if dst_docname is None:
                # rule not defined in current grammar and global grammar
                # no reference, only colored text for rule display
                new_nodes.append(node_text)
            else: 
                # refer to rule in full grammar page (assume defined there)
                anchor = self['namespace'] + "-full-" + rule_label
                refuri = app.builder.get_relative_uri(src_docname, dst_docname)  + '#' + anchor
                ref_node = docutils.nodes.reference("", "", refuri=refuri)
                ref_node.append(node_text)
                new_nodes.append(ref_node)

        self.replace_self(new_nodes)


class rule_def_node(nodes.General, nodes.Element):

    def replaceWithNodes(self, app,dst_docname):
        new_nodes = []
        rule_label = self['rulename']
        src_docname = self['docname']
        #color = type2color["rule_def"]
        color = type2color[self.__class__.__name__]
        node_text = docutils.nodes.inline(text=rule_label, classes=[color])

        # create a target node to link to
        if self['in_full_grammar']:
            targetid = self['namespace'] + "-full-" + rule_label
        else:
            targetid = self['namespace'] + "-part-" + rule_label

        #nodeId = docutils.nodes.make_id(targetid)
        
        #  works with target node with id targetid
        target_node = docutils.nodes.target('', '', ids=[targetid])
        new_nodes.append(target_node)

        if dst_docname is None:
            # no destination found,then no reference node is needed, just use text node
            new_nodes.append(node_text)
        else:
            # create reference node to destination ( which contains text node as child)
            if self['in_full_grammar']:
                anchor = self['namespace'] + "-part-" + rule_label
            else:
                anchor = self['namespace'] + "-full-" + rule_label
            ref_node = docutils.nodes.reference("", "")
            ref_node['refdocname'] = dst_docname
            ref_node['refuri'] = app.builder.get_relative_uri(src_docname, dst_docname) + '#' + anchor
            ref_node.append(node_text)
            new_nodes.append(ref_node)

        self.replace_self(new_nodes)






def resolve_special_grammar_nodes(app, doctree, fromdocname):



    # pprint.pprint("-----------")
    # pprint.pprint(fromdocname)
    # pprint.pprint("-----------")


    env = app.builder.env

    if not hasattr(env, 'ruledefs'):
        return

    color_nodes = list(doctree.traverse(line_node))
    for node in color_nodes:
        node.replaceWithNodes()

    # replace each rule_def node with other nodes using node.replaceWithNodes
    #node: rule_def_node or token_def_node
    def_nodes= list(doctree.traverse(rule_def_node)) + list(doctree.traverse(token_def_node)) + \
               list(doctree.traverse(rule_ref_node)) + list(doctree.traverse(token_ref_node))
    for node in def_nodes:
        
        dst_docname = None
        # we need to lookup filename of a def in other file  so that we can link to it
        # notes: 
        #   for a part grammar file the other file is full grammar file
        #   for the full  grammar file the other file is a part grammar file
        #   where we assume
        #    - each grammar has only one full grammar file defined
        #    - each rule is only defined at max once in the full grammar file and at max once in a part grammar file
        key = (node['namespace'],not node['in_full_grammar'],node['rulename'])
        dst_docname = None
        if key in env.grammar_rule2docname:
            dst_docname=env.grammar_rule2docname[key]

        node.replaceWithNodes(app, dst_docname)

    # ref_nodes = list(doctree.traverse(rule_ref_node))
    # for node in ref_nodes:
    #     dst_docname = None
    #     node.replaceWithNodes(app, dst_docname)
        
    color_nodes = list(doctree.traverse(grammarName_node))  +  list(doctree.traverse(grammarType_node))\
                   + list(doctree.traverse(terminal_node))  +  list(doctree.traverse(comment_node))\
                   + list(doctree.traverse(counter_node))
    for node in color_nodes:
        node.replaceWithNodes()


def setup(app: Sphinx):
    # for color in colors:
    #     app.add_role(color,role_textcolor(color))
    app.add_directive("grammar", Grammar)
    #app.add_directive("oldgrammar", RstGrammar)

    # app.add_role("rule_ref", role_rule_ref)
    # app.add_role("rule_def", role_rule_def)
    # app.add_role("terminal", role_terminal)


    #app.connect('missing-reference', process_missing_reference)
    # only used for references in restructured text source, but not
    # in custom directives added docutil.nodes.reference  node!
    # Instead must use env object to fix links in custom directive yourself

    # app.env not yet defined
    # app.env['ruledefs'] = [] # list of all  ruledef anonymous objects

 
    # # https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx-core-events
    # app.connect('config-inited',  on_config_inited)
    # app.connect('builder-inited', on_build_inited)
    # app.connect('build-finished', on_build_finished)
    # app.connect('doctree-resolved', process_todo_nodes)

    app.connect('env-updated', process_ruledefs)
    app.connect('doctree-resolved', resolve_special_grammar_nodes)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }