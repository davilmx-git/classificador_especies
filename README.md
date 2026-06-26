# Classificador de Espécies de Peixes da Bacia Amazônica

Projeto em Python para cadastro, busca, filtragem e análise de espécies de peixes amazônicos. O sistema usa uma lista de dicionários para armazenar os dados e um menu interativo para navegação.

## Objetivo

- Organizar informações sobre espécies de peixes da Amazônia.
- Permitir cadastro de novas espécies.
- Buscar espécies pelo nome.
- Filtrar espécies pelo período de piracema.
- Listar todos os peixes cadastrados.
- Gerar estatísticas gerais do conjunto de dados.


## Como o sistema funciona

O programa começa com uma lista chamada `peixes`, onde cada peixe possui nome, peso médio, habitat e piracema. Em seguida, o sistema apresenta um menu com opções numeradas para o usuário interagir com as funções do programa.

### Estrutura dos dados

Cada espécie é armazenada em um dicionário com os seguintes campos:

- `nome`
- `peso_medio`
- `habitat`
- `piracema`

Exemplos de espécies já cadastradas no código:

- tambaqui
- pirarucu
- tucunaré
- jaraqui.


## Funções do programa

### classificar_porte(peso)

Essa função recebe o peso médio do peixe e classifica o porte em:

- Pequeno
- Médio
- Grande.


### cadastrar_especie()

Permite adicionar uma nova espécie informando:

- nome
- peso médio
- habitat
- período de piracema

Depois disso, o novo peixe é inserido na lista `peixes`.

### buscar_por_nome()

Busca uma espécie pelo nome digitado pelo usuário.
Se encontrar, mostra os dados completos da espécie.
Se não encontrar, exibe a mensagem de espécie não localizada.

### filtrar_por_piracema()

Filtra as espécies de acordo com o mês ou período informado.
O programa percorre a lista e retorna os peixes cujo campo `piracema` contém o texto digitado.

### mostrar_peixe(peixe)

Exibe os dados organizados da espécie, incluindo:

- nome
- peso médio
- classificação do porte
- habitat
- período de piracema. 


### listar_todos()

Mostra todas as espécies cadastradas no sistema, uma por uma.

### calcular_estatisticas()

Calcula e exibe:

- quantidade de espécies cadastradas
- peso médio geral
- espécie mais pesada
- classificação da espécie mais pesada.


## Menu principal

O programa usa um laço `while True` para manter o sistema em execução até o usuário escolher sair. As opções do menu são:

- 1 - Cadastrar nova espécie
- 2 - Buscar espécie por nome
- 3 - Filtrar por período de piracema
- 4 - Listar todas as espécies
- 5 - Calcular estatísticas
- 0 - Sair.

## Exemplo de uso

1. O usuário escolhe uma opção no menu.
2. O programa executa a função correspondente.
3. Os dados são exibidos no terminal.
4. O processo continua até o usuário digitar `0` para encerrar.
## Tecnologias utilizadas

- Python
- Estruturas de repetição
- Condicionais
- Listas
- Dicionários
- Entrada de dados com `input()`.


## Organização da apresentação oral

### Integrante 1

- Introdução ao projeto.
- Objetivo do sistema.
- Estrutura dos dados.


### Integrante 2

- Explicação das funções de cadastro, busca e filtro.
- Explicação da função de classificação de porte.


### Integrante 3

- Listagem de espécies.
- Estatísticas.
- Explicação do menu principal e encerramento.


## Conclusão

O projeto mostra de forma prática como usar Python para organizar informações de peixes amazônicos. Além disso, trabalha conceitos importantes como listas, dicionários, funções, repetição e tomada de decisão.




Link: [Projeto Classificador](https://colab.research.google.com/drive/1rLrF375T5k_79MW8sCB-KiB7j4emrUQg?usp=sharing)
