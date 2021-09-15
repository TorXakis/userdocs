.. code-block:: antlr
 
    // Define TorXakis grammar
    grammar TorXakisLanguageDefinition;

    torXakisRoot			:		torXakisDefns EOF ;
    torXakisDefns			:		torXakisDefn
                            |       torXakisDefn torXakisDefns ;
    torXakisDefn			:		typeDefList
                            |		funcDefList
                            |		constDefList
                            |		procDefList
                            |		specDef
                            |		adapDef
                            |		sutDef ;

    typeDefList				:		TYPEDEF typeDefs endDef ;
    typeDefs				:		typeDef
                            |		typeDefs Semicolon typeDef ;
    typeDef					:		Capid IsDef constructors ;
    constructors			:		constructor
                            |		constructor Bar constructors ;
    constructor				:		Capid fieldList ;
    fieldList				:
                            |		field
                            |		OpenBrace CloseBrace
                            |		OpenBrace fields CloseBrace ;
    fields					:		field
                            |		field Comma fields ;
    field					:		neSmallIdList SortOf Capid ;

    funcDefList				:		FUNCDEF funcDefs endDef ;
    funcDefs				:		funcDef
                            |		funcDefs Semicolon funcDef ;
    funcDef					:		Smallid formalVars ofSort IsDef valExpr
                            |		Operator formalVars ofSort IsDef valExpr ;

    constDefList			: 		CONSTDEF constDefs endDef ;
    constDefs				:		constDef
                            |		constDefs Semicolon constDef ;
    constDef				:		Smallid ofSort IsDef valExpr ;

    procDefList				:		PROCDEF procDefs endDef ;
    procDefs				:		procDef
                            |		procDefs Semicolon procDef ;
    procDef					:		Smallid formalChannels formalVars IsDef behaviourExpr
                            |		Smallid formalChannels formalVars EXIT ofSorts IsDef behaviourExpr ;

    specDef					:		SPECDEF Capid IsDef CHAN IN channelDeclList CHAN OUT channelDeclList BEHAVIOUR behaviourExpr endDef ;

    adapDef					:		ADAPDEF	Capid IsDef CHAN IN channelDeclList SUT IN channelDeclList CHAN OUT channelDeclList SUT OUT channelDeclList adapMappings ;
    adapMappings			:
                            |		adapMapping endDef adapMappings ;
    adapMapping				:		MAP IN neOfferList Arrow offer
                            |		MAP OUT offer Arrow neOfferList ;

    sutDef					: 		SUTDEF Capid IsDef SUT IN channelDeclList SUT OUT channelDeclList sutChannels ;
    sutChannels				:
                            |		sutChannel endDef sutChannels ;
    sutChannel				:		SOCK IN Capid HOST string PORT Integer
                            |		SOCK OUT Capid HOST string PORT Integer ;

    ofSort					:		SortOf Capid ;
    ofSorts					:		capIdList
                            |		OpenPar capIdList ClosePar
                            |		sharpCapIdList
                            |		OpenPar sharpCapIdList ClosePar ;

    formalChannels			:
                            |		OpenList channelDeclList CloseList ;
    channelDeclList			:
                            |		channelDecls
                            |		channelDecls Semicolon channelDeclList ;
    channelDecls			: 		neCapIdList
                            |		neCapIdList SortOf ofSorts ;

    formalVars				:
                            |		OpenPar ClosePar
                            |		OpenPar varDeclList ClosePar ;
    varDeclList				:		varDecls
                            |		varDecls Semicolon	varDeclList ;
    varDecls				:		neSmallIdList ofSort ;

    behaviourExpr			:		behaviourExpr1;
    behaviourExpr1			:		behaviourExpr1 Enable behaviourExpr2
                            |		behaviourExpr1 Enable ACCEPT channelOffList IN behaviourExpr2
                            |		behaviourExpr1 Disable behaviourExpr2
                            |		behaviourExpr1 Interrupt behaviourExpr2
                            |		behaviourExpr2;
    behaviourExpr2			:		behaviourExpr2 Synchronization behaviourExpr3
                            |		behaviourExpr2 Interleaving behaviourExpr3
                            |		behaviourExpr2 OpenCommunicate capIdList CloseCommunicate behaviourExpr3
                            | 		behaviourExpr3;
    behaviourExpr3			:		behaviourExpr3 Choice behaviourExpr4
                            |		behaviourExpr3 AltChoice behaviourExpr4
                            |		behaviourExpr4 ;
    behaviourExpr4			:		OpenPred neValExprs ClosePred Guard behaviourExpr4
                            |		prefixOfferList Prefix behaviourExpr4
                            |		prefixOfferList OpenPred neValExprs ClosePred Prefix behaviourExpr4
                            |		prefixOfferList
                            |		prefixOfferList OpenPred neValExprs ClosePred
                            |		STOP
                            |		Smallid actualChannels actualValExprs
                            |		LET neValueDefList IN behaviourExpr1 endIn
                            |		HIDE formalChannels IN behaviourExpr1 endIn
                            |		BEGIN behaviourExpr1 END
                            |		OpenPar behaviourExpr1 ClosePar ;

    actualValExprs			:
                            |		OpenPar valExprs ClosePar ;

    prefixOfferList			:		ISTEP
                            |		neOfferList
                            |		Bar neOfferList Bar
                            |		OpenBrace offerList CloseBrace ;
    offerList				:
                            |		neOfferList ;
    neOfferList				:		offer
                            |		neOfferList Bar offer ;
    offer					:		EXIT channelOffList
                            |		Capid channelOffList ;
    channelOffList			:
                            |		channelOffer channelOffList;
    channelOffer			:		Question varDecls
                            |		Question neSmallIdList
                            |		Exclam valExpr;

    actualChannels			:
                            |		OpenList capIdList CloseList ;

    endDef					:
                            |		Semicolon
                            |		ENDDEF
                            |		END ;
    endIn					:		NI
                            |		END ;
    endIf					:		FI
                            |		END ;

    valExpr					:		valExpr1 ;
    valExpr1				:		LET neValueDefList IN valExpr1 endIn
                            |		IF neValExprs THEN valExpr1 ELSE valExpr1 endIf
                            |		valExpr1 Operator valExpr2
                            |		valExpr2 ofSort
                            |		valExpr2 ;
    valExpr2				:		Smallid
                            |		Smallid OpenPar valExprs ClosePar
                            |		Operator valExpr2
                            |		Capid
                            |		Capid OpenPar valExprs ClosePar
                            |		constant
                            |		OpenPar valExpr1 ClosePar
                            |		ERROR string
                            |		ERROR OpenPar string ClosePar ;
    valExprs				:
                            |		neValExprs ;
    neValExprs				:		valExpr1
                            |		valExpr1 Comma neValExprs ;

    valueDefList			:
                            |		neValueDefList ;
    neValueDefList			:		neValueDefs
                            |		neValueDefs Semicolon neValueDefList ;
    neValueDefs				:		valueDef
                            |		valueDef Comma neValueDefs ;

    valueDef				:		Smallid ofSort Equal valExpr
                            |		Smallid Equal valExpr ;
    constant				:		Integer
                            |		character
                            |		string ;
    capIdList				:
                            |		neCapIdList;
    neCapIdList				:		Capid
                            |		neCapIdList Comma Capid ;
    sharpCapIdList			:		sharpCapIdList1 Sharp Capid ;
    sharpCapIdList1			:		Capid
                            |		sharpCapIdList1 Sharp Capid ;
    neSmallIdList			:		Smallid
                            |		neSmallIdList Comma Smallid ;

    string					:		DoubleQuote ( ~DoubleQuote | BackSlash DoubleQuote )* DoubleQuote ;
    character				:		Quote ( ~Quote | BackSlash Quote ) Quote ;

    TYPEDEF					:		'TYPEDEF' ;
    FUNCDEF					:		'FUNCDEF' ;
    CONSTDEF				:		'CONSTDEF' ;
    PROCDEF					:		'PROCDEF' ;
    SPECDEF					:		'SPECDEF' ;
    ADAPDEF					:		'ADAPDEF' ;
    SUTDEF					:		'SUTDEF' ;
    ENDDEF					:		'ENDDEF' ;
    SUT						:		'SUT' ;
    CHAN					:		'CHAN' ;
    MAP						:		'MAP' ;
    SOCK					:		'SOCK' ;
    IN						:		'IN' ;
    OUT						:		'OUT' ;
    HOST					:		'HOST' ;
    PORT					:		'PORT' ;
    BEHAVIOUR				:		'BEHAVIOUR' ;
    STOP					:		'STOP' ;
    EXIT					:		'EXIT' ;
    ACCEPT					:		'ACCEPT' ;
    HIDE					:		'HIDE' ;
    LET						:		'LET' ;
    NI						:		'NI' ;
    BEGIN					:		'BEGIN' ;
    END						:		'END' ;
    IF						:		'IF' ;
    THEN					:		'THEN' ;
    ELSE					:		'ELSE' ;
    FI						:		'FI' ;
    ISTEP					:		'ISTEP' ;
    ERROR					:		'ERROR' ;

    Arrow					:		'->' ;
    Choice					:		'[]' ;
    AltChoice				:		'##' ;
    Prefix					:		'>->' ;
    Enable					:		'>>>' ;
    Disable					:		'[>>' ;
    Interrupt				:		'[><' ;
    SortOf					:		'::' ;
    IsDef					:		'::=' ;
    Guard					:		'=>>' ;
    Synchronization			:		'||' ;
    Interleaving			:		'|||' ;
    OpenCommunicate			:		'|[' ;
    CloseCommunicate		:		']|' ;
    OpenPred				:		'[[' ;
    ClosePred				:		']]' ;

    OpenList				:		'[' ;
    CloseList				:		']' ;
    OpenBrace				:		'{' ;
    CloseBrace				:		'}' ;
    OpenPar					:		'(' ;
    ClosePar				:		')' ;
    Question				:		'?' ;
    Exclam					:		'!' ;
    Sharp					:		'#' ;
    Semicolon				:		';' ;
    Comma					:		',' ;
    Quote					:		'\'' ;
    DoubleQuote				:		'"' ;
    Underscore				:		'_' ;

    Equal					:		'=' ;
    Bar						:		'|' ;
    Operator				:		( Equal | Plus | Minus | Star | Power |	Slash |	BackSlash | LessThen | GreaterThen | Bar | AtSign |	Ampersand |	Percent )+;
    Plus					:		'+' ;
    Minus					:		'-' ;
    Star					:		'*' ;
    Power					:		'^' ;
    Slash					:		'/' ;
    BackSlash				:		'\\' ;
    LessThen				:		'<' ;
    GreaterThen				:		'>' ;
    AtSign					:		'@' ;
    Ampersand				:		'&' ;
    Percent					:		'%' ;

    Capid					:		AlphaCap ( Alpha | Digit | Underscore )* ;
    Smallid					:		AlphaSmall ( Alpha | Digit | Underscore )* ;
    Integer					:		Digit+ ;
    AlphaCap				:		[A-Z] ;
    AlphaSmall				:		[a-z] ;
    Alpha					:		AlphaCap
                            |		AlphaSmall ;
    Digit					:		[0-9] ;

    Comment					:		'--' (~[\r\n])* -> skip;
    NonWS					:		~[ \r\t\n\u000C] ;
    WS						:		[ \r\t\n\u000C]+ -> skip ;