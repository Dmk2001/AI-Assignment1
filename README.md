# Description of code:
## Init_population(): 
This generates an array of specified length (100) of binary strings of character length 30. Each string represents a chromosome consisting of 1’s and 0’s.
## Avg_fitness():
Returns the average fitness of a population. (sum / len(population)
## Calculate_fitness():
Determines the fitness of each function by counting the number of 1’s in a chromosome. For problem 1.2, fitness is calculated by the number of bits that math the target string. For 1.3, if the fitness is 0 (there no 1’s), then a value of 60 is returned.
## Parent_selection():
Implements tournament selection by randomly choosing a subset of chromosomes, then it selects the chromosome with highest fitness.
## Crossover():
Crossover occurs with an 80% chance. Crossover involves taking 2 parents, randomly choosing a crossover point and then crossing bits between each at this point. This creates new offspring (child). This applies to all problems.
## Mutate():
Introduces random mutation to 2 child chromosomes at a given rate (0.01). Flips bits in chromosome at random to produce mutated children. This applies to al problems.
## Evolve():
Mutation and crossover rates are set. Loops through populations, generating a new population for each generation. This function calls the parent selection, crossover, and mutation functions. Returns a new population of chromosomes.
## Genetic_algorithm():
initializes a population, evolves it over a specified number of generations, and records the average fitness of each generation. Finally, it plots a graph showing how the average fitness changes over generations.
## Main():
Sets population, generation and string size. Calls genetic algorithm function.

## One Max Problem
![1 1](https://github.com/Dmk2001/AI-Assignment1/assets/74598528/574ee8ee-bef8-42c8-a81b-345bc781a629)

The algorithm is quick to find the optimal solution, taking roughly 20 generations to achieve an average fitness score which is close to the optimal. The increase in fitness score is quick to increase over the first 20 generations as chromosomes mutate quickly to achieve the target solution of 30 1’s. After generation 20, the graph stabilises, with slight fluctuations over the following generations. However, this shows the algorithm is efficient at calculating the optimal/near optimal solution.
 
## Target String
![1 2](https://github.com/Dmk2001/AI-Assignment1/assets/74598528/13109b00-1ab6-4a0a-92ce-9faf42242796)

This problem shows similar performance to the one above. However, when comparing both graphs, we see the one max problem reaches a higher average fitness at generation 20 as opposed to finding the target string. It shows the ability of the algorithm to find specific patterns.
## Deceptive Problem
![1 3](https://github.com/Dmk2001/AI-Assignment1/assets/74598528/1eabebad-00e8-4aeb-ab56-0d8e2f3f899a)

We can see from this graph that the algorithm struggles with the deceptive landscape as unlike the previous two problems, it never reaches towards the optimal solution, with massive spikes as chromosomes are penalised for having complete solutions. Initially, it performs like the previous two problems, quickly reaching an average fitness which is high, but fails to surpass this.

