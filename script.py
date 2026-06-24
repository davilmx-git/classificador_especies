# Classificador de Espécies de Peixes da Bacia Amazônica

peixes = [
    {
        "nome": "tambaqui",
        "peso_medio": 30,
        "habitat": "rios e lagos de várzea",
        "piracema": "novembro a março"
    },
    {
        "nome": "pirarucu",
        "peso_medio": 100,
        "habitat": "lagos e rios de águas calmas",
        "piracema": "dezembro a maio"
    },
    {
        "nome": "tucunaré",
        "peso_medio": 8,
        "habitat": "rios, lagos e igarapés",
        "piracema": "setembro a dezembro"
    },
    {
        "nome": "jaraqui",
        "peso_medio": 1,
        "habitat": "rios de água branca",
        "piracema": "novembro a março"
    }
]


def classificar_porte(peso):
    if peso <= 2:
        return "Pequeno"
    else:
        if peso <= 20:
            return "Médio"
        else:
            return "Grande"


def cadastrar_especie():
    nome = input("Digite o nome da espécie: ")
    peso_medio = float(input("Digite o peso médio em kg: "))
    habitat = input("Digite o habitat: ")
    piracema = input("Digite o período de piracema: ")

    novo_peixe = {
        "nome": nome.lower(),
        "peso_medio": peso_medio,
        "habitat": habitat,
        "piracema": piracema
    }

    peixes.append(novo_peixe)

    print("\nEspécie cadastrada com sucesso!")


def buscar_por_nome():
    nome_busca = input("Digite o nome da espécie que deseja buscar: ").lower()

    encontrado = False

    for peixe in peixes:
        if peixe["nome"] == nome_busca:
            mostrar_peixe(peixe)
            encontrado = True

    if encontrado == False:
        print("\nEspécie não encontrada.")


def filtrar_por_piracema():
    periodo = input("Digite o mês ou período de piracema: ").lower()

    encontrados = []

    for peixe in peixes:
        if periodo in peixe["piracema"].lower():
            encontrados.append(peixe)

    if len(encontrados) > 0:
        print("\nEspécies encontradas nesse período:")
        for peixe in encontrados:
            mostrar_peixe(peixe)
    else:
        print("\nNenhuma espécie encontrada nesse período.")


def mostrar_peixe(peixe):
    porte = classificar_porte(peixe["peso_medio"])

    print("\n--- Dados da Espécie ---")
    print(f"Nome: {peixe['nome'].title()}")
    print(f"Peso médio: {peixe['peso_medio']} kg")
    print(f"Classificação: Peixe {porte}")
    print(f"Habitat: {peixe['habitat']}")
    print(f"Período de piracema: {peixe['piracema']}")


def listar_todos():
    print("\n===== ESPÉCIES CADASTRADAS =====")

    for peixe in peixes:
        mostrar_peixe(peixe)


def calcular_estatisticas():
    soma_pesos = 0
    peixe_mais_pesado = peixes[0]

    for peixe in peixes:
        soma_pesos += peixe["peso_medio"]

        if peixe["peso_medio"] > peixe_mais_pesado["peso_medio"]:
            peixe_mais_pesado = peixe

    media = soma_pesos / len(peixes)

    print("\n===== ESTATÍSTICAS =====")
    print(f"Quantidade de espécies cadastradas: {len(peixes)}")
    print(f"Peso médio geral: {media:.2f} kg")
    print(f"Espécie mais pesada: {peixe_mais_pesado['nome'].title()}")
    print(f"Peso médio da espécie mais pesada: {peixe_mais_pesado['peso_medio']} kg")
    print(f"Classificação: Peixe {classificar_porte(peixe_mais_pesado['peso_medio'])}")


while True:
    print("\n===== CLASSIFICADOR DE PEIXES AMAZÔNICOS =====")
    print("1 - Cadastrar nova espécie")
    print("2 - Buscar espécie por nome")
    print("3 - Filtrar por período de piracema")
    print("4 - Listar todas as espécies")
    print("5 - Calcular estatísticas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_especie()

    elif opcao == "2":
        buscar_por_nome()

    elif opcao == "3":
        filtrar_por_piracema()

    elif opcao == "4":
        listar_todos()

    elif opcao == "5":
        calcular_estatisticas()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
