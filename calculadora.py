"""Calculadora financeira interativa para operações básicas no terminal."""


def calcula_valor_compra():
    """Solicita preço e quantidade e exibe o valor total da compra."""
    valor = float(input('Informe o valor do item: '))
    quantidade = int(input('Informe a quantidade comprada: '))

    compra = lambda valor, quantidade: valor * quantidade
    total = compra(valor, quantidade)

    print('\n', f'O total da compra é de: R$ {total:.2f}')


def calcula_desconto():
    """Solicita preço e desconto percentual e exibe o preço final."""
    valor = float(input('Informe o valor do item: '))
    desconto = float(input('Informe o valor do desconto: '))

    desconto_calculado = lambda valor, desconto: valor * (desconto / 100)

    total = desconto_calculado(valor, desconto)
    valor_com_desconto = valor - total

    print('\n', f'O total com o desconto é de: R$ {valor_com_desconto:.2f}')


def calcula_aumento():
    """Solicita preço e aumento percentual e exibe o preço reajustado."""
    valor = float(input('Informe o valor do item: '))
    aumento = float(input('Informe o valor do aumento: '))

    aumento_calculado = lambda valor, aumento: valor * (aumento / 100)

    total = aumento_calculado(valor, aumento)
    valor_com_aumento = valor + total

    print('\n', f'O total com o aumento é de: R$ {valor_com_aumento:.2f}')


def calcula_lucro():
    """Solicita custo e preço de venda e informa lucro ou prejuízo."""
    custo_producao = float(input('Informe o custo de produção: '))
    valor_venda = float(input('Informe o valor de venda: '))

    calcula_lucro = lambda custo_producao, valor_venda: valor_venda - custo_producao

    total = calcula_lucro(custo_producao, valor_venda)

    if total < 0:
        print('\n', f'O prejuízo da venda foi de R$ {abs(total):.2f}')
    else:
        print('\n', f'O lucro da venda foi de R$ {total:.2f}')


def calcula_margem_lucro():
    """Calcula e exibe a margem sobre o preço de venda, em porcentagem."""
    custo_producao = float(input('Informe o custo de produção: '))
    valor_venda = float(input('Informe o valor de venda: '))

    calcula_margem_lucro = lambda custo_producao, valor_venda: (
        (valor_venda - custo_producao) / valor_venda
    ) * 100

    total_margem_lucro = calcula_margem_lucro(custo_producao, valor_venda)

    if total_margem_lucro < 0:
        print('\n', f'Prejuízo de {abs(total_margem_lucro):.2f}%')
    else:
        print('\n', f'Lucro de {total_margem_lucro:.2f}%')


def somar_despesas(*despesas: float):
    """Soma valores de despesas recebidos como argumentos e exibe o total."""
    total = 0

    for despesa in despesas:
        total += despesa

    print('\n', f'O valor total de suas despesas é de R$ {total:.2f}')


def resumo_financeiro():
    """Solicita receitas e despesas e exibe o saldo financeiro."""
    receitas = float(input('Informe sua receita: '))
    despesas = float(input('Informe suas despesas: '))

    saldo = receitas - despesas

    print(f'''
    ===== RESUMO FINANCEIRO =====

    Receita: R$ {receitas:.2f}
    Despesas: R$ {despesas:.2f}
    Saldo: R$ {saldo:.2f}
    ''')


def menu():
    """Exibe o menu interativo e executa a operação selecionada."""

    opcao = -1

    while opcao != 0:

        print('''
        ===== CALCULADORA FINANCEIRA =====

        1 - Calcular valor de uma compra
        2 - Calcular desconto
        3 - Calcular aumento
        4 - Calcular lucro
        5 - Calcular margem de lucro
        6 - Somar várias despesas
        7 - Gerar resumo financeiro
        0 - Sair
        ''')

        try:

            opcao = int(input('Informe a opção: '))

            if opcao == 1:
                calcula_valor_compra()

            elif opcao == 2:
                calcula_desconto()

            elif opcao == 3:
                calcula_aumento()

            elif opcao == 4:
                calcula_lucro()

            elif opcao == 5:
                calcula_margem_lucro()

            elif opcao == 6:

                quantidade_despesas = int(
                    input('QUANTAS DESPESAS DESEJA INFORMAR? ')
                )

                despesas = []

                for i in range(quantidade_despesas):

                    valor = float(
                        input(f'Informe a despesa {i + 1}: ')
                    )

                    despesas.append(valor)

                somar_despesas(*despesas)

            elif opcao == 7:
                resumo_financeiro()

            elif opcao < 0 or opcao > 7:
                print('Número inválido')

            else:
                print('\nPrograma finalizado')

        except ValueError:
            print('Informe uma das opções acima')


if __name__ == '__main__':
    menu()    
