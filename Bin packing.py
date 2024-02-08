import random
import numpy as np
import Bin_packing_problems as bppScript
from matplotlib import pyplot as plt


def init_population(num_items, max_bin_weight, min_weight, population_size):
    population = []
    for _ in range(population_size):
        chromosome = [random.randint(0, (num_items - 1)) for _ in range(num_items)]
        population.append(chromosome)
    return population


# def check_valid_solution(chromosome, item_sizes, max_bin_size):
def calculate_fitness(chromosome, item_sizes, max_bin_size):
    num_bins = max(chromosome) + 1
    bins = [[] for _ in range(num_bins)]  # Create empty bins
    overloaded_bins = 0
    penalty = 0
    reward = 0
    for i, bin_index in enumerate(chromosome):
        bins[bin_index].append(item_sizes[i])  # Place the item in the corresponding bin

    total_fitness = 0
    for bin_contents in bins:
        bin_weight = sum(bin_contents)

        if bin_weight > max_bin_size:  # Check to see if bins exceed limit
            overloaded_bins = overloaded_bins + 1
        else:
            total_fitness = 20
    if overloaded_bins > 0:  # Apply penalty for invalid chromosomes
        penalty = overloaded_bins * -40
    if overloaded_bins == 0:
        reward = reward + (100 - len(np.unique(chromosome))) * 5
    total_fitness += reward + penalty

    return total_fitness


def calculate_average_fitness(population, item_sizes, max_bin_size):  # Calculates Average fitness of population
    total_fitness = 0
    for chromosome in population:
        fitness = calculate_fitness(chromosome, item_sizes, max_bin_size)
        total_fitness += fitness
    average_fitness = total_fitness / len(population)
    return average_fitness


def tournament_selection(population, tournament_size, item_sizes, max_bin_size):
    tournament = random.sample(population, tournament_size)  # Randomly select a subset (tournament) from the population
    tournament_fitness = []
    for chromosome in tournament:
        tournament_fitness.append(calculate_fitness(chromosome, item_sizes, max_bin_size))

    return tournament[tournament_fitness.index(max(tournament_fitness))]


def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1))  # Randomly select a crossover point
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return child1, child2


def mutation(chromosome, mutation_rate):
    mutated_chromosome = chromosome[:]  # Create a copy of the chromosome to avoid modifying the original
    for i in range(len(mutated_chromosome)):
        if random.random() < mutation_rate:
            mutated_chromosome[i] = random.randint(0, (len(chromosome) - 1))  # Mutate the gene to a random value
    return mutated_chromosome


def evolve(population, item_sizes, max_bin_size):
    mutation_rate = 0.02  # Rate of Mutation
    crossover_rate = 0.8  # Rate of crossover
    new_population = []
    for x in range(0, 50):
        parent1 = tournament_selection(population, 5, item_sizes, max_bin_size)
        parent2 = tournament_selection(population, 5, item_sizes, max_bin_size)
        if random.random() < crossover_rate:  # Determines if crossover should occur
            child1, child2 = crossover(parent1, parent2)
        else:
            child1, child2 = parent1, parent2
        mutated_child1 = mutation(child1, mutation_rate)
        mutated_child2 = mutation(child2, mutation_rate)
        new_population.append(mutated_child1)
        new_population.append(mutated_child2)
    return new_population


def genetic_algorithm(item_sizes, max_bin_size, generations, population_size):
    population = init_population(len(item_sizes), max_bin_size, min(item_sizes), population_size)
    fitness_hist = []
    bins_used_hist = []

    for x in range(0, generations):
        population = evolve(population, item_sizes, max_bin_size)
        fitness_hist.append(calculate_average_fitness(population, item_sizes, max_bin_size))
        bins_used = 0
        for chromosome in population:
            bins_used += len(np.unique(chromosome))
        bins_used_hist.append(bins_used / len(population))
    # Return dictionary of fitness history and average bins used for each generation
    return {'fitness_hist': fitness_hist, 'bins_used_hist': bins_used_hist}


if __name__ == "__main__":
    population_size = 100
    generations = 100
    # Initialise problems
    bpp_problems = bppScript.bin_packing_problems()
    problem_info = []
    # Iterate through problems, perform genetic algorithm
    for x in range(0, len(bpp_problems) - 1):
        problem_info.append(
            genetic_algorithm(bpp_problems[x].sizes, bpp_problems[x].bin_size, generations, population_size))
    # Plotting fitness
    plt.figure(figsize=(20, 14))
    plt.subplot(2, 1, 1)
    plt.xlabel('Generations')
    plt.ylabel('Average Fitness')
    plt.title('Genetic Algorithm: Fitness Over Generations')

    # Plotting bins used
    plt.subplot(2, 1, 2)
    plt.xlabel('Generations')
    plt.ylabel('Average Bins Used')
    plt.title('Genetic Algorithm: Average Bins Used Over Generations')

    for i in range(0, 1):
        info = genetic_algorithm(bpp_problems[i].sizes, bpp_problems[i].bin_size, generations, population_size)
        # Plotting fitness
        plt.subplot(2, 1, 1)
        plt.plot(range(1, generations + 1), info['fitness_hist'], label=f'{bpp_problems[i].name}')
        plt.legend()

        # Plotting bins used
        plt.subplot(2, 1, 2)
        plt.plot(range(1, generations + 1), info['bins_used_hist'], label=f'{bpp_problems[i].name}')
        plt.legend()

    # Show Graphs
    plt.tight_layout()
    plt.show()
