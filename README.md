# Description of code for problems 1 - 3:
### Init_population(): 
This generates an array of specified length (100) of binary strings of character length 30. Each string represents a chromosome consisting of 1’s and 0’s.
### Avg_fitness():
Returns the average fitness of a population. (sum / len(population)
### Calculate_fitness():
Determines the fitness of each function by counting the number of 1’s in a chromosome. For problem 1.2, fitness is calculated by the number of bits that math the target string. For 1.3, if the fitness is 0 (there no 1’s), then a value of 60 is returned. If it is all 1's it is also penalised.
### Parent_selection():
Implements tournament selection by randomly choosing a subset of chromosomes, then it selects the chromosome with highest fitness.
### Crossover():
Crossover occurs with an 80% chance. Crossover involves taking 2 parents, randomly choosing a crossover point and then crossing bits between each at this point. This creates new offspring (child). This applies to all problems.
### Mutate():
Introduces random mutation to 2 child chromosomes at a given rate (0.01). Flips bits in chromosome at random to produce mutated children. This applies to all problems.
### Evolve():
Mutation and crossover rates are set. Loops through populations, generating a new population for each generation. This function calls the parent selection, crossover, and mutation functions. Returns a new population of chromosomes.
### Genetic_algorithm():
initializes a population, evolves it over a specified number of generations, and records the average fitness of each generation. Finally, it plots a graph showing how the average fitness changes over generations.
### Main():
Sets population, generation and string size. Calls genetic algorithm function.

### One Max Problem
![1 1](https://github.com/Dmk2001/AI-Assignment1/assets/74598528/574ee8ee-bef8-42c8-a81b-345bc781a629)

The algorithm is quick to find the optimal solution, taking roughly 20 generations to achieve an average fitness score which is close to the optimal. The increase in fitness score is quick to increase over the first 20 generations as chromosomes mutate quickly to achieve the target solution of 30 1’s. After generation 20, the graph stabilises, with slight fluctuations over the following generations. However, this shows the algorithm is efficient at calculating the optimal/near optimal solution.
 
### Target String
![1 2](https://github.com/Dmk2001/AI-Assignment1/assets/74598528/13109b00-1ab6-4a0a-92ce-9faf42242796)

This problem shows similar performance to the one above. However, when comparing both graphs, we see the one max problem reaches a higher average fitness at generation 20 as opposed to finding the target string. It shows the ability of the algorithm to find specific patterns.

### Deceptive Problem
![1 3](https://github.com/Dmk2001/AI-Assignment1/assets/74598528/1eabebad-00e8-4aeb-ab56-0d8e2f3f899a)

We can see from this graph that the algorithm struggles with the deceptive landscape as unlike the previous two problems, it never reaches towards the optimal solution, with massive spikes as chromosomes are penalised for having complete solutions. Initially, it performs like the previous two problems, quickly reaching an average fitness which is high, but fails to surpass this.

#  Bin Packing Problem 
### Representation of Solutions
Chromosomes are represented using integers. Each index in a chromosome corresponds to an item in the item sizes array. The integer represents the bin in which an item will be placed. For example, chromosome[0] = 6 means that item 1 is placed in bin 6. This is a straightforward solution and makes crossover and mutation easier to implement, 
### Fitness Function
Fitness is calculated by checking if there are any overloaded bins in the chromosome. If there is, a penalty is applied, which scales up for more overloaded bins. Chromosomes are rewarded if there are less bins used. If there are no overloaded bins, an initial reward of 40 is given. By applying a penalty, infeasible solutions are discouraged, ideally resulting in solutions that are feasible. 
### Selection Of Parents
Parents are selected using tournament selection. 5 random chromosomes are selected and the one with the highest fitness is selected as the first parent. This is repeated for the second. Using tournament selection increases diversity due to its random selection of candidates. Basing selection on fitness will ideally lead to better candidates for mutation, leading to an optimal solution.
### Crossover  
Crossover occurs with a probability of 80%. When this happens, a single point crossover occurs at random point over 2 parents. These points are then switched to create two "new" children. Crossover promotes diverse child candidates that may contain solutions which are closer to the optimum. Using 1 point crossover allows for potential useful combinations to be preserved.
### Mutation
Mutation works by randomly reassigning items to different bins at a rate of 1%. Bins are randomly reassigned an integer that lies between the min value of integers in the chromosome and the max. The hope is that values begin to converge and bins outside the range aren't used. This acts in a similar way to flipping bits in the first 3 problems, randomly reassigning values without consideration of whether bins become full when flipped. This isn't very robust as there's no check for if bins are full, but it allows for a greater search space of potentially better solutions and would prevent getting stuck at a local optimum.

### Results: Average Fitness and Average Bins Used
![bpp](https://github.com/Dmk2001/AI-Assignment1/assets/74598528/9244e662-e47e-48f3-85f6-679a6fe5bc61)
### Insights into the problem landscape
The bin packing/knapsack problem is NP-Hard. Finding an optimal solution for large or complex instances is computationally expensive and can't be solved in polynomial time. Genetic algorithms allow the search of potential solutions in a time which is more reasonable as they naturally select solutions through evolution of existing solutions as opposed to a brute-force search.

The fitness landscape of a problem like this tends to have many local optima (max and min) as changes which are small can lead to a larger change such as how items are placed into bins, or the number of bins used within a chromosome. Using mutation and crossover functions like above, allow for a greater search space, minimising the chance of hitting local optima which could mean the actual optimal solution may not be found.

The problem presented here is a simple version of the bin backing problem. In this case, the only consideration for optimisation is finding the minimum number of bins that are required to fit all the items. We don't take into account any notion of value or how bins are packed (only if they are overflowing). In this case, finding an optimal solution is relatively easy to both find and calculate although it takes time with the algorithm I've coded. From the graph above, we can see the average fitness rises quickly and the average bins drops quickly over the first 100 generations. After this, the improvement does begin to slow.

The solution above, based on the graph does work in finding what could be close to the optimal solution. However, improvements could of course be made. Increasing population size and the number of generations may tend to find an even closer optimal solution. Adjusting mutation and crossover rate is another consideration to be made.  Changing the mutation function to only reassign items to bins that won't cause an overflow could be considered but this may lead to local optima as the use of invalid solutions allows for a greater search space. 

Adjusting fitness to calculate how well bins are packed could also provide more optimal solutions too. Using a different form of mutation such as scrambling chromosomes, swapping indices or by starting with a high mutation rate which decreases over generations. Differences like this may help further. 

In conclusion, the results obtained are a positive start. With minor code changes I feel it's possible to generate a solution that may provide better performance over fewer generations, reaching a solution that is close to if not the best solution to this problem.

## References for research
Genetic Algorithm for Bin Packing Problem - https://www.codeproject.com/Articles/633133/ga-bin-packing

Application of Genetic Algorithm for the Bin Packing Problem with a New Representation Scheme - https://www.sid.ir/fileserver/je/1010720100302

Python and the Bin Packing Problem - https://reintech.io/blog/python-bin-packing-problem-guide

Exploring the Bin Packing Problem - https://medium.com/swlh/exploring-the-bin-packing-problem-f54a93ebdbe5

Wikipedia (as suggested) - https://en.wikipedia.org/wiki/Bin_packing_problem

