class SemanticError(Exception):
    pass

class SemanticAnalyser:
    def __init__(self):
        self.symbol_table = {}

    def register_function(self, name, idType, line):
        if name in self.symbol_table:
            raise SemanticError(
                f"Linha {line}: A função '{name}' já foi declarada anteriormente "
                f"(primeira declaração na linha {self.symbol_table[name]['linha']})."
                )

        self.symbol_table[name] = {
            'tipo_retorno': idType,
            'linha': line,
            'escopo': 'global'
        }
        
        self.show_symbol_table()
        return True

    def show_symbol_table(self):
        print("\n--- TABELA DE SÍMBOLOS MODIFICADA ---")
        if not self.symbol_table:
            print("Tabela vazia.")
        for name, info in self.symbol_table.items():
            print(f"Função: {name:<10} | Tipo Retorno: {info['tipo_retorno']:<6} | Linha: {info['linha']}")
        print("-------------------------------------\n")