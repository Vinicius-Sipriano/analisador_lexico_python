from sys import argv

from lexicalAnalyser import LexicalAnalyser, Token, Tokens
from receiveFlags import flags

# Códigos para não-terminais (usando apenas números)
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


TYPE_TOKENS = {
    Tokens.TK_INT.value,
    Tokens.TK_FLOAT.value,
}


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
    [TK_FUNCTION_LIST],
    [TK_FUNCTION, TK_FUNCTION_LIST_P],
    [TK_FUNCTION, TK_FUNCTION_LIST_P],
    [],
    [TK_TYPE, Tokens.TK_ID.value, Tokens.TK_OPEN_PAREN.value, TK_PARAM_LIST_OPT, Tokens.TK_CLOSE_PAREN.value, TK_BLOCK],
    [TK_PARAM_LIST],
    [],
    [TK_PARAM, TK_PARAM_LIST_P],
    [Tokens.TK_COMMA.value, TK_PARAM, TK_PARAM_LIST_P],
    [],
    [TK_TYPE, Tokens.TK_ID.value],
    [Tokens.TK_OPEN_BRACE.value, TK_DECL_LIST_OPT, TK_STMT_LIST_OPT, Tokens.TK_CLOSE_BRACE.value],
    [TK_DECL_LIST],
    [],
    [TK_VAR_DECL, TK_DECL_LIST_P],
    [TK_VAR_DECL, TK_DECL_LIST_P],
    [],
    [TK_TYPE, Tokens.TK_ID.value, Tokens.TK_SEMICOLON.value],
    [TK_STMT_LIST],
    [],
    [TK_STMT, TK_STMT_LIST_P],
    [TK_STMT, TK_STMT_LIST_P],
    [],
    [TK_ASSIGN_STMT],
    [TK_IF_STMT],
    [TK_WHILE_STMT],
    [TK_PRINT_STMT],
    [TK_RETURN_STMT],
    [TK_BLOCK],
    [Tokens.TK_ID.value, Tokens.TK_ATRIB.value, TK_EXPR, Tokens.TK_SEMICOLON.value],
    [Tokens.TK_RETURN.value, TK_EXPR, Tokens.TK_SEMICOLON.value],
    [Tokens.TK_PRINT.value, Tokens.TK_OPEN_PAREN.value, TK_EXPR, Tokens.TK_CLOSE_PAREN.value, Tokens.TK_SEMICOLON.value],
    [Tokens.TK_IF.value, Tokens.TK_OPEN_PAREN.value, TK_EXPR, Tokens.TK_CLOSE_PAREN.value, TK_STMT, TK_ELSE_PART],
    [Tokens.TK_ELSE.value, TK_STMT],
    [],
    [Tokens.TK_WHILE.value, Tokens.TK_OPEN_PAREN.value, TK_EXPR, Tokens.TK_CLOSE_PAREN.value, TK_STMT],
    [TK_REL_EXPR],
    [TK_ADD_EXPR, TK_REL_EXPR_P],
    [TK_REL_OP, TK_ADD_EXPR],
    [],
    [Tokens.TK_EQUALTY.value],
    [Tokens.TK_INEQUALTY.value],
    [Tokens.TK_LESS.value],
    [Tokens.TK_GREATER.value],
    [Tokens.TK_LESS_OR_EQUAL.value],
    [Tokens.TK_GREATER_OR_EQUAL.value],
    [TK_MUL_EXPR, TK_ADD_EXPR_P],
    [Tokens.TK_PLUS.value, TK_MUL_EXPR, TK_ADD_EXPR_P],
    [Tokens.TK_MINUS.value, TK_MUL_EXPR, TK_ADD_EXPR_P],
    [],
    [TK_FACTOR, TK_MUL_EXPR_P],
    [Tokens.TK_MULTIPLY.value, TK_FACTOR, TK_MUL_EXPR_P],
    [Tokens.TK_DIVIDE.value, TK_FACTOR, TK_MUL_EXPR_P],
    [],
    [Tokens.TK_OPEN_PAREN.value, TK_EXPR, Tokens.TK_CLOSE_PAREN.value],
    [Tokens.TK_ID.value, TK_FACTOR_TAIL],
    [Tokens.TK_NUM.value],
    [Tokens.TK_OPEN_PAREN.value, TK_ARG_LIST_OPT, Tokens.TK_CLOSE_PAREN.value],
    [],
    [TK_ARG_LIST],
    [],
    [TK_EXPR, TK_ARG_LIST_P],
    [Tokens.TK_COMMA.value, TK_EXPR, TK_ARG_LIST_P],
    [],
    [Tokens.TK_INT.value],
    [Tokens.TK_FLOAT.value],
]


