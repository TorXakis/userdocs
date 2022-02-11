
get g4 parser/lexer from:
 https://github.com/antlr/grammars-v4/tree/master/antlr/antlr4

https://www.antlr.org/download.html -> python: 

  https://github.com/antlr/antlr4/blob/master/doc/python-target.md#python-2-and-3

    How to create a Python lexer or parser? This is pretty much the same as
    creating a Java lexer or parser, except you need to specify the language
    target, for example:

     $ antlr4 -Dlanguage=Python3 MyGrammar.g4
        `-> the java version of the antlr tool  => generates python3 source code!!

   => I did in this folder:

         antlr4  -Dlanguage=Python3 *.g4

  https://github.com/antlr/antlr4/blob/master/doc/python-target.md#where-can-i-get-the-runtime

  get python runtime library:

     pip3 install antlr4-python3-runtime



