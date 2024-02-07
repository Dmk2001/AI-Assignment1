import random

from matplotlib import pyplot as plt


def init_population(population_size, string_length):
    population = []
    for x in range(0, population_size):
        str = ""
        for _ in range(string_length):
            str += random.choice('01')
        population.append(str)
    return population


def avg_fitness(population):
    sum = 0
    for chromosome in population:
        sum += calculate_fitness(chromosome)
    return sum / len(population)


def calculate_fitness(chromosome):
    return chromosome.count('1')


def parentSelection(population):
    # tournament selection
    tournament = []
    # Choose 5 random chromosomes
    for x in range(0, 5):
        tournament.append(random.choice(population))
    max = 0
    for x in range(0, len(tournament)):
        if calculate_fitness(tournament[x]) >= max:
            max = calculate_fitness(tournament[x])
            parent = tournament[x]
    return parent


def crossover(parent1, parent2):
    # random crossover point
    crossover_point = random.randint(0, len(parent1))
    return parent1[:crossover_point] + parent2[crossover_point:], parent1[:crossover_point] + parent1[crossover_point:]


def mutate(children, mutation_rate):
    mutated_kids = []
    for child in children:
        mutated_child = ""
        mutated_child_char = ""
        for char in child:
            if random.random() < mutation_rate:
                if char == 1:
                    mutated_child_char = "0"
                elif char == 0:
                    mutated_child_char = "1"

            else:
                mutated_child_char = char
            mutated_child += mutated_child_char
        mutated_kids.append(mutated_child)

    return mutated_kids


def evolve(population):
    crossover_rate = 0.8
    mutation_rate = 0.01
    new_population = []
    for x in range(0, 15):
        # Select parents
        parent1 = parentSelection(population)
        parent2 = parentSelection(population)
        # Create children
        if random.random() < crossover_rate:
            children = crossover(parent1, parent2)
            new_population += (mutate(children, mutation_rate))
        else:
            new_population += (mutate((parent1, parent2), mutation_rate))

    return new_population


def genetic_algorithm(pop_size, str_length, generations):
    population = init_population(pop_size, str_length)
    fitness_hist = []
    for x in range(0, generations):
        population = evolve(population)
        fitness_hist.append(avg_fitness(population))
    plt.plot(range(1, generations + 1), fitness_hist, marker='o')
    plt.xlabel('Generations')
    plt.ylabel('Average Fitness')
    plt.title('Genetic Algorithm: Average Fitness Over Generations')
    plt.show()


if __name__ == "__main__":
    population_size = 100
    string_length = 30
    generations = 30

    genetic_algorithm(population_size, string_length, generations)
