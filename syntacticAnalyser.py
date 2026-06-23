from sys import argv

from lexicalAnalyser import LexicalAnalyser, Token, Tokens
from semanticAnalyser import SemanticAnalyser, SemanticError
from receiveFlags import flags

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
    [TK_FUNCTION_LIST],
    [TK_FUNCTION, TK_FUNCTION_LIST_P],
    [TK_FUNCTION, TK_FUNCTION_LIST_P],
    [],
    [TK_TYPE, Tokens.TK_ID.value, "#ACAO_DECL_FUNCAO", Tokens.TK_OPEN_PAREN.value, TK_PARAM_LIST_OPT, Tokens.TK_CLOSE_PAREN.value, TK_BLOCK, "#ACAO_END_FUNCTION"],
    [TK_PARAM_LIST],
    [],
    [TK_PARAM, TK_PARAM_LIST_P],
    [Tokens.TK_COMMA.value, TK_PARAM, TK_PARAM_LIST_P],
    [],
    [TK_TYPE, Tokens.TK_ID.value, "#ACAO_DECL_PARAM"],
    [Tokens.TK_OPEN_BRACE.value, TK_DECL_LIST_OPT, TK_STMT_LIST_OPT, Tokens.TK_CLOSE_BRACE.value],
    [TK_DECL_LIST],
    [],
    [TK_VAR_DECL, TK_DECL_LIST_P],
    [TK_VAR_DECL, TK_DECL_LIST_P],
    [],
    [TK_TYPE, Tokens.TK_ID.value, "#ACAO_DECL_VAR", Tokens.TK_SEMICOLON.value],
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
    [Tokens.TK_ID.value, Tokens.TK_ATRIB.value, TK_EXPR, "#ACAO_ASSIGN", Tokens.TK_SEMICOLON.value],
    [Tokens.TK_RETURN.value, TK_EXPR, "#ACAO_RETURN", Tokens.TK_SEMICOLON.value],
    [Tokens.TK_PRINT.value, Tokens.TK_OPEN_PAREN.value, TK_EXPR, Tokens.TK_CLOSE_PAREN.value, Tokens.TK_SEMICOLON.value],
    [Tokens.TK_IF.value, Tokens.TK_OPEN_PAREN.value, TK_EXPR, Tokens.TK_CLOSE_PAREN.value, TK_STMT, TK_ELSE_PART],
    [Tokens.TK_ELSE.value, TK_STMT],
    [],
    [Tokens.TK_WHILE.value, Tokens.TK_OPEN_PAREN.value, TK_EXPR, Tokens.TK_CLOSE_PAREN.value, TK_STMT],
    [TK_REL_EXPR],
    [TK_ADD_EXPR, TK_REL_EXPR_P, "#ACAO_REL_EXPR"],
    [TK_REL_OP, TK_ADD_EXPR, "#ACAO_REL_EXPR_P"],
    ["#ACAO_EMPTY_REL_EXPR_P"],
    [Tokens.TK_EQUALTY.value],
    [Tokens.TK_INEQUALTY.value],
    [Tokens.TK_LESS.value],
    [Tokens.TK_GREATER.value],
    [Tokens.TK_LESS_OR_EQUAL.value],
    [Tokens.TK_GREATER_OR_EQUAL.value],
    [TK_MUL_EXPR, TK_ADD_EXPR_P, "#ACAO_ADD_EXPR"],
    [Tokens.TK_PLUS.value, TK_MUL_EXPR, TK_ADD_EXPR_P, "#ACAO_ADD_EXPR_P"],
    [Tokens.TK_MINUS.value, TK_MUL_EXPR, TK_ADD_EXPR_P, "#ACAO_ADD_EXPR_P_MINUS"],
    ["#ACAO_EMPTY_ADD_EXPR_P"],
    [TK_FACTOR, TK_MUL_EXPR_P, "#ACAO_MUL_EXPR"],
    [Tokens.TK_MULTIPLY.value, TK_FACTOR, TK_MUL_EXPR_P, "#ACAO_MUL_EXPR_P"],
    [Tokens.TK_DIVIDE.value, TK_FACTOR, TK_MUL_EXPR_P, "#ACAO_MUL_EXPR_P_DIV"],
    ["#ACAO_EMPTY_MUL_EXPR_P"],
    [Tokens.TK_OPEN_PAREN.value, TK_EXPR, Tokens.TK_CLOSE_PAREN.value],
    [Tokens.TK_ID.value, TK_FACTOR_TAIL, "#ACAO_FACTOR_ID"],
    [Tokens.TK_NUM.value],
    [Tokens.TK_OPEN_PAREN.value, TK_ARG_LIST_OPT, Tokens.TK_CLOSE_PAREN.value, "#ACAO_CALL_ARGS"],
    [],
    [TK_ARG_LIST],
    [],
    [TK_EXPR, TK_ARG_LIST_P, "#ACAO_BUILD_ARG_LIST"],
    [Tokens.TK_COMMA.value, TK_EXPR, TK_ARG_LIST_P, "#ACAO_APPEND_ARG_LIST"],
    ["#ACAO_EMPTY_ARGS"],
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
    elif isinstance(symbol, str):
        return symbol
    elif symbol < 100:
        terminal_name = TERMINAL_NAMES.get(symbol, f"T{symbol}")
        return f"T{symbol}({terminal_name})"
    else:
        return f"N{symbol}"


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
        self._stack = [EOF, TK_PROGRAM]
        self._step = 0
        self._semantic_stack = []
        self.semantic = SemanticAnalyser()

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

    def _push_terminal_semantic(self, token):
        if token.code == Tokens.TK_ID.value:
            self._semantic_stack.append({
                'kind': 'identifier',
                'name': token.value,
                'line': token.line
            })
        elif token.code == Tokens.TK_NUM.value:
            self._semantic_stack.append({
                'kind': 'expr',
                'type': 'float' if isinstance(token.value, float) else 'int',
                'line': token.line
            })
        elif token.code == Tokens.TK_INT.value:
            self._semantic_stack.append({
                'kind': 'type',
                'type': 'int',
                'line': token.line
            })
        elif token.code == Tokens.TK_FLOAT.value:
            self._semantic_stack.append({
                'kind': 'type',
                'type': 'float',
                'line': token.line
            })
        elif token.code in {
            Tokens.TK_PLUS.value,
            Tokens.TK_MINUS.value,
            Tokens.TK_MULTIPLY.value,
            Tokens.TK_DIVIDE.value,
            Tokens.TK_EQUALTY.value,
            Tokens.TK_INEQUALTY.value,
            Tokens.TK_LESS.value,
            Tokens.TK_GREATER.value,
            Tokens.TK_LESS_OR_EQUAL.value,
            Tokens.TK_GREATER_OR_EQUAL.value,
        }:
            self._semantic_stack.append({
                'kind': 'operator',
                'symbol': token.value,
                'line': token.line
            })

    def _execute_semantic_action(self, action):
        if action == "#ACAO_DECL_FUNCAO":
            token_id = self._tokens[self._position - 1]
            token_type = self._tokens[self._position - 2]
            self.semantic.register_function(
                name=token_id.value,
                idType=token_type.value,
                line=token_id.line
            )
            return

        if action == "#ACAO_END_FUNCTION":
            self.semantic.end_function()
            return

        if action == "#ACAO_ENTER_BLOCK":
            self.semantic.enter_scope("block")
            return

        if action == "#ACAO_EXIT_BLOCK":
            self.semantic.exit_scope()
            return

        if action == "#ACAO_DECL_PARAM":
            identifier = self._semantic_stack.pop()
            typ = self._semantic_stack.pop()
            self.semantic.register_param(
                name=identifier['name'],
                idType=typ['type'],
                line=identifier['line']
            )
            return

        if action == "#ACAO_DECL_VAR":
            identifier = self._semantic_stack.pop()
            typ = self._semantic_stack.pop()
            self.semantic.register_variable(
                name=identifier['name'],
                idType=typ['type'],
                line=identifier['line']
            )
            return

        if action == "#ACAO_ASSIGN":
            expr = self._semantic_stack.pop()
            identifier = self._semantic_stack.pop()
            self.semantic.check_assignment(
                name=identifier['name'],
                expr_type=expr['type'],
                line=identifier['line']
            )
            return

        if action == "#ACAO_RETURN":
            expr = self._semantic_stack.pop()
            self.semantic.check_return(
                expr_type=expr['type'],
                line=expr['line']
            )
            return

        if action == "#ACAO_EMPTY_MUL_EXPR_P":
            self._semantic_stack.append({
                'kind': 'op_list',
                'items': []
            })
            return

        if action == "#ACAO_MUL_EXPR_P":
            tail = self._semantic_stack.pop()
            factor = self._semantic_stack.pop()
            operator = self._semantic_stack.pop()
            items = [{'op': '*', 'type': factor['type'], 'line': factor['line']}]
            items.extend(tail['items'])
            self._semantic_stack.append({
                'kind': 'op_list',
                'items': items
            })
            return

        if action == "#ACAO_MUL_EXPR_P_DIV":
            tail = self._semantic_stack.pop()
            factor = self._semantic_stack.pop()
            operator = self._semantic_stack.pop()
            items = [{'op': '/', 'type': factor['type'], 'line': factor['line']}]
            items.extend(tail['items'])
            self._semantic_stack.append({
                'kind': 'op_list',
                'items': items
            })
            return

        if action == "#ACAO_MUL_EXPR":
            tail = self._semantic_stack.pop()
            factor = self._semantic_stack.pop()
            result_type = factor['type']
            for item in tail['items']:
                result_type = self.semantic.evaluate_arithmetic(
                    result_type,
                    item['type'],
                    item['op'],
                    item['line']
                )
            self._semantic_stack.append({
                'kind': 'expr',
                'type': result_type,
                'line': factor['line']
            })
            return

        if action == "#ACAO_EMPTY_ADD_EXPR_P":
            self._semantic_stack.append({
                'kind': 'op_list',
                'items': []
            })
            return

        if action == "#ACAO_ADD_EXPR_P":
            tail = self._semantic_stack.pop()
            mul_expr = self._semantic_stack.pop()
            operator = self._semantic_stack.pop()
            items = [{'op': '+', 'type': mul_expr['type'], 'line': mul_expr['line']}]
            items.extend(tail['items'])
            self._semantic_stack.append({
                'kind': 'op_list',
                'items': items
            })
            return

        if action == "#ACAO_ADD_EXPR_P_MINUS":
            tail = self._semantic_stack.pop()
            mul_expr = self._semantic_stack.pop()
            operator = self._semantic_stack.pop()
            items = [{'op': '-', 'type': mul_expr['type'], 'line': mul_expr['line']}]
            items.extend(tail['items'])
            self._semantic_stack.append({
                'kind': 'op_list',
                'items': items
            })
            return

        if action == "#ACAO_ADD_EXPR":
            tail = self._semantic_stack.pop()
            mul_expr = self._semantic_stack.pop()
            result_type = mul_expr['type']
            for item in tail['items']:
                result_type = self.semantic.evaluate_arithmetic(
                    result_type,
                    item['type'],
                    item['op'],
                    item['line']
                )
            self._semantic_stack.append({
                'kind': 'expr',
                'type': result_type,
                'line': mul_expr['line']
            })
            return

        if action == "#ACAO_EMPTY_REL_EXPR_P":
            self._semantic_stack.append({
                'kind': 'rel_tail',
                'operator': None,
                'rhs_type': None,
                'line': None
            })
            return

        if action == "#ACAO_REL_EXPR_P":
            add_expr = self._semantic_stack.pop()
            op = self._semantic_stack.pop()
            self._semantic_stack.append({
                'kind': 'rel_tail',
                'operator': op['symbol'],
                'rhs_type': add_expr['type'],
                'line': op['line']
            })
            return

        if action == "#ACAO_REL_EXPR":
            rel_tail = self._semantic_stack.pop()
            add_expr = self._semantic_stack.pop()
            if rel_tail['operator'] is None:
                self._semantic_stack.append(add_expr)
                return
            result_type = self.semantic.evaluate_relational(
                add_expr['type'],
                rel_tail['rhs_type'],
                rel_tail['operator'],
                rel_tail['line']
            )
            self._semantic_stack.append({
                'kind': 'expr',
                'type': result_type,
                'line': add_expr['line']
            })
            return

        if action == "#ACAO_EMPTY_ARGS":
            self._semantic_stack.append({
                'kind': 'args',
                'types': []
            })
            return

        if action == "#ACAO_BUILD_ARG_LIST":
            arg_tail = self._semantic_stack.pop()
            expr = self._semantic_stack.pop()
            self._semantic_stack.append({
                'kind': 'args',
                'types': [expr['type']] + arg_tail['types']
            })
            return

        if action == "#ACAO_APPEND_ARG_LIST":
            arg_tail = self._semantic_stack.pop()
            expr = self._semantic_stack.pop()
            self._semantic_stack.append({
                'kind': 'args',
                'types': [expr['type']] + arg_tail['types']
            })
            return

        if action == "#ACAO_CALL_ARGS":
            if self._semantic_stack and self._semantic_stack[-1]['kind'] == 'args':
                args = self._semantic_stack.pop()
            else:
                args = {'kind': 'args', 'types': []}
            self._semantic_stack.append(args)
            return

        if action == "#ACAO_FACTOR_ID":
            tail = None
            if self._semantic_stack and self._semantic_stack[-1]['kind'] == 'args':
                tail = self._semantic_stack.pop()
            identifier = self._semantic_stack.pop()
            if tail:
                func_type = self.semantic.get_symbol_type(identifier['name'], identifier['line'])
                self._semantic_stack.append({
                    'kind': 'expr',
                    'type': func_type,
                    'line': identifier['line']
                })
                return
            expr_type = self.semantic.get_symbol_type(identifier['name'], identifier['line'])
            self._semantic_stack.append({
                'kind': 'expr',
                'type': expr_type,
                'line': identifier['line']
            })
            return

        raise ParseError(f"Ação semântica desconhecida: {action}")

    def parse(self):
        self._print_step("INÍCIO")
        
        while self._stack:
            top = self._stack[-1]
            current = self._current()

            if isinstance(top, str) and top.startswith("#"):
                self._stack.pop()
                self._execute_semantic_action(top)
                self._step += 1
                self._print_step(f"AÇÃO SEMÂNTICA: {top}")
                continue

            if top == EOF:
                if current.code == EOF:
                    self._stack.pop()
                    self._step += 1
                    self._print_step("POP EOF da pilha")
                    continue
                self._error(["fim de arquivo"])

            if isinstance(top, int) and top < 100:
                if top == current.code:
                    self._stack.pop()
                    self._push_terminal_semantic(current)
                    self._position += 1
                    self._step += 1
                    terminal_name = terminal_text(top)
                    self._print_step(f"MATCH: Terminal '{terminal_name}' (código {top}) removido")
                    continue

                self._error([terminal_text(top)])

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
            
            raise ParseError(f"Símbolo inválido na pilha: {top}")

        print("\n" + "="*50)
        print("✓ Sentença ACEITA!")
        print("="*50)
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

    syntactic_analyser = SyntacticAnalyser(tokens)

    try:
        syntactic_analyser.parse()
        print("\n" + "="*20 + " RELATÓRIO SEMÂNTICO FINAL " + "="*20)
        syntactic_analyser.semantic.show_symbol_table()

    except ParseError as error:
        print(f"Erro sintático (error de parser) em:\n{type(error).__name__}: {error}")
    except SemanticError as error:
        print(f"Erro semântico em:\n{type(error).__name__}: {error}")

if __name__ == "__main__":
    main()