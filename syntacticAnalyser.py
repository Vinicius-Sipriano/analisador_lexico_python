from enum import Enum
from sys import argv

from lexicalAnalyser import LexicalAnalyser, Token, Tokens
from receiveFlags import flags

class NTerminals(Enum):
    TK_PROGRAM = 100
    TK_FUNCTION_LIST = 101
    TK_FUNCTION_LIST_P = 102
    TK_FUNCTION = 103
    TK_PARAM_LIST_OPT = 104
    TK_PARAM_LIST = 105
    TK_PARAM_LIST_P = 106
    TK_PARAM = 107
    TK_BLOCK = 108
    TK_DECL_LIST_OPT = 109
    TK_DECL_LIST = 110
    TK_DECL_LIST_P = 111
    TK_VAR_DECL = 112
    TK_STMT_LIST_OPT = 113
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
    TK_ARG_LIST_OPT = 133
    TK_ARG_LIST = 134
    TK_ARG_LIST_P = 135
    TK_TYPE = 136


EOF = 0
COMMENT_TOKENS = {
    Tokens.TK_COMMENT_LINE.value,
    Tokens.TK_COMMENT_BLOCK.value,
}

TERMINAL_NAMES = {
    EOF: "$",
    Tokens.TK_INT.value: "int",
    Tokens.TK_FLOAT.value: "float",
    Tokens.TK_IF.value: "if",
    Tokens.TK_ELSE.value: "else",
    Tokens.TK_WHILE.value: "while",
    Tokens.TK_RETURN.value: "return",
    Tokens.TK_PRINT.value: "print",
    Tokens.TK_ID.value: "id",
    Tokens.TK_NUM.value: "num",
    Tokens.TK_ATRIB.value: "=",
    Tokens.TK_PLUS.value: "+",
    Tokens.TK_MINUS.value: "-",
    Tokens.TK_MULTIPLY.value: "*",
    Tokens.TK_DIVIDE.value: "/",
    Tokens.TK_EQUALTY.value: "==",
    Tokens.TK_INEQUALTY.value: "!=",
    Tokens.TK_LESS.value: "<",
    Tokens.TK_GREATER.value: ">",
    Tokens.TK_LESS_OR_EQUAL.value: "<=",
    Tokens.TK_GREATER_OR_EQUAL.value: ">=",
    Tokens.TK_OPEN_PAREN.value: "(",
    Tokens.TK_CLOSE_PAREN.value: ")",
    Tokens.TK_OPEN_BRACE.value: "{",
    Tokens.TK_CLOSE_BRACE.value: "}",
    Tokens.TK_COMMA.value: ",",
    Tokens.TK_SEMICOLON.value: ";",
}


