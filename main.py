"""
Sistema de Gestão de Peças Industrial
Desenvolvido para controle de qualidade e armazenamento de peças

Autor: Sistema de Automação Digital
Disciplina: Algoritmos e Lógica de Programação
"""

from management_system import ManagementSystem


def exibir_menu():
    """Exibe o menu principal do sistema"""
    print("\n" + "="*80)
    print("SISTEMA DE GESTÃO DE PEÇAS INDUSTRIAL")
    print("="*80)
    print("\n1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair")
    print("\n" + "="*80)


def obter_entrada_numerica(mensagem, tipo=float, minimo=None, maximo=None):
    """Obtém entrada numérica do usuário com validação"""
    while True:
        try:
            valor = tipo(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"✗ Valor deve ser maior ou igual a {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"✗ Valor deve ser menor ou igual a {maximo}")
                continue
            return valor
        except ValueError:
            print(f"✗ Entrada inválida! Digite um número válido.")


def main():
    """Função principal do programa"""
    system = ManagementSystem()

    print("\n" + "="*80)
    print("BEM-VINDO AO SISTEMA DE GESTÃO DE PEÇAS INDUSTRIAL")
    print("="*80)
    print("\nSistema de automação para controle de qualidade e armazenamento")

    while True:
        exibir_menu()

        try:
            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "1":
                # Cadastrar nova peça
                print("\n--- CADASTRO DE NOVA PEÇA ---")
                peso = obter_entrada_numerica("Digite o peso (g): ", float, 0)
                cor = input("Digite a cor: ").strip()
                comprimento = obter_entrada_numerica("Digite o comprimento (cm): ", float, 0)

                system.register_part(peso, cor, comprimento)

            elif opcao == "2":
                # Listar peças
                print("\n--- LISTAGEM DE PEÇAS ---")
                print("\n1. Listar peças aprovadas")
                print("2. Listar peças reprovadas")
                print("3. Listar ambas")

                sub_opcao = input("\nEscolha uma opção: ").strip()

                if sub_opcao == "1":
                    system.list_approved_parts()
                elif sub_opcao == "2":
                    system.list_rejected_parts()
                elif sub_opcao == "3":
                    system.list_approved_parts()
                    system.list_rejected_parts()
                else:
                    print("✗ Opção inválida!")

            elif opcao == "3":
                # Remover peça
                print("\n--- REMOÇÃO DE PEÇA ---")
                id_peca = obter_entrada_numerica("Digite o ID da peça a remover: ", int, 1)
                system.remove_part(id_peca)

            elif opcao == "4":
                # Listar caixas fechadas
                system.list_boxes()

            elif opcao == "5":
                # Gerar relatório
                system.generate_report()

            elif opcao == "0":
                # Sair
                print("\n" + "="*80)
                print("ENCERRANDO SISTEMA...")
                system.generate_report()
                print("\nObrigado por usar o Sistema de Gestão de Peças Industrial!")
                print("="*80 + "\n")
                break

            else:
                print("\n✗ Opção inválida! Escolha uma opção entre 0 e 5.")

        except KeyboardInterrupt:
            print("\n\n✗ Operação cancelada pelo usuário.")
            print("Encerrando sistema...")
            break
        except Exception as e:
            print(f"\n✗ Erro inesperado: {e}")
            print("Por favor, tente novamente.")


if __name__ == "__main__":
    main()
