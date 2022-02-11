.. TorXakis Zoekresultatenocum documentation master file, created by
   sphinx-quickstart on Fri May 29 03:19:38 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



=======================================================
TorXakis User Documentation
=======================================================

.. comment
   .. helloworld::

       .. parsed-literal::

          ja  **jo**
             x

Some intro text here...

.. helloworld::

    ja  **jo**
       x

nested_list_parse


Some more text here...


.. parsed-literal::

   Hallo dit is een
       **parsed**
      :red:`literal`


.. rstgrammar::

   parser grammar ANTLRv4Parser;
   
   options { tokenVocab = ANTLRv4Lexer; }
   // The main entry point for parsing a v4 grammar.
   grammarSpec
      : grammarDecl prequelConstruct* rules modeSpec* EOF
      ;
   
   grammarDecl
      : grammarType identifier SEMI
      ;


.. grammar::

   parser grammar ANTLRv4Parser;
   
   options { tokenVocab = ANTLRv4Lexer; }
   // The main entry point for parsing a v4 grammar.
   grammarSpec
      : grammarDecl prequelConstruct* rules modeSpec* EOF
      ;
   
   grammarDecl
      : grammarType identifier SEMI
      ;
   
   grammarType
      : (LEXER GRAMMAR | PARSER GRAMMAR | GRAMMAR)
      ;
      // This is the list of all constructs that can be declared before
      // the set of rules that compose the grammar, and is invoked 0..n
      // times by the grammarPrequel rule.
   
   prequelConstruct
      : optionsSpec
      | delegateGrammars
      | tokensSpec
      | channelsSpec
      | action_
      ;
      // ------------
      // Options - things that affect analysis and/or code generation
   
   optionsSpec
      : OPTIONS (option SEMI)* RBRACE
      ;
   
   option
      : identifier ASSIGN optionValue
      ;
   
   optionValue
      : identifier (DOT identifier)*
      | STRING_LITERAL
      | actionBlock
      | INT
      ;
      // ------------
      // Delegates
   
   delegateGrammars
      : IMPORT delegateGrammar (COMMA delegateGrammar)* SEMI
      ;
   
   delegateGrammar
      : identifier ASSIGN identifier
      | identifier
      ;
      // ------------
      // Tokens & Channels
   
   tokensSpec
      : TOKENS idList? RBRACE
      ;
   
   channelsSpec
      : CHANNELS idList? RBRACE
      ;
   
   idList
      : identifier (COMMA identifier)* COMMA?
      ;
      // Match stuff like @parser::members {int i;}
   
   action_
      : AT (actionScopeName COLONCOLON)? identifier actionBlock
      ;
      // Scope names could collide with keywords; allow them as ids for action scopes
   
   actionScopeName
      : identifier
      | LEXER
      | PARSER
      ;






This is :red:`red text`.


External hyperlinks, like Python_.

Documentation version '|DOCVERSION|' for TorXakis version '|TOOLVERSION|'.

This documentation is also available as printable format as `PDF document <PDFDOCUMENTURL_>`_ .
For other versions see the `documentation overview webpage <DOCUMENT_OVERVIEW_URL_>`_.


.. toctree::
   :caption: Contents
   :maxdepth: 1

   intro
   getting-started
   mbt/index
   torxakis_mbt
   usage/index
   examples/index



.. raw:: latex

   \appendix


.. toctree::
   :caption: Appendices
   :maxdepth: 1

   Installation
   grammar/index
   command-line
   torxakis-help
   grammar
   grammarv3




\backmatter

.. toctree::
   :caption: Backmatter
   :maxdepth: 1

   glossary
   bibliography
   genindex
