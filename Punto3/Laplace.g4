grammar Laplace;

start : expr EOF ;

expr
    : LAPLACE '(' function ')'        # laplaceTransform
    | function                        # baseFunction
    ;

function
    : expFunction                     // Función exponencial
    | unitStepFunction                // Escalón unitario
    | delayedUnitStepFunction         // Escalón unitario con retardo
    | deltaFunction                   // Delta de Dirac
    | delayedDeltaFunction            // Delta de Dirac con retardo
    | powFunction                     // Potencia t^n
    | qPowFunction                    // Potencia generalizada t^q
    | sineFunction                    // Seno
    | cosineFunction                  // Coseno
    | sinhFunction                    // Seno hiperbólico
    | coshFunction                    // Coseno hiperbólico
    | logFunction                     // Logaritmo natural
    | besselFunction                  // Función de Bessel
    | modifiedBesselFunction          // Función de Bessel modificada
    ;


expFunction
    : 'e' '^' '(' '-' param '*' 't' ')' 
    ;

unitStepFunction
    : 'u' '(' 't' ')'                   
    ;

delayedUnitStepFunction
    : 'u' '(' 't' '-' param ')' 
    ;

deltaFunction
    : 'δ' '(' 't' ')'                   
    ;

delayedDeltaFunction
    : 'δ' '(' 't' '-' param ')'           
    ;

powFunction
    : 't' '^' INT                         
    ;

qPowFunction
    : 't' '^' param                      
    ;

sineFunction
    : 'sin' '(' param '*' 't' ')'       
    ;

cosineFunction
    : 'cos' '(' param '*' 't' ')'         
    ;

sinhFunction
    : 'sinh' '(' param '*' 't' ')'       
    ;

coshFunction
    : 'cosh' '(' param '*' 't' ')'        
    ;

logFunction
    : 'log' '(' 't' '/' param ')'        
    ;

besselFunction
    : 'Jn' '(' param '*' 't' ')'         
    ;

modifiedBesselFunction
    : 'I' param '(' param '*' 't' ')'    
    ;

param : INT | FLOAT ;

LAPLACE: 'L' ; // La transformada de Laplace
INT: [0-9]+ ;  // Enteros
FLOAT: [0-9]+ '.' [0-9]+ ; // Flotantes

WS: [ \t\r\n]+ -> skip ; // Espacios en blanco