PRODUCTIONS = [
    [NTerminals.TK_FUNCTION_LIST],
    [NTerminals.TK_FUNCTION, NTerminals.TK_FUNCTION_LIST_P],
    [NTerminals.TK_FUNCTION, NTerminals.TK_FUNCTION_LIST_P],
    [],
    [NTerminals.TK_TYPE, Tokens.TK_ID.value, Tokens.TK_OPEN_PAREN.value, NTerminals.TK_PARAM_LIST_OPT, Tokens.TK_CLOSE_PAREN.value, NTerminals.TK_BLOCK],
    [NTerminals.TK_PARAM_LIST],
    [],
    [NTerminals.TK_PARAM, NTerminals.TK_PARAM_LIST_P],
    [Tokens.TK_COMMA.value, NTerminals.TK_PARAM, NTerminals.TK_PARAM_LIST_P],
    [],
    [NTerminals.TK_TYPE, Tokens.TK_ID.value],
    [Tokens.TK_OPEN_BRACE.value, NTerminals.TK_DECL_LIST_OPT, NTerminals.TK_STMT_LIST_OPT, Tokens.TK_CLOSE_BRACE.value],
    [NTerminals.TK_DECL_LIST],
    [],
    [NTerminals.TK_VAR_DECL, NTerminals.TK_DECL_LIST_P],
    [NTerminals.TK_VAR_DECL, NTerminals.TK_DECL_LIST_P],
    [],
    [NTerminals.TK_TYPE, Tokens.TK_ID.value, Tokens.TK_SEMICOLON.value],
    [NTerminals.TK_STMT_LIST],
    [],
    [NTerminals.TK_STMT, NTerminals.TK_STMT_LIST_P],
    [NTerminals.TK_STMT, NTerminals.TK_STMT_LIST_P],
    [],
    [NTerminals.TK_ASSIGN_STMT],
    [NTerminals.TK_IF_STMT],
    [NTerminals.TK_WHILE_STMT],
    [NTerminals.TK_PRINT_STMT],
    [NTerminals.TK_RETURN_STMT],
    [NTerminals.TK_BLOCK],
    [Tokens.TK_ID.value, Tokens.TK_ATRIB.value, NTerminals.TK_EXPR, Tokens.TK_SEMICOLON.value],
    [Tokens.TK_RETURN.value, NTerminals.TK_EXPR, Tokens.TK_SEMICOLON.value],
    [Tokens.TK_PRINT.value, Tokens.TK_OPEN_PAREN.value, NTerminals.TK_EXPR, Tokens.TK_CLOSE_PAREN.value, Tokens.TK_SEMICOLON.value],
    [Tokens.TK_IF.value, Tokens.TK_OPEN_PAREN.value, NTerminals.TK_EXPR, Tokens.TK_CLOSE_PAREN.value, NTerminals.TK_STMT, NTerminals.TK_ELSE_PART],
    [Tokens.TK_ELSE.value, NTerminals.TK_STMT],
    [],
    [Tokens.TK_WHILE.value, Tokens.TK_OPEN_PAREN.value, NTerminals.TK_EXPR, Tokens.TK_CLOSE_PAREN.value, NTerminals.TK_STMT],
    [NTerminals.TK_REL_EXPR],
    [NTerminals.TK_ADD_EXPR, NTerminals.TK_REL_EXPR_P],
    [NTerminals.TK_REL_OP, NTerminals.TK_ADD_EXPR],
    [],
    [Tokens.TK_EQUALTY.value],
    [Tokens.TK_INEQUALTY.value],
    [Tokens.TK_LESS.value],
    [Tokens.TK_GREATER.value],
    [Tokens.TK_LESS_OR_EQUAL.value],
    [Tokens.TK_GREATER_OR_EQUAL.value],
    [NTerminals.TK_MUL_EXPR, NTerminals.TK_ADD_EXPR_P],
    [Tokens.TK_PLUS.value, NTerminals.TK_MUL_EXPR, NTerminals.TK_ADD_EXPR_P],
    [Tokens.TK_MINUS.value, NTerminals.TK_MUL_EXPR, NTerminals.TK_ADD_EXPR_P],
    [],
    [NTerminals.TK_FACTOR, NTerminals.TK_MUL_EXPR_P],
    [Tokens.TK_MULTIPLY.value, NTerminals.TK_FACTOR, NTerminals.TK_MUL_EXPR_P],
    [Tokens.TK_DIVIDE.value, NTerminals.TK_FACTOR, NTerminals.TK_MUL_EXPR_P],
    [],
    [Tokens.TK_OPEN_PAREN.value, NTerminals.TK_EXPR, Tokens.TK_CLOSE_PAREN.value],
    [Tokens.TK_ID.value, NTerminals.TK_FACTOR_TAIL],
    [Tokens.TK_NUM.value],
    [Tokens.TK_OPEN_PAREN.value, NTerminals.TK_ARG_LIST_OPT, Tokens.TK_CLOSE_PAREN.value],
    [],
    [NTerminals.TK_ARG_LIST],
    [],
    [NTerminals.TK_EXPR, NTerminals.TK_ARG_LIST_P],
    [Tokens.TK_COMMA.value, NTerminals.TK_EXPR, NTerminals.TK_ARG_LIST_P],
    [],
    [Tokens.TK_INT.value],
    [Tokens.TK_FLOAT.value],
]


PARSING_TABLE = {}


def _set_entries(non_terminal, lookaheads, production_number):
    table_row = PARSING_TABLE.setdefault(non_terminal, {})
    for lookahead in lookaheads:
        table_row[lookahead] = production_number