PARSING_TABLE = {}


def _set_entries(non_terminal, lookaheads, production_number):
    table_row = PARSING_TABLE.setdefault(non_terminal, {})
    for lookahead in lookaheads:
        table_row[lookahead] = production_number


_set_entries(TK_PROGRAM, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 1)
_set_entries(TK_FUNCTION_LIST, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 2)
_set_entries(TK_FUNCTION_LIST_P, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 3)
_set_entries(TK_FUNCTION_LIST_P, [EOF], 4)
_set_entries(TK_FUNCTION, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 5)
_set_entries(TK_PARAM_LIST_OPT, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 6)
_set_entries(TK_PARAM_LIST_OPT, [Tokens.TK_CLOSE_PAREN.value], 7)
_set_entries(TK_PARAM_LIST, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 8)
_set_entries(TK_PARAM_LIST_P, [Tokens.TK_COMMA.value], 9)
_set_entries(TK_PARAM_LIST_P, [Tokens.TK_CLOSE_PAREN.value], 10)
_set_entries(TK_PARAM, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 11)
_set_entries(TK_BLOCK, [Tokens.TK_OPEN_BRACE.value], 12)
_set_entries(TK_DECL_LIST_OPT, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 13)
_set_entries(TK_DECL_LIST_OPT, [Tokens.TK_IF.value, Tokens.TK_WHILE.value, Tokens.TK_PRINT.value, Tokens.TK_RETURN.value, Tokens.TK_ID.value, Tokens.TK_OPEN_BRACE.value, Tokens.TK_CLOSE_BRACE.value], 14)
_set_entries(TK_DECL_LIST, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 15)
_set_entries(TK_DECL_LIST_P, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 16)
_set_entries(TK_DECL_LIST_P, [Tokens.TK_IF.value, Tokens.TK_WHILE.value, Tokens.TK_PRINT.value, Tokens.TK_RETURN.value, Tokens.TK_ID.value, Tokens.TK_OPEN_BRACE.value, Tokens.TK_CLOSE_BRACE.value], 17)
_set_entries(TK_VAR_DECL, [Tokens.TK_INT.value, Tokens.TK_FLOAT.value], 18)
_set_entries(TK_STMT_LIST_OPT, [Tokens.TK_IF.value, Tokens.TK_WHILE.value, Tokens.TK_PRINT.value, Tokens.TK_RETURN.value, Tokens.TK_ID.value, Tokens.TK_OPEN_BRACE.value], 19)
_set_entries(TK_STMT_LIST_OPT, [Tokens.TK_CLOSE_BRACE.value], 20)
_set_entries(TK_STMT_LIST, [Tokens.TK_IF.value, Tokens.TK_WHILE.value, Tokens.TK_PRINT.value, Tokens.TK_RETURN.value, Tokens.TK_ID.value, Tokens.TK_OPEN_BRACE.value], 21)
_set_entries(TK_STMT_LIST_P, [Tokens.TK_IF.value, Tokens.TK_WHILE.value, Tokens.TK_PRINT.value, Tokens.TK_RETURN.value, Tokens.TK_ID.value, Tokens.TK_OPEN_BRACE.value], 22)
_set_entries(TK_STMT_LIST_P, [Tokens.TK_CLOSE_BRACE.value], 23)
_set_entries(TK_STMT, [Tokens.TK_ID.value], 24)
_set_entries(TK_STMT, [Tokens.TK_IF.value], 25)
_set_entries(TK_STMT, [Tokens.TK_WHILE.value], 26)
_set_entries(TK_STMT, [Tokens.TK_PRINT.value], 27)
_set_entries(TK_STMT, [Tokens.TK_RETURN.value], 28)
_set_entries(TK_STMT, [Tokens.TK_OPEN_BRACE.value], 29)
_set_entries(TK_ASSIGN_STMT, [Tokens.TK_ID.value], 30)
_set_entries(TK_RETURN_STMT, [Tokens.TK_RETURN.value], 31)
_set_entries(TK_PRINT_STMT, [Tokens.TK_PRINT.value], 32)
_set_entries(TK_IF_STMT, [Tokens.TK_IF.value], 33)
_set_entries(TK_ELSE_PART, [Tokens.TK_ELSE.value], 34)
_set_entries(TK_ELSE_PART, [Tokens.TK_IF.value, Tokens.TK_WHILE.value, Tokens.TK_PRINT.value, Tokens.TK_RETURN.value, Tokens.TK_ID.value, Tokens.TK_OPEN_BRACE.value, Tokens.TK_CLOSE_BRACE.value, EOF], 35)
_set_entries(TK_WHILE_STMT, [Tokens.TK_WHILE.value], 36)
_set_entries(TK_EXPR, [Tokens.TK_OPEN_PAREN.value, Tokens.TK_ID.value, Tokens.TK_NUM.value], 37)
_set_entries(TK_REL_EXPR, [Tokens.TK_OPEN_PAREN.value, Tokens.TK_ID.value, Tokens.TK_NUM.value], 38)
_set_entries(TK_REL_EXPR_P, [Tokens.TK_EQUALTY.value, Tokens.TK_INEQUALTY.value, Tokens.TK_LESS.value, Tokens.TK_GREATER.value, Tokens.TK_LESS_OR_EQUAL.value, Tokens.TK_GREATER_OR_EQUAL.value], 39)
_set_entries(TK_REL_EXPR_P, [Tokens.TK_CLOSE_PAREN.value, Tokens.TK_SEMICOLON.value, Tokens.TK_COMMA.value], 40)
_set_entries(TK_REL_OP, [Tokens.TK_EQUALTY.value], 41)
_set_entries(TK_REL_OP, [Tokens.TK_INEQUALTY.value], 42)
_set_entries(TK_REL_OP, [Tokens.TK_LESS.value], 43)
_set_entries(TK_REL_OP, [Tokens.TK_GREATER.value], 44)
_set_entries(TK_REL_OP, [Tokens.TK_LESS_OR_EQUAL.value], 45)
_set_entries(TK_REL_OP, [Tokens.TK_GREATER_OR_EQUAL.value], 46)
_set_entries(TK_ADD_EXPR, [Tokens.TK_OPEN_PAREN.value, Tokens.TK_ID.value, Tokens.TK_NUM.value], 47)
_set_entries(TK_ADD_EXPR_P, [Tokens.TK_PLUS.value], 48)
_set_entries(TK_ADD_EXPR_P, [Tokens.TK_MINUS.value], 49)
_set_entries(TK_ADD_EXPR_P, [Tokens.TK_EQUALTY.value, Tokens.TK_INEQUALTY.value, Tokens.TK_LESS.value, Tokens.TK_GREATER.value, Tokens.TK_LESS_OR_EQUAL.value, Tokens.TK_GREATER_OR_EQUAL.value, Tokens.TK_CLOSE_PAREN.value, Tokens.TK_SEMICOLON.value, Tokens.TK_COMMA.value], 50)
_set_entries(TK_MUL_EXPR, [Tokens.TK_OPEN_PAREN.value, Tokens.TK_ID.value, Tokens.TK_NUM.value], 51)
_set_entries(TK_MUL_EXPR_P, [Tokens.TK_MULTIPLY.value], 52)
_set_entries(TK_MUL_EXPR_P, [Tokens.TK_DIVIDE.value], 53)
_set_entries(TK_MUL_EXPR_P, [Tokens.TK_PLUS.value, Tokens.TK_MINUS.value, Tokens.TK_EQUALTY.value, Tokens.TK_INEQUALTY.value, Tokens.TK_LESS.value, Tokens.TK_GREATER.value, Tokens.TK_LESS_OR_EQUAL.value, Tokens.TK_GREATER_OR_EQUAL.value, Tokens.TK_CLOSE_PAREN.value, Tokens.TK_SEMICOLON.value, Tokens.TK_COMMA.value], 54)
_set_entries(TK_FACTOR, [Tokens.TK_OPEN_PAREN.value], 55)
_set_entries(TK_FACTOR, [Tokens.TK_ID.value], 56)
_set_entries(TK_FACTOR, [Tokens.TK_NUM.value], 57)
_set_entries(TK_FACTOR_TAIL, [Tokens.TK_OPEN_PAREN.value], 58)
_set_entries(TK_FACTOR_TAIL, [Tokens.TK_MULTIPLY.value, Tokens.TK_DIVIDE.value, Tokens.TK_PLUS.value, Tokens.TK_MINUS.value, Tokens.TK_EQUALTY.value, Tokens.TK_INEQUALTY.value, Tokens.TK_LESS.value, Tokens.TK_GREATER.value, Tokens.TK_LESS_OR_EQUAL.value, Tokens.TK_GREATER_OR_EQUAL.value, Tokens.TK_CLOSE_PAREN.value, Tokens.TK_SEMICOLON.value, Tokens.TK_COMMA.value], 59)
_set_entries(TK_ARG_LIST_OPT, [Tokens.TK_OPEN_PAREN.value, Tokens.TK_ID.value, Tokens.TK_NUM.value], 60)
_set_entries(TK_ARG_LIST_OPT, [Tokens.TK_CLOSE_PAREN.value], 61)
_set_entries(TK_ARG_LIST, [Tokens.TK_OPEN_PAREN.value, Tokens.TK_ID.value, Tokens.TK_NUM.value], 62)
_set_entries(TK_ARG_LIST_P, [Tokens.TK_COMMA.value], 63)
_set_entries(TK_ARG_LIST_P, [Tokens.TK_CLOSE_PAREN.value], 64)
_set_entries(TK_TYPE, [Tokens.TK_INT.value], 65)
_set_entries(TK_TYPE, [Tokens.TK_FLOAT.value], 66)


