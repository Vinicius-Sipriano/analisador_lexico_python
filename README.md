# Analisador Léxico e Sintático em Python

Este projeto implementa três componentes da frente de compilação:

- um analisador léxico para reconhecer os tokens da linguagem
- um analisador sintático LL(1) para validar a gramática codificada na tabela de parsing
- um analisador semântico para validar as ações semânticas da linguagem

## Requisitos

- Python 3 instalado

## Estrutura

- [lexicalAnalyser.py](lexicalAnalyser.py) faz a análise léxica e gera os tokens
- [syntacticAnalyser.py](syntacticAnalyser.py) consome os tokens do léxico e executa a análise sintática
- [semanticAnalyser.py](semanticAnalyser.py) faz a análise semântica através das ações semânticas
- [examples/](examples/) contém arquivos de teste para os três analisadores

## Analisador Léxico

O léxico reconhece:

- palavras reservadas: `int`, `float`, `if`, `else`, `while`, `return` e `print`
- identificadores: `TK_ID`
- números inteiros e reais: `TK_NUM`
- operadores e símbolos: `=`, `+`, `-`, `*`, `/`, `==`, `!=`, `<`, `>`, `<=`, `>=`, `(`, `)`, `{`, `}`, `,` e `;`

### Como executar o léxico

```bash
python lexicalAnalyser.py examples/example.txt
```

### Saída esperada do léxico

O programa imprime os tokens encontrados no formato:

```txt
( TOKEN, LEXEMA, LINHA)
```

Quando houver um caractere inválido ou um identificador inválido, o analisador exibe uma mensagem de erro léxico indicando linha e coluna.

## Analisador Sintático

O sintático foi implementado como um parser preditivo LL(1), usando:

- pilha de análise
- tabela de parsing codificada
- lista de produções da gramática

Ele recebe a saída do léxico internamente, então basta executar o arquivo sintático com um código-fonte de entrada válido para a gramática.

### Como executar o sintático

```bash
python syntacticAnalyser.py examples/example.txt
```

### Saída esperada do sintático

O programa imprime os tokens analisados no formato:

```txt
( TOKEN, LEXEMA, LINHA)
```

E ele mostra o processo da pilha a cada passo:

```txt
Pilha: [$ ...]
Ação: ...
```

Se a sentença estiver correta, o analisador imprime:

```txt
Sentença ACEITA!
```

Se houver erro sintático, o programa mostra uma mensagem amigável no formato:

```txt
Erro sintático (error de parser) em:
ParseError: Linha X: esperado ..., encontrado '...'
```

## Analisador Semântico

O semântico foi implementado usando uma tabela de símbolos

### Como executar o semântico

```bash
python syntacticAnalyser.py examples/example.txt
```

O semântico é executado através do syntacticAnalyser, sendo o semanticAnalyser para apoio ao código principal.

### Saída esperada do semântico

Ele atualiza a tabela de símbolos a cada mudança feita nela.

--- TABELA DE SÍMBOLOS MODIFICADA ---
Funções:
  Função:   | Tipo Retorno:   | Linha: 
Identificadores declarados:
  Função    :        | Tipo:     | Escopo:   | Linha: 
  Variável  :        | Tipo:     | Escopo:   | Linha:  
-------------------------------------

## Observação sobre os exemplos

- [examples/example.txt](examples/example.txt) é útil para testar o léxico, mas não pertence à gramática sintática atual
- [examples/example4.txt](examples/example4.txt) e [examples/example5.txt](examples/example5.txt) foram criados para testar o sintático
- O arquivo de entrada padrão pode ser alterado em [receiveFlags.py](receiveFlags.py)