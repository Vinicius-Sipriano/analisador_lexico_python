from sys import argv
from receiveFlags import flags
from typing import NamedTuple
from enum import Enum
import re

class Tokens(Enum):
    TK_INT = 1
    TK_FLOAT = 2
    TK_IF = 3
    TK_ELSE = 4
    TK_WHILE = 5
    TK_RETURN = 6
    TK_PRINT = 7
    TK_ID = 8
    TK_NUM = 9
    TK_ATRIB = 10
    TK_PLUS = 11
    TK_MINUS = 12
    TK_MULTIPLY = 13
    TK_DIVIDE = 14
    TK_EQUALTY = 15
    TK_INEQUALTY = 16
    TK_LESS = 17
    TK_GREATER = 18
    TK_LESS_OR_EQUAL = 19
    TK_GREATER_OR_EQUAL = 20
    TK_OPEN_PAREN = 21
    TK_CLOSE_PAREN = 22
    TK_OPEN_BRACE = 23
    TK_CLOSE_BRACE = 24
    TK_COMMA = 25
    TK_SEMICOLON = 26
    TK_PERIOD = 30
    TK_NEW_LINE = 31
    TK_SPACE = 32
    TK_MISMATCH = 33

  
    TK_COMMENT_LINE = 34
    TK_COMMENT_BLOCK = 35

class LexicalError:

    def __init__(self, line, lex, mesg):
        self.line = line
        self.lex = lex
        self.mesg = mesg
        self.print_error()

    def print_error(self):
        print("\n-------------------|ERRO|-------------------")
        print(f"Erro léxico na linha {self.line}")
        print(f"  {self.lex}")
        print(f"  {self.mesg}")
        print("----------------------------------------------")

class Token(NamedTuple):
    code: int
    value: str
    line: int

class LexicalAnalyser:

    def __init__(self, source_code):
        self.__source_code = source_code

        self.__token_pair = [
            (Tokens.TK_INT.name, r"int\b"),
            (Tokens.TK_FLOAT.name, r"float\b"),
            (Tokens.TK_IF.name, r"if\b"),
            (Tokens.TK_ELSE.name, r"else\b"),
            (Tokens.TK_WHILE.name, r"while\b"),
            (Tokens.TK_RETURN.name, r"return\b"),
            (Tokens.TK_PRINT.name, r"print\b"),

          
            (Tokens.TK_ID.name, r"[a-zA-Z][a-zA-Z0-9]{0,9}"),

            
            (Tokens.TK_NUM.name, r"\b(0|[1-9]\d{0,2})(\.\d{1,2})?\b"),

            
            ("TK_COMMENT_LINE", r"//.*"),
            ("TK_COMMENT_BLOCK", r"/\*[\s\S]*?\*/"),

            (Tokens.TK_ATRIB.name, r"="),
            (Tokens.TK_PLUS.name, r"\+"),
            (Tokens.TK_MINUS.name, r"\-"),
            (Tokens.TK_MULTIPLY.name, r"\*"),
            (Tokens.TK_DIVIDE.name, r"\/"),
            (Tokens.TK_EQUALTY.name, r"\=="),
            (Tokens.TK_INEQUALTY.name, r"\!="),
            (Tokens.TK_LESS.name, r"\<"),
            (Tokens.TK_GREATER.name, r"\>"),
            (Tokens.TK_LESS_OR_EQUAL.name, r"\<="),
            (Tokens.TK_GREATER_OR_EQUAL.name, r"\>="),
            (Tokens.TK_OPEN_PAREN.name, r"\("),
            (Tokens.TK_CLOSE_PAREN.name, r"\)"),
            (Tokens.TK_OPEN_BRACE.name, r"\{"),
            (Tokens.TK_CLOSE_BRACE.name, r"\}"),
            (Tokens.TK_COMMA.name, r","),
            (Tokens.TK_SEMICOLON.name, r";"),
            (Tokens.TK_PERIOD.name, r"\."),
            (Tokens.TK_NEW_LINE.name, r"\r?\n"),
            (Tokens.TK_SPACE.name, r"[ \t]+"),
            (Tokens.TK_MISMATCH.name, r".")
        ]

        self.__keywords_map = {
            "int": Tokens.TK_INT.name,
            "float": Tokens.TK_FLOAT.name,
            "if": Tokens.TK_IF.name,
            "else": Tokens.TK_ELSE.name,
            "while": Tokens.TK_WHILE.name,
            "return": Tokens.TK_RETURN.name,
            "print": Tokens.TK_PRINT.name,
        }

    def generate_token(self):

        token_base = self.__token_pair
        buffer = self.__source_code

        regex_rules = "|".join("(?P<%s>%s)" % strPair for strPair in token_base)
        line = 1

        for matchedPattern in re.finditer(regex_rules, buffer):
            tk_type = matchedPattern.lastgroup
            lexeme = matchedPattern.group()

            if tk_type == Tokens.TK_NUM.name:
                if "." in lexeme:
                    lexeme = float(lexeme)
                else:
                    lexeme = int(lexeme)

            elif tk_type == Tokens.TK_ID.name and lexeme.lower() in self.__keywords_map:
                tk_type = self.__keywords_map[lexeme.lower()]

            
            elif tk_type in ["TK_COMMENT_LINE", "TK_COMMENT_BLOCK"]:
                yield Token(Tokens[tk_type].value, lexeme, line)
                continue

            elif tk_type == Tokens.TK_NEW_LINE.name:
                line += 1
                continue

            elif tk_type == Tokens.TK_SPACE.name:
                continue

            elif tk_type == Tokens.TK_MISMATCH.name:
                LexicalError(line, lexeme, "Token inválido.")
                continue

            yield Token(Tokens[tk_type].value, lexeme, line)


def main():
    content = flags(argv)
    lexico = LexicalAnalyser(content).generate_token()
    print("\n-------------------|TOKENS|-------------------")
    print(f"{'Token':<15}{'Lexema':<20}{'Linha':<10}")
    print("-" * 45)
    for token in lexico:
        print(f"{token.code:<15}{token.value:<20}{token.line:<10}")

main()