def symbol_repr(symbol):
    """Converte um símbolo (terminal, não-terminal ou EOF) para representação legível"""
    if symbol == EOF:
        return "$"
    elif symbol < 100:  # Terminal - código de token
        terminal_name = TERMINAL_NAMES.get(symbol, f"T{symbol}")
        return f"T{symbol}({terminal_name})"
    else:  # Non-terminal
        return f"N{symbol}"


def production_text(production_number):
    return PRODUCTIONS[production_number - 1]


def terminal_text(code):
    return TERMINAL_NAMES.get(code, str(code))


class ParseError(Exception):
    pass


class SemanticError(Exception):
    pass


def _is_type_token(token_code):
    return token_code in TYPE_TOKENS


def _count_parenthesized_items(tokens, start_index):
    depth = 1
    count = 0
    has_item = False
    index = start_index

    while index < len(tokens):
        token = tokens[index]

        if token.code == Tokens.TK_OPEN_PAREN.value:
            depth += 1
            has_item = True
        elif token.code == Tokens.TK_CLOSE_PAREN.value:
            depth -= 1
            if depth == 0:
                if not has_item:
                    return 0, index
                return count + 1, index
        elif token.code == Tokens.TK_COMMA.value and depth == 1:
            count += 1
            has_item = False
        else:
            has_item = True

        index += 1

    raise SemanticError("Chamada de função incompleta.")


