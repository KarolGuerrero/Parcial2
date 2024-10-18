grammar Racionales;

prog:   expr EOF ;

expr:   expr '+' term      # AddSub
    |   expr '-' term      # AddSub
    |   term               # SingleTerm
    ;

term:   factor '*' factor    # MulDiv
    |   factor '/' factor    # MulDiv
    |   factor             # SingleFactor
    ;

factor: '(' expr ')'       # ParensExpr
    |   fraccion           # FractionFactor
    |   '-' fraccion       # NegativeFraction
    ;

fraccion: INT '/' INT      # FractionExpr
    
    ;

INT: [0-9]+ ;
WS: [ \t\n\r]+ -> skip ;

