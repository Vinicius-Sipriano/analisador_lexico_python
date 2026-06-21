class SemanticAnalyser:
    def __init__(self):
        self.symbol_table = {}

    def register_function(self, nome, tipo, linha):
        if nome in self.symbol_table:
            print(f"\n[ERRO SEMÂNTICO] Linha {linha}: A função '{nome}' já foi declarada anteriormente (primeira declaração na linha {self.symbol_table[nome]['linha']}).")
            return False
        
        self.symbol_table[nome] = {
            'tipo_retorno': tipo,
            'linha': linha,
            'escopo': 'global'
        }
        
        self.show_symbol_table()
        return True

    def show_symbol_table(self):
        print("\n--- TABELA DE SÍMBOLOS MODIFICADA ---")
        if not self.symbol_table:
            print("Tabela vazia.")
        for nome, info in self.symbol_table.items():
            print(f"Função: {nome:<10} | Tipo Retorno: {info['tipo_retorno']:<6} | Linha: {info['linha']}")
        print("-------------------------------------\n")