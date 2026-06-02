TOKEN      = {'a':1, 'b':2, 'c':3, 'î':4, '$':5, 'S':6, 'A':7, 'B':8}
TOKEN_NAME = {v: k for k, v in TOKEN.items()}

matrizParser = [
    [0, 0, 1, 0, 0],
    [3, 3, 2, 3, 0],
    [5, 4, 0, 5, 0],
]

matrizProd = [
    [3, 7, 1],
    [3, 8, 0],
    [8, 0, 0],
    [2, 3, 8],
    [4, 0, 0],
]

EPS      = TOKEN['î']
EOF      = TOKEN['$']
FIRST_NT = TOKEN['S']

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
                print("✓ Sentença ACEITA!")
                return True

            if X >= FIRST_NT:
                p = lookup(X, a)
                if p == 0:
                    print("✗ Erro sintático.")
                    return False
                pilha.pop()
                for sym in reversed(get_prod(p)):
                    pilha.append(sym)
            else:
                if X == a:
                    pilha.pop()
                    break
                else:
                    print(f"✗ Erro: '{TOKEN_NAME[X]}' ≠ '{TOKEN_NAME[a]}'")
                    return False

    print("✓ Sentença ACEITA!")
    return True

parse('cbcaa')