_set_entries(NTerminals.TK_PROGRAM, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 1)
_set_entries(NTerminals.TK_FUNCTION_LIST, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 2)
_set_entries(NTerminals.TK_FUNCTION_LIST_P, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 3)
_set_entries(NTerminals.TK_FUNCTION_LIST_P, [EOF], 4)
_set_entries(NTerminals.TK_FUNCTION, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 5)
_set_entries(NTerminals.TK_PARAM_LIST_OPT, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 6)
_set_entries(NTerminals.TK_PARAM_LIST_OPT, [Tokens.TK_CLOSE_PAREN.value], 7)
_set_entries(NTerminals.TK_PARAM_LIST, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 8)
_set_entries(NTerminals.TK_PARAM_LIST_P, [Tokens.TK_COMMA.value], 9)
_set_entries(NTerminals.TK_PARAM_LIST_P, [Tokens.TK_CLOSE_PAREN.value], 10)
_set_entries(NTerminals.TK_PARAM, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 11)
_set_entries(NTerminals.TK_BLOCK, [Tokens.TK_OPEN_BRACE.value], 12)
_set_entries(NTerminals.TK_DECL_LIST_OPT, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 13)
_set_entries(NTerminals.TK_DECL_LIST_OPT, [Tokens.TK_IF.value, Tokens.TK_WHILE.value, Tokens.TK_PRINT.value, Tokens.TK_RETURN.value, Tokens.TK_ID.value, Tokens.TK_OPEN_BRACE.value, Tokens.TK_CLOSE_BRACE.value], 14)
_set_entries(NTerminals.TK_DECL_LIST, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 15)
_set_entries(NTerminals.TK_DECL_LIST_P, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 16)
_set_entries(NTerminals.TK_DECL_LIST_P, [Tokens.TK_IF.value, Tokens.TK_WHILE.value, Tokens.TK_PRINT.value, Tokens.TK_RETURN.value, Tokens.TK_ID.value, Tokens.TK_OPEN_BRACE.value, Tokens.TK_CLOSE_BRACE.value], 17)
_set_entries(NTerminals.TK_VAR_DECL, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 18)
_set_entries(NTerminals.TK_STMT_LIST_OPT, [Tokens.TK_IF.value, Tokens.TK_WHILE.value, Tokens.TK_PRINT.value, Tokens.TK_RETURN.value, Tokens.TK_ID.value, Tokens.TK_OPEN_BRACE.value], 19)
_set_entries(NTerminals.TK_STMT_LIST_OPT, [Tokens.TK_CLOSE_BRACE.value], 20)
_set_entries(NTerminals.TK_STMT_LIST, [Tokens.TK_IF.value, Tokens.TK_WHILE.value, Tokens.TK_PRINT.value, Tokens.TK_RETURN.value, Tokens.TK_ID.value, Tokens.TK_OPEN_BRACE.value], 21)
_set_entries(NTerminals.TK_STMT_LIST_P, [Tokens.TK_IF.value, Tokens.TK_WHILE.value, Tokens.TK_PRINT.value, Tokens.TK_RETURN.value, Tokens.TK_ID.value, Tokens.TK_OPEN_BRACE.value], 22)
_set_entries(NTerminals.TK_STMT_LIST_P, [Tokens.TK_CLOSE_BRACE.value], 23)
_set_entries(NTerminals.TK_STMT, [Tokens.TK_ID.value], 24)
_set_entries(NTerminals.TK_STMT, [Tokens.TK_IF.value], 25)
_set_entries(NTerminals.TK_STMT, [Tokens.TK_WHILE.value], 26)
_set_entries(NTerminals.TK_STMT, [Tokens.TK_PRINT.value], 27)
_set_entries(NTerminals.TK_STMT, [Tokens.TK_RETURN.value], 28)
_set_entries(NTerminals.TK_STMT, [Tokens.TK_OPEN_BRACE.value], 29)
_set_entries(NTerminals.TK_ASSIGN_STMT, [Tokens.TK_ID.value], 30)
_set_entries(NTerminals.TK_RETURN_STMT, [Tokens.TK_RETURN.value], 31)
_set_entries(NTerminals.TK_PRINT_STMT, [Tokens.TK_PRINT.value], 32)
_set_entries(NTerminals.TK_IF_STMT, [Tokens.TK_IF.value], 33)
_set_entries(NTerminals.TK_ELSE_PART, [Tokens.TK_ELSE.value], 34)
_set_entries(NTerminals.TK_ELSE_PART, [Tokens.TK_IF.value, Tokens.TK_WHILE.value, Tokens.TK_PRINT.value, Tokens.TK_RETURN.value, Tokens.TK_ID.value, Tokens.TK_OPEN_BRACE.value, Tokens.TK_CLOSE_BRACE.value, EOF], 35)
_set_entries(NTerminals.TK_WHILE_STMT, [Tokens.TK_WHILE.value], 36)
_set_entries(NTerminals.TK_EXPR, [Tokens.TK_OPEN_PAREN.value, Tokens.TK_ID.value, Tokens.TK_NUM.value], 37)
_set_entries(NTerminals.TK_REL_EXPR, [Tokens.TK_OPEN_PAREN.value, Tokens.TK_ID.value, Tokens.TK_NUM.value], 38)
_set_entries(NTerminals.TK_REL_EXPR_P, [Tokens.TK_EQUALTY.value, Tokens.TK_INEQUALTY.value, Tokens.TK_LESS.value, Tokens.TK_GREATER.value, Tokens.TK_LESS_OR_EQUAL.value, Tokens.TK_GREATER_OR_EQUAL.value], 39)
_set_entries(NTerminals.TK_REL_EXPR_P, [Tokens.TK_CLOSE_PAREN.value, Tokens.TK_SEMICOLON.value, Tokens.TK_COMMA.value], 40)
_set_entries(NTerminals.TK_REL_OP, [Tokens.TK_EQUALTY.value], 41)
_set_entries(NTerminals.TK_REL_OP, [Tokens.TK_INEQUALTY.value], 42)
_set_entries(NTerminals.TK_REL_OP, [Tokens.TK_LESS.value], 43)
_set_entries(NTerminals.TK_REL_OP, [Tokens.TK_GREATER.value], 44)
_set_entries(NTerminals.TK_REL_OP, [Tokens.TK_LESS_OR_EQUAL.value], 45)
_set_entries(NTerminals.TK_REL_OP, [Tokens.TK_GREATER_OR_EQUAL.value], 46)
_set_entries(NTerminals.TK_ADD_EXPR, [Tokens.TK_OPEN_PAREN.value, Tokens.TK_ID.value, Tokens.TK_NUM.value], 47)
_set_entries(NTerminals.TK_ADD_EXPR_P, [Tokens.TK_PLUS.value], 48)
_set_entries(NTerminals.TK_ADD_EXPR_P, [Tokens.TK_MINUS.value], 49)
_set_entries(NTerminals.TK_ADD_EXPR_P, [Tokens.TK_EQUALTY.value, Tokens.TK_INEQUALTY.value, Tokens.TK_LESS.value, Tokens.TK_GREATER.value, Tokens.TK_LESS_OR_EQUAL.value, Tokens.TK_GREATER_OR_EQUAL.value, Tokens.TK_CLOSE_PAREN.value, Tokens.TK_SEMICOLON.value, Tokens.TK_COMMA.value], 50)
_set_entries(NTerminals.TK_MUL_EXPR, [Tokens.TK_OPEN_PAREN.value, Tokens.TK_ID.value, Tokens.TK_NUM.value], 51)
_set_entries(NTerminals.TK_MUL_EXPR_P, [Tokens.TK_MULTIPLY.value], 52)
_set_entries(NTerminals.TK_MUL_EXPR_P, [Tokens.TK_DIVIDE.value], 53)
_set_entries(NTerminals.TK_MUL_EXPR_P, [Tokens.TK_PLUS.value, Tokens.TK_MINUS.value, Tokens.TK_EQUALTY.value, Tokens.TK_INEQUALTY.value, Tokens.TK_LESS.value, Tokens.TK_GREATER.value, Tokens.TK_LESS_OR_EQUAL.value, Tokens.TK_GREATER_OR_EQUAL.value, Tokens.TK_CLOSE_PAREN.value, Tokens.TK_SEMICOLON.value, Tokens.TK_COMMA.value], 54)
_set_entries(NTerminals.TK_FACTOR, [Tokens.TK_OPEN_PAREN.value], 55)
_set_entries(NTerminals.TK_FACTOR, [Tokens.TK_ID.value], 56)
_set_entries(NTerminals.TK_FACTOR, [Tokens.TK_NUM.value], 57)
_set_entries(NTerminals.TK_FACTOR_TAIL, [Tokens.TK_OPEN_PAREN.value], 58)
_set_entries(NTerminals.TK_FACTOR_TAIL, [Tokens.TK_MULTIPLY.value, Tokens.TK_DIVIDE.value, Tokens.TK_PLUS.value, Tokens.TK_MINUS.value, Tokens.TK_EQUALTY.value, Tokens.TK_INEQUALTY.value, Tokens.TK_LESS.value, Tokens.TK_GREATER.value, Tokens.TK_LESS_OR_EQUAL.value, Tokens.TK_GREATER_OR_EQUAL.value, Tokens.TK_CLOSE_PAREN.value, Tokens.TK_SEMICOLON.value, Tokens.TK_COMMA.value], 59)
_set_entries(NTerminals.TK_ARG_LIST_OPT, [Tokens.TK_OPEN_PAREN.value, Tokens.TK_ID.value, Tokens.TK_NUM.value], 60)
_set_entries(NTerminals.TK_ARG_LIST_OPT, [Tokens.TK_CLOSE_PAREN.value], 61)
_set_entries(NTerminals.TK_ARG_LIST, [Tokens.TK_OPEN_PAREN.value, Tokens.TK_ID.value, Tokens.TK_NUM.value], 62)
_set_entries(NTerminals.TK_ARG_LIST_P, [Tokens.TK_COMMA.value], 63)
_set_entries(NTerminals.TK_ARG_LIST_P, [Tokens.TK_CLOSE_PAREN.value], 64)
_set_entries(NTerminals.TK_TYPE, [Tokens.TK_INT.value], 65)
_set_entries(NTerminals.TK_TYPE, [Tokens.TK_FLOAT.value], 66)


