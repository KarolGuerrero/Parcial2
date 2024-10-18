grammar Colecciones;

program
    : statement* EOF
    ;

statement
    : mapFunction ';'
    | filterFunction ';'
    ;

mapFunction
    : 'MAP' '(' functionCall ',' iterableObject ')'
    ;

filterFunction
    : 'FILTER' '(' functionCall ',' iterableObject (',' INT)? ')'
    ;

functionCall
    : ID
    ;

iterableObject
    : list
    | tuple
    ;

list
    : '[' expressionList ']'
    ;

tuple
    : '(' expressionList ')'
    ;

expressionList
    : '"'? expression '"'? (',' '"'? expression '"'? )*
    ;

expression
    : INT
    | ID
    ;

ID      : [a-zA-Z_][a-zA-Z0-9_]*;
INT     : [0-9]+;
WS      : [ \t\r\n]+ -> skip; // Espacios en blanco se ignoran