def _collect_function_signatures(tokens):
    signatures = {}
    brace_depth = 0
    index = 0

    while index < len(tokens):
        token = tokens[index]

        if token.code == Tokens.TK_OPEN_BRACE.value:
            brace_depth += 1
            index += 1
            continue

        if token.code == Tokens.TK_CLOSE_BRACE.value:
            brace_depth = max(0, brace_depth - 1)
            index += 1
            continue

        if (
            brace_depth == 0
            and _is_type_token(token.code)
            and index + 2 < len(tokens)
            and tokens[index + 1].code == Tokens.TK_ID.value
            and tokens[index + 2].code == Tokens.TK_OPEN_PAREN.value
        ):
            function_name = tokens[index + 1].value
            parameter_count, closing_index = _count_parenthesized_items(tokens, index + 3)
            signatures[function_name] = parameter_count
            index = closing_index + 1
            continue

        index += 1

    return signatures


def _validate_function_calls(tokens, signatures):
    brace_depth = 0
    index = 0

    while index < len(tokens):
        token = tokens[index]

        if token.code == Tokens.TK_OPEN_BRACE.value:
            brace_depth += 1
            index += 1
            continue

        if token.code == Tokens.TK_CLOSE_BRACE.value:
            brace_depth = max(0, brace_depth - 1)
            index += 1
            continue

        is_function_definition = (
            brace_depth == 0
            and _is_type_token(token.code)
            and index + 2 < len(tokens)
            and tokens[index + 1].code == Tokens.TK_ID.value
            and tokens[index + 2].code == Tokens.TK_OPEN_PAREN.value
        )

        if is_function_definition:
            _, closing_index = _count_parenthesized_items(tokens, index + 3)
            index = closing_index + 1
            continue

        if (
            token.code == Tokens.TK_ID.value
            and index + 1 < len(tokens)
            and tokens[index + 1].code == Tokens.TK_OPEN_PAREN.value
        ):
            function_name = token.value
            expected_count = signatures.get(function_name)

            if expected_count is None:
                raise SemanticError(f"Função '{function_name}' não declarada.")

            actual_count, closing_index = _count_parenthesized_items(tokens, index + 2)
            if actual_count != expected_count:
                raise SemanticError(
                    f"Número diferente de parâmetros na chamada de '{function_name}': "
                    f"esperado {expected_count}, encontrado {actual_count}."
                )

            index = closing_index + 1
            continue

        index += 1


