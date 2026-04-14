from sys import argv
from receiveFlags import flags
from typing import NamedTuple
import re

class LexicalError:

    def __init__(self, line, col, lex, mesg):
        self.line = line
        self.col = col
        self.lex = lex
        self.mesg = mesg
        self.print_error()

    def print_error(self):
        print("\n-------------------|ERRO|-------------------")
        print(f"Erro léxico na linha {self.line}, coluna {self.col}:")
        print(f"  {self.lex}")
        print(f"  {self.mesg}")
        print("----------------------------------------------")

class Token(NamedTuple):
    type: str
    value: str
    line: int
    col: int

class LexicalAnalyser:

    def __init__(self, source_code):
        self.__source_code = source_code

        self.__keywords = {
            "if", "else", "while", "return", "int", "float", "print"
        }

        self.__keywords1 = {
            "IF", "ELSE", "WHILE", "RETURN", "INT", "FLOAT", "PRINT"
        }

        self.__token_pair = [
            ("TK_NUM", r"\d+(\.\d+)?"),
            ("TK_ID", r"[a-zA-Z_][a-zA-Z0-9_]*"),
            ("TK_OP_RE", r"==|!=|<=|>=|[\<\>]"),
            ("TK_PERIOD", r"\."),
            ("TK_SEMICOLON", r";"),
            ("TK_ATRIB", r"="),
            ("TK_OP_AR", r"[\+\-\*/]"),
            ("TK_OPEN_PAREN", r"\("),
            ("TK_CLOSE_PAREN", r"\)"),
            ("TK_OPEN_BRACE", r"\{"),
            ("TK_CLOSE_BRACE", r"\}"),
            ("TK_COMMA", r","),
            ("TK_NEW_LINE", r"\r?\n"),
            ("TK_SPACE", r"[ \t]+"),
            ("TK_MISMATCH", r".")
        ]

    def generate_token(self):

        token_base = self.__token_pair
        buffer = self.__source_code

        regex_rules = "|".join("(?P<%s>%s)" % strPair for strPair in token_base)
        line = 1
        col_start = 0

        for matchedPattern in re.finditer(regex_rules, buffer):
            tk_type = matchedPattern.lastgroup
            lexeme = matchedPattern.group()
            column = (matchedPattern.start() + 1) - col_start
            if tk_type == "TK_NUM":
                if "." in lexeme:
                    lexeme = float(lexeme)
                else:
                    lexeme = int(lexeme)
            elif lexeme.upper() in self.__keywords1 and tk_type == "TK_ID":
                if lexeme not in self.__keywords:
                    LexicalError(line, column, lexeme, "Identificador não pode ser igual a palavra reservada.")
                tk_type = "TK_KEYWORD"
            elif tk_type == "TK_NEW_LINE":
                col_start = matchedPattern.end()
                line += 1
                continue
            elif tk_type == "TK_SPACE":
                continue
            elif tk_type == "TK_MISMATCH":
                LexicalError(line, column, lexeme, "Token inválido.")
                continue

            yield Token(tk_type, lexeme, line, column)


def main():
    content = flags(argv)
    lexico = LexicalAnalyser(content).generate_token()
    print("\n-------------------|TOKENS|-------------------")
    print("( TOKEN, LEXEMA, LINHA, COLUNA )")
    for token in lexico:
        print(f"( {token.type}, {token.value}, {token.line}, {token.col} )")

main()