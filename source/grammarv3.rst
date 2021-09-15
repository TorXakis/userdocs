
Grammarv3
=========


.. code-block:: antlr

    grammar TorXakisDsl;

    Model:
        (
            TypeDefs
        |   FuncDefs
        |   ConstDefs
        |   ProcDefs
        |   StautDefs
        |   ChannelDefs
        |   ModelDef
        |   PurpDef
        |   MapperDef
        |   CnectDef
        )*
    ;

    TypeDefs:
        'TYPEDEF' TypeDef (';' TypeDef)* 'ENDDEF'
    ;

    TypeDef:
        TypeName '::=' NeConstructorList
    ;

    FuncDefs:
        'FUNCDEF' FuncDef (';' FuncDef)* 'ENDDEF'
    ;

    FuncDef:
        FuncName '(' ( NeVarsDeclarationList ) ')' "::" TypeName "::=" ValExpr
    ;

    ConstDefs:
        'CONSTDEF' ConstDef (';' ConstDef)* 'ENDDEF'
    ;

    ConstDef:
        ConstName "::" TypeName "::=" ValExpr
    ;

    ProcDefs:
        'PROCDEF' ProcDef (';' ProcDef )* 'ENDDEF'
    ;

    ProcDef:
        ProcName '[' ( NeChannelsDeclList)? ']' '(' (NeVarDeclList)? ')' (ExitDecl)? '::=' ProcessBehaviour
    ;

    StautDefs:
        'STAUTDEF' StautDef (';' StautDef )* 'ENDDEF'
    ;

    StautDef:
        StautName '[' ( NeChannelsDeclList)? ']' '(' (NeVarDeclList)? ')' (ExitDecl)? '::=' StautItems
    ;

    ChannelDefs:
        'CHANDEF' ChannelDef
        // (';' ChannelDef )*
        'ENDDEF'
    ;

    ChannelDef:
        ChannelDefName '::=' NeChannelsDeclList
    ;

    ModelDef:
        'MODELDEF' ModelName '::='
            'CHAN' 'IN'  ( NeChannelNameList )?
            'CHAN' 'OUT' ( NeChannelNameList )?
            'BEHAVIOUR' ProcessBehaviour
        'ENDDEF'
    ;

    PurpDef:
        'PURPDEF' PurpName '::='
            'CHAN' 'IN'  ( NeChannelNameList )?
            'CHAN' 'OUT' ( NeChannelNameList )?
            NeTestGoals
        'ENDDEF'
    ;

    MapperDef:
        'MAPPERDEF' MapperName '::='
            'CHAN' 'IN'  ( NeChannelsDeclList)?
            'CHAN' 'OUT' ( NeChannelsDeclList )?
            'BEHAVIOUR' ProcessBehaviour
        'ENDDEF'
    ;

    CnectDef:
        'CNECTDEF' CnectName '::='
            ( 'CLIENTSOCK' | 'SERVERSOCK' )
            ConnectionItem*
        'ENDDEF'
    ;

    StautItems:
        (
                 StateItem
            |    VarItem
            |    InitItem
            |    TransItem
        )*
    ;

    StateItem:
        'STATE' NeIdNameList
    ;

    VarItem:
        'VAR' (NeVarsDeclarationList)?
    ;

    InitItem:
        'INIT' IdName (UpdateList)?
    ;

    TransItem:
        'TRANS' Transition (';' Transition)*
    ;

    Transition:
        IdName '->' ConditionalCommunications (UpdateList)? '->' IdName
    ;

    UpdateList:
        '{' Update (';' Update )* '}'
    ;

    Update:
        VarName ':=' ValExpr
    ;

    PurpName:
        CAPSID
    ;

    MapperName:
        CAPSID
    ;

    NeConstructorList:
        Constructor ( '|' Constructor )*
    ;

    Constructor:
        ConstructorName  ( '{' NeFieldList '}' )?
    ;

    NeFieldList:
        Fields ( ';' Fields )*
    ;

    Fields:
        NeFieldNameList '::' TypeName
    ;

    NeFieldNameList:
        FieldName ( ',' FieldName )*
    ;

    FieldName:
        SMALLID
    ;

    ExitDecl:
        'EXIT' ('::' NeTypeNameList)?
    ;


    ModelName:
        CAPSID
    ;

    NeTestGoals:
        TestGoal (testGoals+=TestGoal)*
    ;

    TestGoal:
        'GOAL' IdName '::=' ProcessBehaviour
    ;

    ConnectionItem:
        (
                 ConnectionOut
            |    ConnectionIn
            |    Encoding
            |    Decoding
        )
    ;

    ConnectionOut:
        'CHAN' 'OUT' ChannelsDecl 'HOST' HostName 'PORT' PortNumber
    ;

    ConnectionIn:
        'CHAN' 'IN' ChannelsDecl 'HOST' HostName 'PORT' PortNumber
    ;

    Encoding:
        'ENCODE' Communication '->' ChannelOffer
    ;

    Decoding:
        'DECODE' Communication '<-' ChannelOffer
    ;

    PortNumber:
        INT
    ;

    HostName:
        STRING
    ;

    StautName:
        CAPSID
    ;

    ChannelDefName:
        CAPSID
    ;

    ProcName:
        SMALLID
    ;

    CnectName:
        CAPSID
    ;

    NeVarsDeclarationList:
        VarsDeclaration (";" VarsDeclaration )*
    ;

    VarsDeclaration:
        NeVarNameList "::" TypeName
    ;

    NeVarDeclList:
        VarsDecl (";" VarsDecl)*
    ;

    VarsDecl:
        NeVarNameList "::" TypeName
    ;

    NeChannelsDeclList:
        ChannelsDecl ( ';' ChannelsDecl )*
    ;

    ChannelsDecl:
        NeChannelNameList ( '::' NeTypeNameList)?
    ;

    NeTypeNameList:
        TypeName ("#" TypeName)*
    ;

    TypeName:
        CAPSID
    ;

    NeChannelNameList:
        ChannelName ("," ChannelName)*
    ;

    NeIdNameList:
        IdName ("," IdName)*
    ;

    IdName:
             SMALLID
        |    CAPSID
    ;

    ChannelName:
        CAPSID
    ;

    NeVarNameList:
        VarName ("," VarName)*
    ;

    VarName:
        SMALLID
    ;

    ProcessBehaviour:
        ProcessBehaviourLevel1
    ;

    ProcessBehaviourLevel1:
        ProcessBehaviourLevel2
        ( (  '>>>' ProcessBehaviourLevel2 )
        | (  '>>>' 'ACCEPT' ( '?' (varDecls+=VarDecl | VarName) | '!' ValExpr )* 'IN' ProcessBehaviourLevel2 'NI' )
        | (  '[>>' ProcessBehaviourLevel2 )
        | (  '[><' ProcessBehaviourLevel2 )
        )*
    ;

    ProcessBehaviourLevel2:
        ProcessBehaviourLevel3
        ( (  '||' ProcessBehaviourLevel3 )
        | (  '|||' ProcessBehaviourLevel3 )
        | (  SynchronizedChannels ProcessBehaviourLevel3 )
        )*
    ;

    ProcessBehaviourLevel3:
        ProcessBehaviourLevel4
        ( (  '##' ProcessBehaviourLevel4 )
        )*
    ;

    ProcessBehaviourLevel4:
          ProcessBehaviourGuarded
        | ProcessBehaviourStop
        | ProcessBehaviourSequence
        | ProcCall
        | ProcessBehaviourLet
        | ProcessBehaviourHide
        | ProcessBehaviourBracket
    ;

    ProcCall:
        ProcName '[' (NeChannelNameList)? ']' '(' (NeValExprList)? ')'
    ;

    NeValExprList:
        ValExpr ( ',' ValExpr )*
    ;

    ProcessBehaviourBracket:
        '(' ProcessBehaviourLevel1 ')'
    ;

    ProcessBehaviourHide:
        'HIDE' '[' (NeChannelsDeclList)? ']' 'IN' ProcessBehaviourLevel1 'NI'
    ;

    ProcessBehaviourLet:
        'LET' Assignment ( ';' Assignment )* 'IN' ProcessBehaviourLevel1 'NI'
    ;

    ProcessBehaviourSequence:
        ConditionalCommunications ( '>->' ProcessBehaviourLevel4 )?
    ;

    ProcessBehaviourGuarded:
        Condition '=>>' ProcessBehaviourLevel4
    ;


    ProcessBehaviourStop:
        'STOP'
    ;

    SynchronizedChannels:
        '|[' NeChannelNameList ']|'
    ;


    ConditionalCommunications:
        Communications (Condition)?
    ;

    Communications:
        Communication ( '|' Communication )*
    ;

    Communication:
        ( (ChannelName | 'EXIT' ) ChannelOffer*
        )
    ;

    ChannelOffer:
        '!' ValExpr | '?' (varDecls+=VarDecl | VarName)
    ;

    Condition:
        '[[' ValExpr ']]'
    ;

    Assignment:
        ( VarDecl | VarName ) '=' ValExpr
    ;

    VarDecl:
        VarName '::' TypeName
    ;

    ValExpr:
        ValExpr1
    ;

    ValExpr1:
        ValExpr2
        ( (  OPERATOR ValExpr2 )
        | (  '::' TypeName )
        )*
        | ValExprLet
        | ValExprIte
    ;


    ValExpr2:
            SmallIdName // Temporarily solution for the conflict in the next two
    //        ValExprConst
    //    |    ValExprVar
        |    ValExprUnaryOperator
        |    ValExprFunctionCall
        |     ValExprContructorCall
        |    ValExprInteger
        |    ValExprString
        |     ValExprRegex
        |    ValExprBracket
        |    ValExprError
    ;

    ValExprUnaryOperator:
        OPERATOR ValExpr2
    ;

    SmallIdName:
        SMALLID
    ;

    ValExprError:
        'ERROR' STRING
    ;

    ValExprIte:
        'IF' ValExpr1 'THEN' ValExpr1 'ELSE' ValExpr1 'FI'
    ;

    ValExprLet:
        'LET' Assignment (';' Assignment)* 'IN' ValExpr1 'NI'
    ;

    ValExprBracket:
        '(' ValExpr ')'
    ;

    ValExprRegex:
        'REGEX' '(' STRING ')'
    ;

    ValExprString:
        STRING
    ;

    ValExprInteger:
        BIG_INT
    ;

    ValExprContructorCall:
        ConstructorName ( '(' NeValExprList ')' )?
    ;

    ValExprFunctionCall:
        FuncName '(' ( NeValExprList )? ')'
    ;


    ValExprVar:
        VarName
    ;

    ValExprConst:
        ConstName
    ;

    ConstructorName:
        CAPSID
    ;

    FuncName:
        SMALLID
    ;

    ConstName:
        SMALLID
    ;

    OPERATOR       : ( '=' | '+' | '-' | '*' | '^' | '/' | '\\' | '<' | '>' | '@' | '|' | '&' | '%' )+ ;
    CAPSID         : 'A'..'Z' ( 'A'..'Z' | 'a'..'z' | '0'..'9' | '_')*;
    SMALLID        : 'a'..'z' ( 'A'..'Z' | 'a'..'z' | '0'..'9' | '_')*;
    SL_COMMENT     : '--' !('\n'|'\r')* ('\r'? '\n')?;
    ML_COMMENT     : '{-' -> '-}';
    BIG_INT:
        INT
    ;
