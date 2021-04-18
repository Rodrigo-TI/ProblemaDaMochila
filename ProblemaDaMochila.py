import random
from deap import creator, base, tools, algorithms
# individuo
creator.create("Fitness", base.Fitness, weights=(-1.0, 1.0))
creator.create("Individual", set, fitness=creator.Fitness)
# variaveis
qtd_populacao = 50
indice_inicial = 0
capMaxMochila = 100
qtd_itens = 0
mochila = []
for i in range(qtd_itens):
    peso = random.randint(1, 100)
    valor = random.randint(1, 10)
    mochila[i] = (peso, valor)
# adicionando as funcionalidades
toolbox = base.Toolbox()
toolbox.register("atributo", random.randrange, qtd_itens)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.atributo, indice_inicial)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
# avaliacao
def avaliacao(individual):
    pesoTotal = 0.0
    valorTotal = 0.0
    for item in individual:
        pesoTotal += mochila[item][0]
        valorTotal += mochila[item][1]
    if pesoTotal > capMaxMochila:
        return -1
    return pesoTotal, valorTotal
# crossover
def crossover(individual1, individual2):
    temp = set(individual1)
    individual1 &= individual2
    individual2 ^= temp
    return individual1, individual2
def mutacao(individual):
    if random.random() < 0.5:
        if len(individual) > 0:
            individual.remove(random.choice(sorted(tuple(individual))))
    else:
        individual.add(random.randrange(qtd_itens))
    return individual
# adicionando as funcionalidades
toolbox.register("evaluate", avaliacao)
toolbox.register("mate", crossover)
toolbox.register("mutate", mutacao)
toolbox.register("select", tools.selNSGA2)
# criando a populacao
populacao = toolbox.population(n=qtd_populacao)