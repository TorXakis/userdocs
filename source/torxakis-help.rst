
Torxakis help
=============

The output of the ``help`` command in the ``TorXakis`` command line interface:

::

    $ torxakis
    TXS >>  TorXakis :: Model-Based Testing

    TXS >>  txsserver starting: "localhost" : 63980
    TXS >>  Solver "z3" initialized : Z3 [4.8.10]
    TXS >>  TxsCore initialized
    TXS >>  LPEOps version 2019.07.05.02
    TXS >>  input files parsed:
    TXS >>  []
    TXS >> help
    TXS >>
    --------------------------------
    TorXakis :: Model-Based Testing
    --------------------------------

    quit, q                               : stop TorXakis completely
    exit, x                               : exit the current command run of TorXakis
    help, h, ?                            : show help
    info, i                               : show info on TorXakis
    param [<parameter>]                   : show value of <parameter>/[all parameters]
    param <parameter> <value>             : set <parameter> to <value>
    echo <text>                           : echo <text>
    # <text>                              : comment       : <text> is ignored
    seed <n>                              : set random seed to <n>

    --------------------------------

    delay <n>                             : delay TorXakis for <n> seconds
    time                                  : give the current time
    timer <name>                          : set or read timer <name>
    run <file>                            : run the torxakis script from <file>

    --------------------------------

    var <variable-declarations>           : declare variables
    val <value-definitions>               : define values
    eval <value-expression>               : evaluate the (closed) <value-expression>
    solve <value-expression>              : solve the (open, boolean) <value-expression>
    unisolve <value-expression>           : solve (uniquely) the (open, boolean) <value-expression>
                                            'unsat': 0, 'sat': 1, 'unknown': >1 or unknown solution

    --------------------------------

    tester <mod> [<purp>] [<map>] <cnect> : start testing with model <mod> and connection <cnect>
                                            using possible test purpose <purp> and/or mapper <map>
    simulator <mod> <cnect>               : start simulating with model <mod> and connection <cnect>
    stepper <mod>                         : start stepping with model <mod>
    stop                                  : stop testing, simulation, or stepping

    --------------------------------

    test <action>                         : make a test step identified by (visible) input <action>
    test                                  : make a test step by observing output/quiescence
    test <n>                              : make <n> random test steps
    sim [<n>]                             : make <n>/[unbounded] random simulation steps
    step <action>                         : make a step identified by <action>
    step [<n>]                            : make <n>/[one] random steps

    --------------------------------

    show <object>                         : show <object>       :
                                            tdefs, state, model, purp, mapper, cnect, var, or val
    state                                 : show current state number
    btree [<state>]                       : show <state>/[current] behaviour tree
    goto [<state>]                        : goto <state>/[current] state number in the model
    back [<n>]                            : go back <n>/[one] visible steps in the model state
    path                                  : show the visible path from the initial state
    trace [proc|purp]                     : show the current trace [in PROCDEF|PURPDEF] format]
    menu [in|out|purp] [<state>]          : give the [in|out] menu of actions of [current] <state>

    --------------------------------
    ncomp                                 : test purpose generation via `N-Complete'-algorithm
    lpe                                   : lpe transformation (Linear Process Equation)
    lpeop <op> <lpe> <out>                : apply lpe operation <op> to model <lpe> and produce output named <out>
                                               stop       -> do nothing
                                               show       -> print the lpe to console
                                               export     -> generate torxakis file (do not change identifiers)
                                               export*    -> generate compilable torxakis file
                                               mcrl2      -> translate to mCRL2 specification file
                                               clean      -> remove duplicate/unreachable summands
                                               cstelm     -> remove parameters that never change value
                                               parelm     -> remove behavior-independent parameters
                                               istepelm   -> remove ISTEP actions (preserve weak bisimulation)
                                               datareset  -> reset parameters based on control flow graphs
                                               parreset   -> reset parameters based on summand reachability
                                               isdet      -> determine if the lpe is deterministic
                                               det        -> make the lpe deterministic
                                               uguard     -> add guards for underspecified summands
                                               angelic    -> make the lpe input-enabled (angelic completion)
                                               A->B       -> do two lpe operations in succession
                                               loop       -> repeat lpe operations until a fixpoint is reached
                                               loop*x     -> loop lpe operations x times or until a fixpoint is reached
     merge <mod1> <mod2> <out>            : put two models in parallel and save it as a new model
    --------------------------------
    systart <name> <command>              : start external system <command> with internal <name>
    systop  <name>                        : stop external command with internal <name>
    <command> '$<' <file>                 : read command arguments from <file>
    <command> args '$>' <file>            : write standard output of <command> to <file>
    <command> args '$>>' <file>           : append standard output of <command> to <file>

    --------------------------------

