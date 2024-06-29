# Função para exibir o menu
def exibir_menu():
    print("1. Adicionar produtos")
    print("2. Exibir produtos")
    print("3. Sair")

# Função para adicionar um novo cadastro
def adicionar_cadastro(cadastros):
    nome = input("Digite o nome: ")
    descricao = input("Digite a descrição: ")
    valor = input("Digite o valor: ").replace(',', '.')
    
    try:
        valor = float(valor)
    except ValueError:
        print("Valor inválido! Tente novamente.")
        return
    
    disponivel_input = input("Produto disponível (sim/não)? ").strip().lower()
    disponivel = True if disponivel_input == 'sim' else False
    
    cadastro = {
        "nome": nome,
        "descricao": descricao,
        "valor": valor,
        "disponivel": disponivel
    }
    
    cadastros.append(cadastro)
    print("Produto adicionado com sucesso!\n")
    exibir_cadastros(cadastros)  # Exibe a listagem automaticamente após o cadastro

# Função para exibir todos os cadastros
def exibir_cadastros(cadastros):
    if not cadastros:
        print("Nenhum cadastro encontrado.\n")
    else:
        # Ordena os cadastros pelo valor do produto
        cadastros_ordenados = sorted(cadastros, key=lambda x: x['valor'])
        print("𝐋𝐢𝐬𝐭𝐚𝐠𝐞𝐦:")
        for i, cadastro in enumerate(cadastros_ordenados):
            print(f"Cadastro {i + 1}:")
            print(f"Nome do produto: {cadastro['nome']}")
            print(f"Valor do produto: {cadastro['valor']:.2f}")
            print()

        print("4. Adicionar novo produto")
        opcao = input("Escolha uma opção: ")

        if opcao == "4":
            adicionar_cadastro(cadastros)
        else:
            print("Opção inválida. Retornando ao menu principal.\n")

def main():
    cadastros = []
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_cadastro(cadastros)
        elif opcao == "2":
            exibir_cadastros(cadastros)
        elif opcao == "3":
            print("Saindo do programa")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
