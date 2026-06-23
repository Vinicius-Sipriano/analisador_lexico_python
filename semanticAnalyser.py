class SemanticError(Exception):
    pass

class SemanticAnalyser:
    def __init__(self):
        self.symbol_table = {}
        self.scopes = []
        self.current_function_stack = []
        self.declared_symbols = []

    def enter_scope(self, scope_name=None):
        self.scopes.append({
            'name': scope_name,
            'symbols': {}
        })
        self.show_symbol_table()

    def exit_scope(self):
        if not self.scopes:
            raise SemanticError("Escopo inválido: tentativa de sair de um escopo inexistente.")
        self.scopes.pop()
        self.show_symbol_table()

    def current_scope(self):
        return self.scopes[-1] if self.scopes else None

    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope['symbols']:
                return scope['symbols'][name]
        self.show_symbol_table()
        return self.symbol_table.get(name)

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
        self.current_function_stack.append(name)
        self.enter_scope(name)
        self.declared_symbols.append({
            'name': name,
            'tipo': idType,
            'linha': line,
            'categoria': 'função',
            'escopo': 'global'
        })
        self.show_symbol_table()
        return True

    def register_param(self, name, idType, line):
        current = self.current_scope()
        if current is None:
            raise SemanticError(
                f"Linha {line}: parâmetro '{name}' declarado fora de um escopo válido."
            )

        if name in current['symbols']:
            raise SemanticError(
                f"Linha {line}: o identificador '{name}' já foi declarado neste escopo."
            )

        current['symbols'][name] = {
            'tipo': idType,
            'linha': line,
            'categoria': 'parâmetro'
        }
        self.declared_symbols.append({
            'name': name,
            'tipo': idType,
            'linha': line,
            'categoria': 'parâmetro',
            'escopo': current['name']
        })
        self.show_symbol_table()

    def register_variable(self, name, idType, line):
        current = self.current_scope()
        if current is None:
            raise SemanticError(
                f"Linha {line}: variável '{name}' declarada fora de um escopo válido."
            )

        if name in current['symbols']:
            raise SemanticError(
                f"Linha {line}: o identificador '{name}' já foi declarado neste escopo."
            )

        current['symbols'][name] = {
            'tipo': idType,
            'linha': line,
            'categoria': 'variável'
        }
        self.declared_symbols.append({
            'name': name,
            'tipo': idType,
            'linha': line,
            'categoria': 'variável',
            'escopo': current['name']
        })
        self.show_symbol_table()

    def get_symbol_type(self, name, line):
        symbol = self.lookup(name)
        if symbol is None:
            raise SemanticError(
                f"Linha {line}: identificador '{name}' não foi declarado."
            )
        self.show_symbol_table()
        return symbol.get('tipo') or symbol.get('tipo_retorno')

    def check_assignment(self, name, expr_type, line):
        declared_type = self.get_symbol_type(name, line)
        if not self.types_compatible(expr_type, declared_type):
            raise SemanticError(
                f"Linha {line}: tipo incompatível na atribuição para '{name}'. "
                f"Esperado '{declared_type}', encontrado '{expr_type}'."
            )
        self.show_symbol_table()

    def check_return(self, expr_type, line):
        if not self.current_function_stack:
            raise SemanticError(
                f"Linha {line}: retorno declarado fora de uma função."
            )
        current_function = self.current_function_stack[-1]
        expected_type = self.symbol_table[current_function]['tipo_retorno']
        if not self.types_compatible(expr_type, expected_type):
            raise SemanticError(
                f"Linha {line}: tipo de retorno incompatível para a função "
                f"'{current_function}'. Esperado '{expected_type}', encontrado '{expr_type}'."
            )
        self.show_symbol_table()

    def end_function(self):
        if not self.current_function_stack:
            raise SemanticError("Interno: tentativa de finalizar função inexistente.")
        self.current_function_stack.pop()
        self.exit_scope()
        self.show_symbol_table()

    def types_compatible(self, source_type, target_type):
        if source_type == target_type:
            return True
        if source_type == 'int' and target_type == 'float':
            return True
        return False

    def evaluate_arithmetic(self, left_type, right_type, operator, line):
        if left_type == 'bool' or right_type == 'bool':
            raise SemanticError(
                f"Linha {line}: operação aritmética inválida entre tipos "
                f"'{left_type}' e '{right_type}'."
            )
        if left_type == 'float' or right_type == 'float':
            return 'float'
        if left_type == 'int' and right_type == 'int':
            return 'int'
        raise SemanticError(
            f"Linha {line}: tipos incompatíveis na operação '{operator}': "
            f"'{left_type}' e '{right_type}'."
        )

    def evaluate_relational(self, left_type, right_type, operator, line):
        if left_type == 'bool' or right_type == 'bool':
            raise SemanticError(
                f"Linha {line}: operação relacional inválida entre tipos "
                f"'{left_type}' e '{right_type}'."
            )
        if left_type in ('int', 'float') and right_type in ('int', 'float'):
            return 'bool'
        raise SemanticError(
            f"Linha {line}: tipos incompatíveis na operação '{operator}': "
            f"'{left_type}' e '{right_type}'."
        )

    def show_symbol_table(self):
        print("\n--- TABELA DE SÍMBOLOS MODIFICADA ---")
        if not self.symbol_table and not self.declared_symbols:
            print("Tabela vazia.")
        if self.symbol_table:
            print("Funções:")
            for name, info in self.symbol_table.items():
                print(f"  Função: {name:<10} | Tipo Retorno: {info['tipo_retorno']:<6} | Linha: {info['linha']}")
        if self.declared_symbols:
            print("Identificadores declarados:")
            for symbol in self.declared_symbols:
                print(
                    f"  {symbol['categoria'].capitalize():<10}: {symbol['name']:<10} "
                    f"| Tipo: {symbol['tipo']:<6} | Escopo: {symbol['escopo']} | Linha: {symbol['linha']}"
                )
        print("-------------------------------------\n")