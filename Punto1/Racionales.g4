grammar Laplace;

start : expr EOF ;

expr : LBRACE function RBRACE ;

function : laplaceTransform ;

laplaceTransform
    : 'e^(-' INT '*t)'                                # expFunction
    | 'u(t)'                                           # unitStepFunction
    | 'u(t-' INT ')'                                   # delayedUnitStepFunction
    | 'δ(t)'                                           # deltaFunction
    | 'δ(t-' INT ')'                                   # delayedDeltaFunction
    | 't^' INT                                         # powFunction
    | 't^' SYMBOL                                      # qPowFunction
    | 'sin(' SYMBOL '*t)'                              # sineFunction
    | 'cos(' SYMBOL '*t)'                              # cosineFunction
    | 'sinh(' INT '*t)'                                # sinhFunction
    | 'cosh(' INT '*t)'                                # coshFunction
    | 'log(t/t0)'                                      # logFunction
    | 'Jn(' SYMBOL '*t)'                               # besselFunction
    | 'I(' INT '*t)'                                   # modifiedBesselFunction
    ;

LBRACE : 'L(' ;
RBRACE : ')' ;
INT : [0-9]+ ;
SYMBOL : [a-zA-Z]+ ;  // Acepta letras como t, w, n, etc.
WS : [ \t\r\n]+ -> skip ;


