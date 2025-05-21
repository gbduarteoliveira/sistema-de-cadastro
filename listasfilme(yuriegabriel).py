from collections import Counter


generos = []
titulos = []
anos = []
notas = []
avaliacao = []


def cadastrar_filme():
    titulo = input("Digite o Título: ").strip().title()
    genero = input("Qual o Gênero: ").strip().capitalize()

    try:
        ano = int(input("Ano: "))
    except ValueError:
        print("Ano inválido. Deve ser um número inteiro.")
        return

    try:
        nota_input = float(input("Nota (0 a 10): "))
    except ValueError:
        print("Nota inválida")
        return

    notas_avaliacao = classificar_nota(nota_input)

    titulos.append(titulo)
    generos.append(genero)
    anos.append(ano)
    notas.append(nota_input)
    avaliacao.append(notas_avaliacao)

    print("Filme cadastrado com sucesso!")


def classificar_nota(nota):
    if nota < 0 or nota > 10:
        return 'Nota inválida (deve estar entre 0 e 10)'
    elif nota >= 7:
        return 'Bom'
    elif nota >= 6:
        return 'Regular'
    else:
        return 'Ruim'


def listar_filmes():
    if len(titulos) == 0:
        print("Nenhum filme cadastrado.")
        return

    print("--- Filmes Cadastrados ---")
    for i in range(len(titulos)):
        print(f"Filme {i + 1}:")
        print(f"  Título: {titulos[i]}")
        print(f"  Gênero: {generos[i]}")
        print(f"  Ano: {anos[i]}")
        print(f"  Nota: {notas[i]}")
        print(f"  Avaliação: {avaliacao[i]}")
    print()


def buscar_filmes():
    if not titulos:
        print("Nenhum filme cadastrado para buscar.")
        return

    titulo_buscado = input("Digite o título do filme: ").lower()
    encontrou_filme = False

    for i in range(len(titulos)):
        if titulo_buscado in titulos[i].lower():
            print(f" Filme encontrado:")
            print(f"  Título: {titulos[i]}")
            print(f"  Gênero: {generos[i]}")
            print(f"  Ano: {anos[i]}")
            print(f"  Nota: {notas[i]}")
            print(f"  Avaliação: {avaliacao[i]}")
            encontrou_filme = True

    if not encontrou_filme:
        print(" Nenhum filme encontrado com esse título.")


def exibir_filmes_individualmente():
    if not titulos:
        print("Nenhum filme cadastrado para exibir.")
        return

    print(" Filmes Cadastrados:")
    for i in range(len(titulos)):
        print(f"Filme {i + 1}:")
        print(f"  Título: {titulos[i]}")
        print(f"  Gênero: {generos[i]}")
        print(f"  Ano: {anos[i]}")
        print(f"  Nota: {notas[i]}")
        print(f"  Avaliação: {avaliacao[i]}")


def remover_filmes():
    if not titulos:
        print("Nenhum filme cadastrado para remover.")
        return

    titulo_remover = input(
        "Digite o título do filme a ser removido: ").strip().lower()
    encontrou_filme = False

    for i in range(len(titulos)):
        if titulo_remover in titulos[i].lower():
            print(f"\nFilme encontrado para remoção:")
            print(f"  Título: {titulos[i]}")
            print(f"  Gênero: {generos[i]}")
            print(f"  Ano: {anos[i]}")
            print(f"  Nota: {notas[i]}")
            print(f"  Avaliação: {avaliacao[i]}")

            confirmar = input(
                "Deseja realmente remover este filme? (sim/não): ").lower()
            if confirmar == "sim":
                filme_removido = titulos[i]
                titulos.pop(i)
                generos.pop(i)
                anos.pop(i)
                notas.pop(i)
                avaliacao.pop(i)
                print(f"Filme '{filme_removido}' removido com sucesso!")
                encontrou_filme = True
                break
            else:
                print("A remoção foi cancelada.")
                return

    if not encontrou_filme:
        print(f"Nenhum filme encontrado com o título '{titulo_remover}'.")


def exibir_estatisticas():
    if not titulos:
        print("Nenhum filme cadastrado para estatísticas.")
        return

    print("\n--- Estatísticas dos Filmes ---")
    total = len(titulos)
    media_notas = sum(notas) / total

    contagem_generos = Counter(generos)
    maior_freq = max(contagem_generos.values())

    generos_mais_comuns = [genero for genero,
                           qtd in contagem_generos.items() if qtd == maior_freq]

    filmes_bons = [titulos[i] for i in range(len(notas)) if notas[i] >= 7]

    print(f"Quantidade total de filmes: {total}")
    print(f"Média das notas: {media_notas:.2f}")
    print("Gênero(s) mais cadastrado(s):")
    for genero in generos_mais_comuns:
        print(f"  - {genero} ({maior_freq} vezes)")

    print("Filmes com nota maior ou igual a 7:")
    for filme in filmes_bons:
        print(f"  - {filme}")
    print()


def exibir_menu():
    while True:
        print("--- Menu de Filmes ---")
        print("1. Cadastrar Filme")
        print("2. Listar Filmes")
        print("3. Buscar Filme")
        print("4. Exibir Filmes Individualmente")
        print("5. Remover Filme")
        print("6. Exibir Estatísticas")
        print("7. Sair")

        opcao = input("Escolha uma opção (1-7): ")

        if opcao == '1':
            cadastrar_filme()
        elif opcao == '2':
            listar_filmes()
        elif opcao == '3':
            buscar_filmes()
        elif opcao == '4':
            exibir_filmes_individualmente()
        elif opcao == '5':
            remover_filmes()
        elif opcao == '6':
            exibir_estatisticas()
        elif opcao == '7':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


exibir_menu()

# teste
