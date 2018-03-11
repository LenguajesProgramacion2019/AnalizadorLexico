import re

global lexeme
global line
row = 1
back = [0, 0]

reserved_words = [
    'log',
    'true',
    'false',
    'importar',
    'math',
    'sqrt',
    'fabs',
    'pow',
    'cos',
    'sin',
    'pi',
    'e',
    'for',
    'funcion',
    'retorno',
    'end',
    'if',
    'while'
]

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '{', '}', '#', '[', ']', '(', ')', '<', '>', '=', '.',
            '!', '&', '|', '+', '-', '*', '/', '%', '^', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '"']

def delta(column, char, state):
    global lexeme
    global line
    if state == 0:
        if char not in alphabet:
            print("Error lexico(linea:" + str(row) + ",posicion:" + str(column) + ")")
            exit(0)
        #cadenas no especificas => string
        elif char == '"':
            lexeme = ""
            return [8, 0]
        # operadores especiales
        elif char == '{':
            print("<token_llave_izq,"+str(row)+","+str(column)+">")
            return [0, 0]
        elif char == '}':
            print("<token_llave_der," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == '#':
            #print("<token_com," + str(row) + "," + str(column) + ">")
            line = ""
            return [0, 0]
        elif char == '[':
            print("<token_cor_izq," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == ']':
            print("<token_cor_der," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == '(':
            print("<token_par_izq," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == ')':
            print("<token_par_der," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == '.':
            #lexeme = char
            #return [11, 0]
            print("<token_point," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == '+':
            print("<token_mas," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == '-':
            print("<token_menos," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == '*':
            print("<token_mul," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == '/':
            print("<token_div," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == '%':
            print("<token_mod," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == '^':
            print("<token_pot," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == '>':
            return [1, 0]
        elif char == '<':
            return [2, 0]
        elif char == '=':
            return [3, 0]
        elif char == '!':
            return [4, 0]
        elif char == '&':
            return [5, 0]
        elif char == '|':
            return [6, 0]
        elif char == 'i':
            return [7, 0]
        #cadenas no especificas => id
        #palabras reservadas
        elif re.match(r'[a-z]', char) or re.match(r'[A-Z]', char):
            lexeme = char
            return [9, 0]
        #cadenas no especificas => int, float
        elif re.match(r'[0-9]', char):
            lexeme = char
            return [10, 0]
        else:
            return [0, 0]

    if state == 1:
        if char == '=':
            print("<token_mayor_igual," + str(row) + "," + str(column-1) + ">")
            return [0, 0]
        else:
            print("<token_mayor," + str(row) + "," + str(column-1) + ">")
            state = 0
            return [0, 1]

    if state == 2:
        if char == '=':
            print("<token_menor_igual," + str(row) + "," + str(column - 1) + ">")
            return [0,0]
        else:
            print("<token_menor," + str(row) + "," + str(column - 1) + ">")
            return [0,1]

    if state == 3:
        if char == '=':
            print("<token_igual_num," + str(row) + "," + str(column - 1) + ">")
            return [0, 0]
        else:
            print("<token_assign," + str(row) + "," + str(column - 1) + ">")
            return [0, 1]

    if state == 4:
        if char == '=':
            print("<token_diff_num," + str(row) + "," + str(column - 1) + ">")
            return [0, 0]
        else:
            print("<token_not," + str(row) + "," + str(column - 1) + ">")
            return [0, 1]

    if state == 5:
        if char == '&':
            print("<token_and," + str(row) + "," + str(column - 1) + ">")
            return [0, 0]
        else:
            print("Error lexico(linea:" + str(row) + ",posicion:" + str(column - 1) + ")")
            exit(0)

    if state == 6:
        if char == '|':
            print("<token_or," + str(row) + "," + str(column - 1) + ">")
            return [0, 0]
        else:
            print("Error lexico(linea:" + str(row) + ",posicion:" + str(column - 1) + ")")
            exit(0)

    if state == 7:
        if char == 'n':
            print("<token_in," + str(row) + "," + str(column - 1) + ">")
            return [0, 0]
        else:
            lexeme = 'i'
            return [9, 1]

    if state == 8:
        if char == '"':
            print("<token_string," + lexeme + "," + str(row) + "," + str(column-len(lexeme)-1) + ">")
            return[0, 0]
        else:
            lexeme = lexeme + char
            return [8, 0]

    if state == 9:
        if re.match(r'[a-z]', char) or re.match(r'[A-Z]', char) or re.match(r'[0-9]', char):
            lexeme = lexeme + str(char)
            return[9, 0]
        else:
            if lexeme in reserved_words:
                print("<"+lexeme + "," + str(row) + "," + str(column - len(lexeme)) + ">")
            else:
                print("<id," + lexeme + "," + str(row) + "," + str(column - len(lexeme)) + ">")
            return [0, 1]

    if state == 10:
        if re.match(r'[0-9]', char):
            lexeme = lexeme + char
            return [10, 0]
        elif char == '.':
            lexeme = lexeme + char
            return [11, 0]
        else:
            print("<token_integer," + lexeme + "," + str(row) + "," + str(column - len(lexeme)) + ">")
            return [0, 1]

    if state == 11:
        if re.match(r'[0-9]', char):
            lexeme = lexeme + char
            return[12, 0]
        else:
            #if lexeme == '.':
            #    print("<token_point," + str(row) + "," + str(column-1) + ">")
            #else:
            #    print("<token_integer," + lexeme[0:len(lexeme) - 1] + "," + str(row) + "," + str(column - len(lexeme)) + ">")
            #    print("<token_point," + str(row) + "," + str(column-1) + ">")
            #return[0, 1]
            print("<token_integer," + lexeme[0:len(lexeme) - 1] + "," + str(row) + "," + str(column - len(lexeme)) + ">")
            return [0, 2]

    if state == 12:
        if re.match(r'[0-9]', char):
            lexeme = lexeme + char
            return[12, 0]
        else:
            print("<token_float," + lexeme + "," + str(row) + "," + str(column - len(lexeme)) + ">")
            return [0, 1]


line = input()
print()
while True:
    i = 0
    line = line+" "

    while i < len(line):
        back = delta(i+1, line[i], back[0])
        i = i + 1 - back[1]
        #print(back[0], back[1])
    if back[0] == 8:
        print("Error lexico(linea:" + str(row) + ",posicion:" + str(i - len(lexeme)) + ")")
        exit(0)

    line = input()
    row += 1

    """
    if(back[0] == 9):
        if (lexeme in reserved_words):
            print("<"+lexeme + "," + str(row) + "," + str(i - len(lexeme) + 1) + ">")
        else:
            print("<id," + lexeme + "," + str(row) + "," + str(i - len(lexeme) + 1) + ">")
        back[0] = 0
    if back[0] == 10:
        print("<token_integer," + lexeme + "," + str(row) + "," + str(i - len(lexeme) + 1) + ">")
        back[0] = 0
    if (back[0] == 11):
        print("<token_float," + lexeme[0:len(lexeme)-1] + "," + str(row) + "," + str(i - len(lexeme) + 1) + ">")
        print("<token_point," + str(row) + "," + str(i) + ">")
        back[0] = 0
    if (back[0] == 12):
        print("<token_float," + lexeme + "," + str(row) + "," + str(i - len(lexeme) + 1) + ">")
        back[0] = 0
    """