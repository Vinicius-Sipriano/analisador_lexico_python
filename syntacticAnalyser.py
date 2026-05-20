from enum import Enum
from lexicalAnalyser import Tokens

class NTerminals(Enum):
    TK_PROGRAM = 100
    TK_FUNC_LIST = 101
    TK_FUNC_LIST_P = 102
    TK_FUNCTION = 103
    TK_PARAM_OPT = 104
    TK_PARAM_LIST = 105
    TK_PARAM_LIST_P = 106
    TK_PARAM = 107
    TK_BLOCK = 108
    TK_DECL_OPT = 109
    TK_DECL_LIST = 110
    TK_DECL_LIST_P = 111
    TK_VAR_DECL = 112
    TK_STMT_OPT = 113
    TK_STMT_LIST = 114
    TK_STMT_LIST_P = 115
    TK_STMT = 116
    TK_ASSIGN_STMT = 117
    TK_IF_STMT = 118
    TK_WHILE_STMT = 119
    TK_PRINT_STMT = 120
    TK_RETURN_STMT = 121
    TK_ELSE_PART = 122
    TK_EXPR = 123
    TK_REL_EXPR = 124
    TK_REL_EXPR_P = 125
    TK_REL_OP = 126
    TK_ADD_EXPR = 127
    TK_ADD_EXPR_P = 128
    TK_MUL_EXPR = 129
    TK_MUL_EXPR_P = 130
    TK_FACTOR = 131
    TK_FACTOR_TAIL = 132
    TK_ARG_OPT = 133
    TK_ARG_LIST = 134
    TK_ARG_LIST_P = 135
    TK_TYPE = 136
    TK_EPSILON = -1
    TK_EOF = 0

