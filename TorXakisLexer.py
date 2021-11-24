from pygments.lexer import RegexLexer,words
from pygments.token import *

from pygments.styles import get_all_styles

__all__ = ['TorXakisLexer', 'TorXakisCmdLexer']



#styles = list(get_all_styles())
#print(styles)

class TorXakisLexer(RegexLexer):
    name = 'TorXakis'
    aliases = ['torxakis','txs']
    filenames = ['*.txs']
    
    keywords=('CNECTDEF', 'SERVERSOCK' , 'CLIENTSOCK' , 'DECODE' , 'ENCODE' , 'MODELDEF', 'CHANDEF', 'STAUTDEF','STATE','VAR','INIT','TRANS', 'TYPEDEF','FUNCDEF','CONSTDEF','PROCDEF','SPECDEF','ADAPDEF','SUTDEF','ENDDEF','SUT','CHAN','MAP','SOCK','IN','OUT','HOST','PORT','BEHAVIOUR','STOP','EXIT','ACCEPT','HIDE','LET','NI','BEGIN','END','IF','THEN','ELSE','FI','ISTEP','ERROR')
    proc_operators=('->' ,'[]' ,'##' ,'>->' ,'>>>' ,'[>>' ,'[><' ,'::' ,'::=' ,'=>>' ,'||' ,'|||' ,'|[' ,']|' ,'[[' ,']]') 
    symbols=('[' ,']' ,'{' ,'}' ,'(' ,')' ,'?' ,'!' ,'#' ,';' ,',' ,'\'' ,'"' ,'_') 
    expr_operators=('=' ,'|' ,'+' ,'-' ,'*' ,'^' ,'/' ,'\\' ,'<' ,'>' ,'@' ,'&' ,'%')


    tokens = {
        'root': [
          #  (r'\s+', Text),
            (r'--.*?$', Comment),
            (words(keywords, prefix=r'\b', suffix=r'\b'), Keyword),
          #  (words(('STATE', 'True', 'False', 'None'), suffix=r'\b'), Keyword.Constant),
           (words(proc_operators), String),       # causes warning
           (words(symbols), Punctuation),
            (words(expr_operators), Operator),
            (r'[ \r\t\n\u000C]+', Text),
            (r'\b[a-z]\w*', Name.Class), # SmallId
            (r'\b[A-Z]\w*', Name.Variable), # CapsId
            (r'"((?:""|[^"])*)"', String),  # "Double Quoted String"
            (r'\b\d+\b', String), #  Number
            #(r'.', Token.Error),
            (r'.',  Text),
        ]
    }


class TorXakisCmdLexer(RegexLexer):
    name = 'TorXakis Command Session'
    aliases = ['torxakiscmd','txscmd']
    filenames = []

    commands=('q','quit','x','h','i','exit','help','info','param','echo','seed','delay','time','timer','run','var','val','eval','solve','unisolve','tester','simulator','stepper','stop','test','test','test','sim','step','ste','show','state','btree','goto','back','path','trace','menu','ncomp','le','lpeop','merge','systart','systop')

    output=("PASS")

    #keywords=('CNECTDEF', 'SERVERSOCK' , 'CLIENTSOCK' , 'DECODE' , 'ENCODE' , 'MODELDEF', 'CHANDEF', 'STAUTDEF','STATE','VAR','INIT','TRANS', 'TYPEDEF','FUNCDEF','CONSTDEF','PROCDEF','SPECDEF','ADAPDEF','SUTDEF','ENDDEF','SUT','CHAN','MAP','SOCK','IN','OUT','HOST','PORT','BEHAVIOUR','STOP','EXIT','ACCEPT','HIDE','LET','NI','BEGIN','END','IF','THEN','ELSE','FI','ISTEP','ERROR')
    #proc_operators=('->' ,'[]' ,'##' ,'>->' ,'>>>' ,'[>>' ,'[><' ,'::' ,'::=' ,'=>>' ,'||' ,'|||' ,'|[' ,']|' ,'[[' ,']]')
    #symbols=('[' ,']' ,'{' ,'}' ,'(' ,')' ,'?' ,'!' ,'#' ,';' ,',' ,'\'' ,'"' ,'_')
    expr_operators=('=' ,'|' ,'+' ,'-' ,'*' ,'^' ,'/' ,'\\' ,'<' ,'>' ,'@' ,'&' ,'%')


    tokens = {
        'root': [
          #  (r'\s+', Text),
            (r'TXS >>', String),  # Punctuation
            (r'#.*?$', Comment),
            (words(commands, prefix=r'\b', suffix=r'\b'), Keyword),
            (words(output, prefix=r'\b', suffix=r'\b'), Keyword),
          #  (words(('STATE', 'True', 'False', 'None'), suffix=r'\b'), Keyword.Constant),
           #(words(proc_operators), String),       # causes warning
           #(words(symbols), Punctuation),
            (words(expr_operators), Operator),
            (r'[ \r\t\n\u000C]+', Text),
            #(r'\b[a-z]\w*', Name.Class), # SmallId
            #(r'\b[A-Z]\w*', Name.Variable), # CapsId
            (r'"((?:""|[^"])*)"', String),  # "Double Quoted String"
            (r'\b\d+\b', String), #  Number
            #(r'.', Token.Error),
            (r'.',  Text),
        ]
    }