import json
import os

class AgilStore:
    def __init__(self):
        self.inventario = {}
        self.carregar_dados()

    def carregar_dados(self):
        if os.path.exists('inventario.json'):
            with open('inventario.json', 'r') as file:
                self.inventario = json.load(file)
        else:
            self.inventario = {}

    def salvar_dados(self):
        with open('inventario.json', 'w') as file:
            json.dump(self.inventario, file, indent=4)

    def adicionar_produto(self, nome, categoria, quantidade, preco):
        produto_id = len(self.inventario) + 1
        self.inventario[produto_id] = {
            'nome': nome,
            'categoria': categoria,
            'quantidade': quantidade,
            'preco': preco
        }
        self.salvar_dados()

    def listar_produtos(self):
        print(f"{'ID':<5}{'Nome':<20}{'Categoria':<20}{'Quantidade':<10}{'Preço':<10}")
        for produto_id, produto in self.inventario.items():
            print(f"{produto_id:<5}{produto['nome']:<20}{produto['categoria']:<20}{produto['quantidade']:<10}{produto['preco']:<10}")

    def atualizar_produto(self, produto_id, nome=None, categoria=None, quantidade=None, preco=None):
        if produto_id in self.inventario:
            if nome:
                self.inventario[produto_id]['nome'] = nome
            if categoria:
                self.inventario[produto_id]['categoria'] = categoria
            if quantidade:
                self.inventario[produto_id]['quantidade'] = quantidade
            if preco:
                self.inventario[produto_id]['preco'] = preco
            self.salvar_dados()
        else:
            print("Produto não encontrado.")

    def excluir_produto(self, produto_id):
        if produto_id in self.inventario:
            del self.inventario[produto_id]
            self.salvar_dados()
        else:
            print("Produto não encontrado.")

    def buscar_produto(self, termo):
        resultados = []
        for produto_id, produto in self.inventario.items():
            if termo.lower() in produto['nome'].lower() or str(produto_id) == termo:
                resultados.append((produto_id, produto))
        return resultados

def main():
    loja = AgilStore()
    while True:
        print("\n1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Buscar Produto")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do Produto: ")
            categoria = input("Categoria: ")
            quantidade = int(input("Quantidade em Estoque: "))
            preco = float(input("Preço: "))
            loja.adicionar_produto(nome, categoria, quantidade, preco)
        elif opcao == '2':
            loja.listar_produtos()
        elif opcao == '3':
            produto_id = int(input("ID do Produto a ser atualizado: "))
            nome = input("Novo Nome (ou Enter para manter): ")
            categoria = input("Nova Categoria (ou Enter para manter): ")
            quantidade = input("Nova Quantidade (ou Enter para manter): ")
            preco = input("Novo Preço (ou Enter para manter): ")
            loja.atualizar_produto(produto_id, nome or None, categoria or None, int(quantidade) if quantidade else None, float(preco) if preco else None)
        elif opcao == '4':
            produto_id = int(input("ID do Produto a ser excluído: "))
            loja.excluir_produto(produto_id)
        elif opcao == '5':
            termo = input("ID ou Nome do Produto: ")
            resultados = loja.buscar_produto(termo)
            if resultados:
                for produto_id, produto in resultados:
                    print(f"ID: {produto_id}, Nome: {produto['nome']}, Categoria: {produto['categoria']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']}")
            else:
                print("Produto não encontrado.")
        elif opcao == '6':
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
