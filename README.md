# GA_bachelor_thesis
Howest - Bachelor thesis for AIBP

This code is based on previous experiments conducted by Cy Chan, M. (2020).

Class scheduling or course scheduling  is a well-known problem in the artificial intelligence and mathematics scene called University Course Scheduling (UCS). 

The UCS-problem is a complex task to solve, requiring efficient allocation of resources. While involving numerous constraints, such as room availability, lectors, students, …. 

By defining it as a constraint satisfaction problem, we can apply our metaheuristic methods. A metaheuristic is a problem-solving strategy or algorithmic framework that guides the search for approximate solutions in complex optimization problems.

Metaheuristic methods such as simulated annealing, ant colony optimization and genetic algorithms can all search this difficult solution space due to their iterative search techniques. 
But in this thesis we focus on genetic algorithms, which offer flexibility in handling the dynamic nature of course scheduling. 

Genetic algorithms are a biology-inspired, population-based algorithms. GAs represent their solutions as chromosomes, which contain all the encoded variables needed to create a viable schedule. After initializing, we can select the most fit individuals for the next generation, making use of genetic operators such as crossover and mutation. 
This will be repeated until a legal solution is found.

In our experiment we tried to create a legal solution from the data, without sacrificing one of the constraints. 
From our theoretical study, we know that it is possible to create a feasible scheduling program that makes use of genetic algorithms. Despite this, creating a working program that could solve it, is something else.

Creating a conflict-free schedule is important for several reasons. Firstly, we optimize the use of resources (Classrooms, Time slots, Materials, …). Secondly, we could create a better student experience, leading to a more general satisfaction across the board. Thirdly, manual course scheduling can be time-consuming and labor-intensive.

We solved this by researching allot of possible solutions, which we then implemented to create the above described experiment. With success.

This is important, as our findings can later lead to a more robust and refined program suitable for Howest. 
While researching we noticed that there are many ways to build a genetic algorithm. Each algorithm is kind of unique, making use of different selection methods, genetic operators, repair-functions, and so much more. 
This can mean that the solution that we found is not the optimal one, but still good enough. Which as you maybe remember is the goal of metaheuristic methods. 

For further research, we could look to implement more departments and classrooms. This data increase could lead to different results of the used genetic algorithm. This would also increase the combination possibilities immensely,  for which our algorithm maybe will not find any legal solution, or in a short amount of time. 
Besides increasing the data, we can look at different selection methods, or genetic operators that maybe perform better for our use case. 

Bibliography

Cy Chan, M. (2020). GASchedule. Github. https://github.com/mcychan/GASchedule.py used under the license of MIT. 
