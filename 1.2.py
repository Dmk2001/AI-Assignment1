import random

from matplotlib import pyplot as plt

target_string = "110010001101011001100010100110"


def init_population(population_size, string_length):
    generation = []
    for x in range(0, population_size):
        str = ""
        for _ in range(string_length):
            str += random.choice('01')
        generation.append(str)
    return generation


def avg_fitness(population):
    sum = 0
    for chromosome in population:
        sum += calculate_fitness(chromosome)
    return sum / len(population)


def calculate_fitness(chromosome):
    fitness = 0
    for x in range(len(chromosome)):
        if chromosome[x] == target_string[x]:
            fitness += 1
    return fitness


def parent_selection(population):
    tournament = []

    for x in range(0, 5):
        tournament.append(random.choice(population))
    max = 0
    for x in range(0, len(tournament)):
        if calculate_fitness(tournament[x]) >= max:
            max = calculate_fitness(tournament[x])
            parent = tournament[x]
    return parent


def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1))
    return parent1[:crossover_point] + parent2[crossover_point:], parent1[:crossover_point] + parent1[crossover_point:]


def mutate(children, mutation_rate):
    mutated_kids = []
    for child in children:
        mutated_child = ""
        for char in child:
            if random.random() < mutation_rate:
                if char == "1":
                    mutated_child += "0"
                elif char == "0":
                    mutated_child += "1"
            else:
                mutated_child += char
        mutated_kids.append(mutated_child)
    return mutated_kids


def evolve(population):
    mutation_rate = 0.01
    crossover_rate = 0.8
    new_population = []
    for x in range(0, 15):
        parent1 = parent_selection(population)
        parent2 = parent_selection(population)
        if random.random() < crossover_rate:
            children = crossover(parent1, parent2)
            new_population += (mutate(children, mutation_rate))
        else:
            new_population += (mutate((parent1, parent2), mutation_rate))
    return new_population


def genetic_algorithm(pop_size, generations):
    population = init_population(pop_size, len(target_string))
    fitness_hist = []
    for x in range(0, generations):
        population = evolve(population)
        fitness_hist.append(avg_fitness(population))

    plt.plot(range(1, generations + 1), fitness_hist)
    plt.xlabel('Generations')
    plt.ylabel('Average Fitness')
    plt.title('Genetic Algorithm (Target String): Average Fitness Over Generations')
    plt.show()


if __name__ == "__main__":
    population_size = 100
    string_length = 30
    generations = 100

    genetic_algorithm(population_size, generations)
