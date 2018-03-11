# AnalizadorLexico

Este programa toma un código fuente escrito en el lenguaje TL y realizar un análisis léxico sobre dicho código. La entrada para juzgar el analizador léxico está dada por un archivo que contiene código fuente escrito en TL.

La salida consiste en una lista de tokens separados por saltos de línea, los cuales siguen el siguiente formato <tipo_de_token,lexema,fila,columna> . En el caso de las palabras reservadas, el token y el lexema son iguales. Entonces se imprime el siguiente formato <tipo_de_token,fila,columna> y para operadores especiales se imprime <nombre_token,fila,columna>.

Para cadenas no especificas se imprime:
<token_string,lexema,fila,columna>
<token_integer,lexema,fila,columna>
<token_float,lexema,fila,columna>
<id,lexema,fila,columna>
