'''
Projeto: vendas
Cadastrar produtos com nome, preço e quantidade.
Listar todos os produtos cadastrados.
Atualizar o preço e a quantidade de um produto.
Realizar uma venda, atualizando a quantidade disponível.
Listar as vendas realizadas.

'''

# (_) antes de uma variavel = não usar fora da classe


class GerenciarProduto:
    def __init__(self) -> None:
        self._estoque = []
        self._vendas = []

    def _retornarDicionarioEstoque(self, item, price, qtd) -> dict:
        return {'item': item, 'preco': price, 'qtd': qtd}

    def _retornarDicionarioVendas(self, item, qtd):
        return {'item': item, 'qtd': qtd}

    def cadastro(self):  
        try:
            reg_item = input('Digite o nome do item que quer estocar: ')
            reg_preco = float(
                input('Digite o preço do item que quer estocar: '))
            reg_qtd = int(
                input('Digite a quantidade  do item que quer estocar: '))

            dicionario = self._retornarDicionarioEstoque(
                reg_item, reg_preco, reg_qtd)
            self._estoque.append(dicionario)
            print('Produto cadastrado com successo')

        except ValueError:
            print('Digite apenas numeros para preço ou quantidade')

    def venda(self):  
        reg_venda = input('Escolha o que vai ser comprado: ')
        qtd_venda = int(input('Escolha quanto foi vendido: '))

        for item in self._estoque:
            if item['item'] == reg_venda:
                if qtd_venda <= item['qtd']:
                    item['qtd'] -= qtd_venda
                    self._vendas.append(
                        self._retornarDicionarioVendas(reg_venda, qtd_venda))
                    print(f'Vendido pai: {qtd_venda} unidades de {reg_venda}')
                else:
                    print('Item insuficiente no estoque')
                break
        else:
            print('Produto não encontrado no estoque')

           
    def listar_estoque(self):  # feito
        if not self._estoque:
            print('Estoque vazio.')
        else:
            for item in self._estoque:
                print(f'Nome: {item["item"]} |\
Preço: {item["preco"]} | Quantidade: {item["qtd"]}')

    def listar_vendas(self):
        if not self._vendas:
            print('Nenhuma venda realizada.')
        else:
            for item in self._vendas:
                print(f'Produto: {item["item"]} | Quantidade: {item["qtd"]}')

    def atualizar(self):
        itens_atlz = input('Nome do produto que deseja atualizar: ')

        for atlz in self._estoque:
            if atlz['item'] == itens_atlz:
                try:
                    novo_preco = float(input('Digite o novo preço: '))
                    nova_qtd = int(input('Digite a nova quantidade: '))
                    atlz['preco'] = novo_preco
                    atlz['qtd'] = nova_qtd
                    print(f'Produto {itens_atlz}')

                except ValueError:
                    print('Digite apenas numeros para preço e quantidade. ')

                break
        else:
            print('Produto não encontrado')


def main():
    mercadinho_clandestino = GerenciarProduto()
    while True:
        opcoes = {
            '1': lambda: mercadinho_clandestino.cadastro(),
            '2': lambda: mercadinho_clandestino.venda(),
            '3': lambda: mercadinho_clandestino.atualizar(),
            '4': lambda: mercadinho_clandestino.listar_estoque(),
            '5': lambda: mercadinho_clandestino.listar_vendas(),
        }
        print('Opções: \n 1.Cadastrar Estoque \n 2.Vender \n 3.Atualizar \n 4.Listar Estoque \n 5.Listar Vendas ')
        entrada = input('Escolha uma opção: ')

        if entrada not in opcoes:
            print('Não, pare.')
        else:
            opcoes[entrada]()


if __name__ == '__main__':
    main()
