grammar Laplace;

// Reglas sintácticas
laplaceTransform: 'L' '{' expression '}' '->' 'X' '(' VARIABLE ')';

expression: function | term (('+' | '-') term)*;

term: factor (('*' | '/') factor)*;

factor: FUNCTION '(' expression ')'
      | VARIABLE
      | NUMBER
      | '-' factor
      | '(' expression ')';

// Funciones específicas de la transformada de Laplace
function: 'integrate' '(' expression ')' 'dt' 'from' '0' 'to' 'infinity'
        | 'e' '^' '(' '-' VARIABLE '*' VARIABLE ')'
        | 'u' '(' VARIABLE ')'
        | 'cos' '(' VARIABLE ')'
        | 'cosh' '(' VARIABLE ')'
        | 'log' '(' expression ')'
        | 'Gamma' '(' VARIABLE ')';

// Reglas léxicas
VARIABLE: [a-zA-Z]+;
NUMBER: [0-9]+('.'[0-9]+)?;
FUNCTION: 'integrate' | 'e' | 'u' | 'cos' | 'cosh' | 'log' | 'Gamma';
WS: [ \t\r\n]+ -> skip;