def production_text(production_number):
    return PRODUCTIONS[production_number - 1]


def terminal_text(code):
    return TERMINAL_NAMES.get(code, str(code))


class ParseError(Exception):
    pass


class SyntacticAnalyser:
    def __init__(self, tokens):
        filtered_tokens = [token for token in tokens if token.code not in COMMENT_TOKENS]
        last_line = filtered_tokens[-1].line if filtered_tokens else 1
        self._tokens = filtered_tokens + [Token(EOF, "$", last_line)]
        self._position = 0
        self._stack = [EOF, NTerminals.TK_PROGRAM]

    def _current(self):
        return self._tokens[self._position]

    def _error(self, expected):
        current = self._current()
        expected_text = ", ".join(expected)
        raise ParseError(
            f"Linha {current.line}: esperado {expected_text}, encontrado {current.value!r}"
        )

    def parse(self):
        while self._stack:
            top = self._stack[-1]
            current = self._current()

            if top == EOF:
                if current.code == EOF:
                    self._stack.pop()
                    continue
                self._error(["fim de arquivo"])

            if isinstance(top, int):
                if top == current.code:
                    self._stack.pop()
                    self._position += 1
                    continue

                self._error([terminal_text(top)])

            production_number = PARSING_TABLE.get(top, {}).get(current.code)
            if production_number is None:
                expected = [terminal_text(code) for code in PARSING_TABLE.get(top, {})]
                self._error(expected if expected else [top.name])

            self._stack.pop()
            for symbol in reversed(production_text(production_number)):
                self._stack.append(symbol)

        print("Sentença ACEITA!")
        return True


def parse_tokens(tokens):
    return SyntacticAnalyser(tokens).parse()


def parse_source(source_code):
    tokens = list(LexicalAnalyser(source_code).generate_token())
    return parse_tokens(tokens)


def main():
    content = flags(argv)

    tokens = list(LexicalAnalyser(content).generate_token())
    
    print("\n-------------------|TOKENS|-------------------")
    print(f"{'Token':<15}{'Lexema':<20}{'Linha':<10}")
    print("-" * 45)
    for token in tokens:
        if token.code not in COMMENT_TOKENS:
            print(f"{token.code:<15}{token.value:<20}{token.line:<10}")

    try:
        parse_source(content)
    except ParseError as error:
        print(f"Erro sintático (error de parser) em:\n{type(error).__name__}: {error}")


if __name__ == "__main__":
    main()