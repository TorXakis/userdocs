
TorXakis Grammar
=======================


.. grammar:: torxakis
   :linenos:
   :emphasize-lines: 1,4,250
   :caption: ``TorXakis`` model
   :name: grammar_torxakis_model

    // Define TorXakis grammar 
    grammar TorXakisLanguageDefinition;

    // grammar rules
    model                   :       (   typeDefs
                                    |   funcDefs
                                    |   constDefs
                                    |   procDefs
                                    |   stautDefs
                                    |   channelDefs
                                    |   modelDef
                                    |   purpDef
                                    |   mapperDef
                                    |   cnectDef
                                    )* EOF;

    typeDefs                :       'TYPEDEF' typeDef (';' typeDef)* 'ENDDEF';
    typeDef                 :       typeName '::=' neConstructorList;

    funcDefs                :       'FUNCDEF' funcDef (';' funcDef)* 'ENDDEF';
    funcDef                 :       funcName '(' ( neVarsDeclarationList ) ')' '::' 
                                    typeName '::=' valExpr;

    constDefs               :       'CONSTDEF' constDef (';' constDef)* 'ENDDEF';
    constDef                :       constName '::' typeName '::=' valExpr;

    procDefs                :       'PROCDEF' procDef (';' procDef )* 'ENDDEF';
    procDef                 :       procName '[' ( neChannelsDeclList)? ']' 
                                    '(' (neVarDeclList)? ')' (exitDecl)? 
                                    '::=' processBehaviour;

    stautDefs               :       'STAUTDEF' stautDef (';' stautDef )* 'ENDDEF';
    stautDef                :       stautName '[' ( neChannelsDeclList)? ']' 
                                    '(' (neVarDeclList)? ')' (exitDecl)? 
                                    '::=' stautItems;

    channelDefs             :       'CHANDEF' channelDef 'ENDDEF';
    channelDef              :       channelDefName '::=' neChannelsDeclList;


    modelDef                :       'MODELDEF' modelName '::='
                                        'CHAN' 'IN'  ( neChannelNameList )?
                                        'CHAN' 'OUT' ( neChannelNameList )?
                                        'BEHAVIOUR' processBehaviour
                                    'ENDDEF';

    purpDef                 :       'PURPDEF' purpName '::='
                                        'CHAN' 'IN'  ( neChannelNameList )?
                                        'CHAN' 'OUT' ( neChannelNameList )?
                                        neTestGoals
                                    'ENDDEF';

    mapperDef               :       'MAPPERDEF' mapperName '::='
                                        'CHAN' 'IN'  ( neChannelsDeclList)?
                                        'CHAN' 'OUT' ( neChannelsDeclList )?
                                        'BEHAVIOUR' processBehaviour
                                    'ENDDEF';

    cnectDef                :       'CNECTDEF' cnectName '::='
                                        ( 'CLIENTSOCK' | 'SERVERSOCK' )
                                        connectionItem*
                                    'ENDDEF';


    exitDecl                :       'EXIT' ('::' neTypeNameList)?;


    stautItems              :       (    stateItem
                                    |    varItem
                                    |    initItem
                                    |    transItem
                                    )*;
    stateItem               :       'STATE' neIdNameList;
    neIdNameList            :       idName (',' idName)*;
    varItem                 :       'VAR' (neVarsDeclarationList)?;
    initItem                :       'INIT' idName (updateList)?;
    transItem               :       'TRANS' transition (';' transition)*;

    transition              :       idName '->' conditionalCommunications 
                                    (updateList)? '->' idName;

    updateList              :       '{' update (';' update )* '}';
    update                  :       varName ':=' valExpr;

    neConstructorList       :       constructor ( '|' constructor )*;
    constructor             :       constructorName  ( '{' neFieldList '}' )?;

    neFieldList             :       fields ( ';' fields )*;
    fields                  :       neFieldNameList '::' typeName;
    neFieldNameList         :       fieldName ( ',' fieldName )*;



    neTestGoals             :       testGoal (testGoal)*;
    testGoal                :       'GOAL' idName '::=' processBehaviour;

    connectionItem          :       (    connectionOut
                                    |    connectionIn
                                    |    encoding
                                    |    decoding
                                    );
    connectionOut           :       'CHAN' 'OUT' channelsDecl 
                                    'HOST' hostName 'PORT' portNumber;
    connectionIn            :       'CHAN' 'IN' channelsDecl 
                                    'HOST' hostName 'PORT' portNumber;
    encoding                :       'ENCODE' communication '->' channelOffer;
    decoding                :       'DECODE' communication '<-' channelOffer;



    neVarsDeclarationList   :       varsDeclaration (';' varsDeclaration )*;
    varsDeclaration         :       neVarNameList '::' typeName;
    neVarDeclList           :       varsDecl (';' varsDecl)*;
    varsDecl                :       neVarNameList '::' typeName;
    neVarNameList           :       varName (',' varName)*;

    neChannelsDeclList      :       channelsDecl ( ';' channelsDecl )*;
    channelsDecl            :       neChannelNameList ( '::' neTypeNameList)?;
    neChannelNameList       :       channelName (',' channelName)*;

    neTypeNameList          :       typeName ('#' typeName)*;



    processBehaviour        :       processBehaviourLevel1;

    processBehaviourLevel1  :       processBehaviourLevel2
                                    ( (  '>>>' processBehaviourLevel2 )
                                    | (  '>>>' 'ACCEPT' ( '?' (varDecls+=varDecl | 
                                         varName) | '!' valExpr )* 'IN' 
                                         processBehaviourLevel2 'NI' )
                                    | (  '[>>' processBehaviourLevel2 )
                                    | (  '[><' processBehaviourLevel2 )
                                    )*;

    processBehaviourLevel2:         processBehaviourLevel3
                                    ( ( '||' processBehaviourLevel3 )
                                    | ( '|||' processBehaviourLevel3 )
                                    | ( synchronizedChannels processBehaviourLevel3 )
                                    )*;

    processBehaviourLevel3:         processBehaviourLevel4
                                    ( (  '##' processBehaviourLevel4 )
                                    )*;

    processBehaviourLevel4:         processBehaviourGuarded
                                    | processBehaviourStop
                                    | processBehaviourSequence
                                    | procCall
                                    | processBehaviourLet
                                    | processBehaviourHide
                                    | processBehaviourBracket;

    procCall                :       procName '[' (neChannelNameList)? ']' 
                                    '(' (neValExprList)? ')';

    neValExprList           :       valExpr ( ',' valExpr )*;

    processBehaviourBracket :       '(' processBehaviourLevel1 ')';
    processBehaviourHide    :       'HIDE' '[' (neChannelsDeclList)? ']' 'IN' 
                                     processBehaviourLevel1 'NI';
    processBehaviourLet     :       'LET' assignment ( ';' assignment )* 'IN' 
                                    processBehaviourLevel1 'NI';
    processBehaviourSequence:       conditionalCommunications 
                                    ( '>->' processBehaviourLevel4 )?;
    processBehaviourGuarded :       condition '=>>' processBehaviourLevel4;
    processBehaviourStop    :       'STOP';

    synchronizedChannels    :       '|[' neChannelNameList ']|';


    conditionalCommunications:      communications (condition)?;

    communications          :       communication ( '|' communication )*;

    communication           :       ( (channelName | 'EXIT' ) channelOffer* );

    channelOffer            :       '!' valExpr | '?' (varDecls+=varDecl | varName);

    condition               :       '[[' valExpr ']]';

    assignment              :       ( varDecl | varName ) '=' valExpr;

    varDecl                 :       varName '::' typeName;

    valExpr                 :       valExpr1;

    valExpr1                :       valExpr2
                                    ( (  OPERATOR valExpr2 )
                                    | (  '::' typeName )
                                    )*
                                    | valExprLet
                                    | valExprIte;


    valExpr2                :       smallIdName // Temporarily solution for the 
                                    // conflict in the next two
                                    //        valExprConst
                                    //    |    valExprVar
                                    |    valExprUnaryOperator
                                    |    valExprFunctionCall
                                    |    valExprContructorCall
                                    |    valExprInteger
                                    |    valExprString
                                    |    valExprRegex
                                    |    valExprBracket
                                    |    valExprError;

    valExprUnaryOperator    :       OPERATOR valExpr2;

    smallIdName             :       SMALLID;

    valExprError            :       'ERROR' STRING;
    valExprIte              :       'IF' valExpr1 
                                    'THEN' valExpr1 'ELSE' valExpr1 'FI';
    valExprLet              :       'LET' assignment (';' assignment)* 
                                    'IN' valExpr1 'NI';
    valExprBracket          :       '(' valExpr ')';
    valExprRegex            :       'REGEX' '(' STRING ')';
    valExprString           :       STRING;
    valExprInteger          :       INT;
    valExprContructorCall   :       constructorName ( '(' neValExprList ')' )?;
    valExprFunctionCall     :       funcName '(' ( neValExprList )? ')';
    valExprVar              :       varName;
    valExprConst            :       constName;

    // identifier types
    portNumber              :       INT;

    hostName                :       STRING;

    idName                  :       SMALLID | CAPSID;

    modelName               :       CAPSID;
    purpName                :       CAPSID;
    mapperName              :       CAPSID;
    cnectName               :       CAPSID;
    stautName               :       CAPSID;
    channelDefName          :       CAPSID;
    constructorName         :       CAPSID;
    typeName                :       CAPSID;
    channelName             :       CAPSID;

    fieldName               :       SMALLID;
    procName                :       SMALLID;
    funcName                :       SMALLID;
    constName               :       SMALLID;
    varName                 :       SMALLID;

    // lexer rules; implicit lexer rules are in grammar rules above
    OPERATOR        : ( '=' | '+' | '-' | '*' | '^' | '/' | '\\' | '<' | '>' | 
                        '@' | '|' | '&' | '%' )+ ;
    CAPSID          : 'A'..'Z' ( 'A'..'Z' | 'a'..'z' | '0'..'9' | '_')*;
    SMALLID         : 'a'..'z' ( 'A'..'Z' | 'a'..'z' | '0'..'9' | '_')*;


    INT             : DIGIT+ ;
    fragment DIGIT : '0'..'9' ;

    STRING : '"' .*? '"' ; // match anything in "..."


    WS : [ \t\n\r]+ -> channel(1) ;

    LINE_COMMENT    : '--' .*? '\n' -> channel(2) ;
    BLOCK_COMMENT   : '{-' .*? '-}' -> channel(2) ;



