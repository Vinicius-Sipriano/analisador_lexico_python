# Analisador Léxico em Python

Este projeto implementa um analisador léxico simples em Python para reconhecer:

- palavras reservadas: `int`, `float`, `if`, `else`, `while`, `return` e `print`
- identificadores: `TK_ID`
- números inteiros e reais: `TK_NUM`
- operadores e símbolos: `=`, `+`, `-`, `*`, `/`, `==`, `!=`, `<`, `>`, `<=`, `>=`, `(`, `)`, `{`, `}`, `,` e `;`

## Requisitos

- Python 3 instalado

## Como executar

1. Crie um arquivo de entrada com o código-fonte da linguagem, por exemplo `exemplo.txt`.
2. Execute o analisador informando o arquivo como argumento:

```bash
python lexicalAnalyser.py exemplo.txt
```

## Saída esperada

O programa imprime os tokens encontrados no formato:

```txt
( TOKEN, LEXEMA, LINHA, COLUNA )
```

Quando houver um caractere inválido ou um identificador inválido, o analisador exibe uma mensagem de erro léxico indicando linha e coluna.