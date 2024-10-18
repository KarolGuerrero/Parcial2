grammar Laplace;

// Reglas para la entrada de funciones
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

// Función exponencial: e^(-a*t)
expFunction
    : 'e' '^' '(' '-' param '*' 't' ')'   // Decaimiento exponencial
    ;

// Función escalón unitario u(t)
unitStepFunction
    : 'u' '(' 't' ')'                     // Escalón unitario
    ;

// Función escalón unitario con retardo u(t - r)
delayedUnitStepFunction
    : 'u' '(' 't' '-' param ')'           // Escalón unitario con retardo
    ;

// Función delta de Dirac δ(t)
deltaFunction
    : 'δ' '(' 't' ')'                     // Delta de Dirac
    ;

// Función delta de Dirac con retardo δ(t - r)
delayedDeltaFunction
    : 'δ' '(' 't' '-' param ')'           // Delta de Dirac con retardo
    ;

// Potencia t^n
powFunction
    : 't' '^' INT                         // Potencia t^n
    ;

// Potencia generalizada t^q
qPowFunction
    : 't' '^' param                       // Potencia generalizada t^q
    ;

// Función seno sin(ωt)
sineFunction
    : 'sin' '(' param '*' 't' ')'         // Seno
    ;

// Función coseno cos(ωt)
cosineFunction
    : 'cos' '(' param '*' 't' ')'         // Coseno
    ;

// Función seno hiperbólico sinh(at)
sinhFunction
    : 'sinh' '(' param '*' 't' ')'        // Seno hiperbólico
    ;

// Función coseno hiperbólico cosh(at)
coshFunction
    : 'cosh' '(' param '*' 't' ')'        // Coseno hiperbólico
    ;

// Función logarítmica log(t/t0)
logFunction
    : 'log' '(' 't' '/' param ')'         // Logaritmo natural
    ;

// Función de Bessel Jn(ωt)
besselFunction
    : 'Jn' '(' param '*' 't' ')'          // Función de Bessel
    ;

// Función de Bessel modificada
modifiedBesselFunction
    : 'I' param '(' param '*' 't' ')'     // Función de Bessel modificada
    ;

// Parámetros para las funciones (números y constantes)
param : INT | FLOAT ;

LAPLACE: 'L' ; // La transformada de Laplace
INT: [0-9]+ ;  // Enteros
FLOAT: [0-9]+ '.' [0-9]+ ; // Flotantes

WS: [ \t\r\n]+ -> skip ; // Espacios en blanco
