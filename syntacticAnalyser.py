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
    [ NTerminals.TK_FUNC_LIST ],                                                                                                        #1
    [ NTerminals.TK_FUNCTION, NTerminals.TK_FUNC_LIST_P ],                                                                             #2
    [ NTerminals.TK_FUNCTION, NTerminals.TK_FUNC_LIST_P ],                                                                             #3
    [ NTerminals.TK_EPSILON ],                                                                                                          #4
    [ NTerminals.TK_TYPE, Tokens.TK_ID.value, Tokens.TK_OPEN_PAREN.value, NTerminals.TK_PARAM_OPT,
        Tokens.TK_CLOSE_PAREN.value, NTerminals.TK_BLOCK ],                                                                            #5
    [ NTerminals.TK_PARAM_LIST ],                                                                                                       #6
    [ NTerminals.TK_EPSILON ],                                                                                                          #7
    [ Tokens.TK_COMMA.value, NTerminals.TK_PARAM, NTerminals.TK_PARAM_LIST_P ],                                                        #8
    [ NTerminals.TK_EPSILON ],                                                                                                          #9
    [ NTerminals.TK_TYPE, Tokens.TK_ID.value ],                                                                                        #10
    [ Tokens.TK_OPEN_BRACE.value, NTerminals.TK_DECL_OPT, NTerminals.TK_STMT_OPT,
        Tokens.TK_CLOSE_BRACE.value ],                                                                                                  #11
    [ NTerminals.TK_DECL_LIST ],                                                                                                        #12
    [ NTerminals.TK_EPSILON ],                                                                                                          #13
    [ NTerminals.TK_VAR_DECL, NTerminals.TK_DECL_LIST_P ],                                                                             #14
    [ NTerminals.TK_VAR_DECL, NTerminals.TK_DECL_LIST_P ],                                                                             #15
    [ NTerminals.TK_EPSILON ],                                                                                                          #16
    [ NTerminals.TK_TYPE, Tokens.TK_ID.value, Tokens.TK_SEMICOLON.value ],                                                             #17
    [ NTerminals.TK_STMT_LIST ],                                                                                                        #18
    [ NTerminals.TK_EPSILON ],                                                                                                          #19
    [ NTerminals.TK_STMT, NTerminals.TK_STMT_LIST_P ],                                                                                 #20
    [ NTerminals.TK_STMT, NTerminals.TK_STMT_LIST_P ],                                                                                 #21
    [ NTerminals.TK_EPSILON ],                                                                                                          #22
    [ NTerminals.TK_ASSIGN_STMT ],                                                                                                      #23
    [ NTerminals.TK_IF_STMT ],                                                                                                          #24
    [ NTerminals.TK_WHILE_STMT ],                                                                                                       #25
    [ NTerminals.TK_PRINT_STMT ],                                                                                                       #26
    [ NTerminals.TK_RETURN_STMT ],                                                                                                      #27
    [ NTerminals.TK_BLOCK ],                                                                                                            #28
    [ Tokens.TK_ID.value, Tokens.TK_ATRIB.value, NTerminals.TK_EXPR, Tokens.TK_SEMICOLON.value ],                                      #29
    [ Tokens.TK_RETURN.value, NTerminals.TK_EXPR, Tokens.TK_SEMICOLON.value ],                                                         #30
    [ Tokens.TK_PRINT.value, Tokens.TK_OPEN_PAREN.value, NTerminals.TK_EXPR,
        Tokens.TK_CLOSE_PAREN.value, Tokens.TK_SEMICOLON.value ],                                                                      #31
    [ Tokens.TK_IF.value, Tokens.TK_OPEN_PAREN.value, NTerminals.TK_EXPR,
        Tokens.TK_CLOSE_PAREN.value, NTerminals.TK_STMT, NTerminals.TK_ELSE_PART ],                                                    #32
    [ Tokens.TK_ELSE.value, NTerminals.TK_STMT ],                                                                                      #33
    [ NTerminals.TK_EPSILON ],                                                                                                          #34
    [ Tokens.TK_WHILE.value, Tokens.TK_OPEN_PAREN.value, NTerminals.TK_EXPR,
        Tokens.TK_CLOSE_PAREN.value, NTerminals.TK_STMT ],                                                                             #35
    [ NTerminals.TK_REL_EXPR ],                                                                                                         #36
    [ NTerminals.TK_ADD_EXPR, NTerminals.TK_REL_EXPR_P ],                                                                              #37
    [ NTerminals.TK_REL_OP, NTerminals.TK_ADD_EXPR ],                                                                                  #38
    [ NTerminals.TK_EPSILON ],                                                                                                          #39
    [ Tokens.TK_EQUALTY.value ],                                                                                                        #40
    [ Tokens.TK_INEQUALTY.value ],                                                                                                      #41
    [ Tokens.TK_LESS.value ],                                                                                                           #42
    [ Tokens.TK_GREATER.value ],                                                                                                        #43
    [ Tokens.TK_LESS_OR_EQUAL.value ],                                                                                                  #44
    [ Tokens.TK_GREATER_OR_EQUAL.value ],                                                                                               #45
    [ NTerminals.TK_MUL_EXPR, NTerminals.TK_ADD_EXPR_P ],                                                                              #46
    [ Tokens.TK_PLUS.value, NTerminals.TK_MUL_EXPR, NTerminals.TK_ADD_EXPR_P ],                                                        #47
    [ Tokens.TK_MINUS.value, NTerminals.TK_MUL_EXPR, NTerminals.TK_ADD_EXPR_P ],                                                       #48
    [ NTerminals.TK_EPSILON ],                                                                                                          #49
    [ NTerminals.TK_FACTOR, NTerminals.TK_MUL_EXPR_P ],                                                                                #50
    [ Tokens.TK_MULTIPLY.value, NTerminals.TK_FACTOR, NTerminals.TK_MUL_EXPR_P ],                                                      #51
    [ Tokens.TK_DIVIDE.value, NTerminals.TK_FACTOR, NTerminals.TK_MUL_EXPR_P ],                                                        #52
    [ NTerminals.TK_EPSILON ],                                                                                                          #53
    [ Tokens.TK_OPEN_PAREN.value, NTerminals.TK_EXPR, Tokens.TK_CLOSE_PAREN.value ],                                                   #54
    [ Tokens.TK_ID.value, NTerminals.TK_FACTOR_TAIL ],                                                                                  #55
    [ Tokens.TK_NUM.value ],                                                                                                             #56
    [ Tokens.TK_OPEN_PAREN.value, NTerminals.TK_ARG_OPT, Tokens.TK_CLOSE_PAREN.value ],                                               #57
    [ NTerminals.TK_EPSILON ],                                                                                                          #58
    [ NTerminals.TK_ARG_LIST ],                                                                                                         #59
    [ NTerminals.TK_EPSILON ],                                                                                                          #60
    [ NTerminals.TK_EXPR, NTerminals.TK_ARG_LIST_P ],                                                                                  #61
    [ Tokens.TK_COMMA.value, NTerminals.TK_EXPR, NTerminals.TK_ARG_LIST_P ],                                                           #62
    [ NTerminals.TK_EPSILON ],                                                                                                          #63
    [ Tokens.TK_INT.value ],                                                                                                             #64
    [ Tokens.TK_FLOAT.value ],                                                                                                           #65
]