def validate_semantics(tokens):
    signatures = _collect_function_signatures(tokens)
    _validate_function_calls(tokens, signatures)


class SyntacticAnalyser:
    def __init__(self, tokens):
        filtered_tokens = [token for token in tokens if token.code not in COMMENT_TOKENS]
        last_line = filtered_tokens[-1].line if filtered_tokens else 1
        self._tokens = filtered_tokens + [Token(EOF, "$", last_line)]
        self._position = 0
        self._stack = [EOF, TK_PROGRAM]
        self._step = 0

    def _current(self):
        return self._tokens[self._position]

    def _error(self, expected):
        current = self._current()
        expected_text = ", ".join(expected)
        raise ParseError(
            f"Linha {current.line}: esperado {expected_text}, encontrado {current.value!r}"
        )

    def _print_step(self, action=""):
        """Imprime o estado atual da análise"""
        current = self._current()
        print(f"\n--- Passo {self._step} ---")
        print(f"Código do Token: {current.code:<3} | Token: {current.value:<15} | Linha: {current.line}")
        pilha_repr = " ".join(symbol_repr(s) for s in self._stack)
        print(f"Pilha: [{pilha_repr}]")
        if action:
            print(f"Ação: {action}")

    def parse(self):
        self._print_step("INÍCIO")
        
        while self._stack:
            top = self._stack[-1]
            current = self._current()

            if top == EOF:
                if current.code == EOF:
                    self._stack.pop()
                    self._step += 1
                    self._print_step("POP EOF da pilha")
                    continue
                self._error(["fim de arquivo"])

            # Terminal (código de token: 1-35)
            if isinstance(top, int) and top < 100:
                if top == current.code:
                    self._stack.pop()
                    self._position += 1
                    self._step += 1
                    terminal_name = terminal_text(top)
                    self._print_step(f"MATCH: Terminal '{terminal_name}' (código {top}) removido")
                    continue

                self._error([terminal_text(top)])

            # Non-terminal (código >= 100)
            if isinstance(top, int) and top >= 100:
                production_number = PARSING_TABLE.get(top, {}).get(current.code)
                if production_number is None:
                    expected = [terminal_text(code) for code in PARSING_TABLE.get(top, {})]
                    self._error(expected if expected else [str(top)])

                self._stack.pop()
                for symbol in reversed(production_text(production_number)):
                    self._stack.append(symbol)
                
                self._step += 1
                self._print_step(f"REDUÇÃO: Produção {production_number}")
                continue
            
            # Se chegou aqui, há algo inesperado
            raise ParseError(f"Símbolo inválido na pilha: {top}")

        return True


def parse_tokens(tokens):
    result = SyntacticAnalyser(tokens).parse()
    validate_semantics(tokens)
    print("\n" + "="*50)
    print("✓ Sentença ACEITA!")
    print("="*50)
    return result


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
        parse_tokens(tokens)
    except ParseError as error:
        print(f"Erro sintático (error de parser) em:\n{type(error).__name__}: {error}")
    except SemanticError as error:
        print(f"Erro semântico em:\n{type(error).__name__}: {error}")


if __name__ == "__main__":
    main()