PRODUCTIONS = [
    [ NTerminals.TK_FUNC_LIST ],                                                                                                        
    [ NTerminals.TK_FUNCTION, NTerminals.TK_FUNC_LIST_P ],                                                                             
    [ NTerminals.TK_FUNCTION, NTerminals.TK_FUNC_LIST_P ],                                                                             
    [ NTerminals.TK_EPSILON ],                                                                                                          
    [ NTerminals.TK_TYPE, Tokens.TK_ID.value, Tokens.TK_OPEN_PAREN.value, NTerminals.TK_PARAM_OPT,
        Tokens.TK_CLOSE_PAREN.value, NTerminals.TK_BLOCK ],                                                                            
    [ NTerminals.TK_PARAM_LIST ],                                                                                                       
    [ NTerminals.TK_EPSILON ],
    [ NTerminals.TK_PARAM, NTerminals.TK_PARAM_LIST_P ]
    [ Tokens.TK_COMMA.value, NTerminals.TK_PARAM, NTerminals.TK_PARAM_LIST_P ],                                                        
    [ NTerminals.TK_EPSILON ],                                                                                                          
    [ NTerminals.TK_TYPE, Tokens.TK_ID.value ],                                                                                           
    [ Tokens.TK_OPEN_BRACE.value, NTerminals.TK_DECL_OPT, NTerminals.TK_STMT_OPT,
        Tokens.TK_CLOSE_BRACE.value ],                                                                                                  
    [ NTerminals.TK_DECL_LIST ],                                                                                                        
    [ NTerminals.TK_EPSILON ],                                                                                                          
    [ NTerminals.TK_VAR_DECL, NTerminals.TK_DECL_LIST_P ],                                                                             
    [ NTerminals.TK_VAR_DECL, NTerminals.TK_DECL_LIST_P ],                                                                             
    [ NTerminals.TK_EPSILON ],                                                                                                          
    [ NTerminals.TK_TYPE, Tokens.TK_ID.value, Tokens.TK_SEMICOLON.value ],                                                             
    [ NTerminals.TK_STMT_LIST ],                                                                                                        
    [ NTerminals.TK_EPSILON ],                                                                                                          
    [ NTerminals.TK_STMT, NTerminals.TK_STMT_LIST_P ],                                                                                 
    [ NTerminals.TK_STMT, NTerminals.TK_STMT_LIST_P ],                                                                                 
    [ NTerminals.TK_EPSILON ],                                                                                                          
    [ NTerminals.TK_ASSIGN_STMT ],                                                                                                      
    [ NTerminals.TK_IF_STMT ],                                                                                                          
    [ NTerminals.TK_WHILE_STMT ],                                                                                                       
    [ NTerminals.TK_PRINT_STMT ],                                                                                                       
    [ NTerminals.TK_RETURN_STMT ],                                                                                                      
    [ NTerminals.TK_BLOCK ],                                                                                                            
    [ Tokens.TK_ID.value, Tokens.TK_ATRIB.value, NTerminals.TK_EXPR, Tokens.TK_SEMICOLON.value ],                                      
    [ Tokens.TK_RETURN.value, NTerminals.TK_EXPR, Tokens.TK_SEMICOLON.value ],                                                         
    [ Tokens.TK_PRINT.value, Tokens.TK_OPEN_PAREN.value, NTerminals.TK_EXPR,
        Tokens.TK_CLOSE_PAREN.value, Tokens.TK_SEMICOLON.value ],                                                                      
    [ Tokens.TK_IF.value, Tokens.TK_OPEN_PAREN.value, NTerminals.TK_EXPR,
        Tokens.TK_CLOSE_PAREN.value, NTerminals.TK_STMT, NTerminals.TK_ELSE_PART ],                                                    
    [ Tokens.TK_ELSE.value, NTerminals.TK_STMT ],                                                                                      
    [ NTerminals.TK_EPSILON ],                                                                                                          
    [ Tokens.TK_WHILE.value, Tokens.TK_OPEN_PAREN.value, NTerminals.TK_EXPR,
        Tokens.TK_CLOSE_PAREN.value, NTerminals.TK_STMT ],                                                                             
    [ NTerminals.TK_REL_EXPR ],                                                                                                         
    [ NTerminals.TK_ADD_EXPR, NTerminals.TK_REL_EXPR_P ],                                                                              
    [ NTerminals.TK_REL_OP, NTerminals.TK_ADD_EXPR ],                                                                                  
    [ NTerminals.TK_EPSILON ],                                                                                                          
    [ Tokens.TK_EQUALTY.value ],                                                                                                        
    [ Tokens.TK_INEQUALTY.value ],                                                                                                      
    [ Tokens.TK_LESS.value ],                                                                                                           
    [ Tokens.TK_GREATER.value ],                                                                                                        
    [ Tokens.TK_LESS_OR_EQUAL.value ],                                                                                                  
    [ Tokens.TK_GREATER_OR_EQUAL.value ],                                                                                               
    [ NTerminals.TK_MUL_EXPR, NTerminals.TK_ADD_EXPR_P ],                                                                              
    [ Tokens.TK_PLUS.value, NTerminals.TK_MUL_EXPR, NTerminals.TK_ADD_EXPR_P ],                                                        
    [ Tokens.TK_MINUS.value, NTerminals.TK_MUL_EXPR, NTerminals.TK_ADD_EXPR_P ],                                                       
    [ NTerminals.TK_EPSILON ],                                                                                                          
    [ NTerminals.TK_FACTOR, NTerminals.TK_MUL_EXPR_P ],                                                                                
    [ Tokens.TK_MULTIPLY.value, NTerminals.TK_FACTOR, NTerminals.TK_MUL_EXPR_P ],                                                      
    [ Tokens.TK_DIVIDE.value, NTerminals.TK_FACTOR, NTerminals.TK_MUL_EXPR_P ],                                                        
    [ NTerminals.TK_EPSILON ],                                                                                                          
    [ Tokens.TK_OPEN_PAREN.value, NTerminals.TK_EXPR, Tokens.TK_CLOSE_PAREN.value ],                                                   
    [ Tokens.TK_ID.value, NTerminals.TK_FACTOR_TAIL ],                                                                                  
    [ Tokens.TK_NUM.value ],                                                                                                             
    [ Tokens.TK_OPEN_PAREN.value, NTerminals.TK_ARG_OPT, Tokens.TK_CLOSE_PAREN.value ],                                              
    [ NTerminals.TK_EPSILON ],                                                                                                          
    [ NTerminals.TK_ARG_LIST ],                                                                                                         
    [ NTerminals.TK_EPSILON ],                                                                                                          
    [ NTerminals.TK_EXPR, NTerminals.TK_ARG_LIST_P ],                                                                                  
    [ Tokens.TK_COMMA.value, NTerminals.TK_EXPR, NTerminals.TK_ARG_LIST_P ],                                                           
    [ NTerminals.TK_EPSILON ],                                                                                                          
    [ Tokens.TK_INT.value ],                                                                                                             
    [ Tokens.TK_FLOAT.value ],                                                                                                           
]

def lookup(X, a):
    return matrizParser[X - FIRST_NT][a - 1]

def get_prod(p):
    return [t for t in matrizProd[p - 1] if t != 0]

def parse(sentence):
    tokens = [TOKEN[ch] for ch in sentence] + [EOF]
    pilha  = [EOF, TOKEN['S']]

    for a in tokens:
        while True:
            X = pilha[-1]

            if X == EPS:
                pilha.pop()
                continue

            if X == EOF:
                print("Sentença ACEITA!")
                return True

            if X >= FIRST_NT:
                p = lookup(X, a)
                if p == 0:
                    print("Erro sintático.")
                    return False
                pilha.pop()
                for sym in reversed(get_prod(p)):
                    pilha.append(sym)
            else:
                if X == a:
                    pilha.pop()
                    break
                else:
                    print(f"Erro: '{TOKEN_NAME[X]}' ≠ '{TOKEN_NAME[a]}'")
                    return False

    print("Sentença ACEITA!")
    return True