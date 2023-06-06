from Objects.Schedule import Schedule
import random
from random import randrange
from time import time


# Lakshmi, R. et al. “A New Biological Operator in Genetic Algorithm for Class Scheduling Problem.”
# International Journal of Computer Applications 60 (2012): 6-11.
# Copyright (c) 2020 - 2022 Miller Cy Chan


class GeneticAlgorithm:
    def initAlgorithm(self, prototype, numberOfChromosomes=100, replaceByGeneration=8, trackBest=5):
        self._currentBestSize = 0
        self._prototype = prototype

        if numberOfChromosomes < 2:
            numberOfChromosomes = 2

        if trackBest < 1:
            trackBest = 1

        self._chromosomes = numberOfChromosomes * [None]
        self._bestFlags = numberOfChromosomes * [False]

        self._bestChromosomes = trackBest * [0]
        self.set_replace_by_generation(replaceByGeneration)

    def __init__(self, configuration, numberOfCrossoverPoints=2, mutationSize=2, crossoverProbability=80,
                 mutationProbability=3):
        self.initAlgorithm(Schedule(configuration))
        self._mutationSize = mutationSize
        self._numberOfCrossoverPoints = numberOfCrossoverPoints
        self._crossoverProbability = crossoverProbability
        self._mutationProbability = mutationProbability
        self._fitness_per_generation = []

    @property
    def result(self):
        return self._chromosomes[self._bestChromosomes[0]]

    def set_replace_by_generation(self, value):
        numberOfChromosomes = len(self._chromosomes)
        trackBest = len(self._bestChromosomes)
        if (value > numberOfChromosomes - trackBest):
            value = numberOfChromosomes - trackBest
        self._replaceByGeneration = value

    def addToBest(self, chromosomeIndex):
        bestChromosomes = self._bestChromosomes
        length_best = len(bestChromosomes)
        bestFlags = self._bestFlags
        chromosomes = self._chromosomes

        if (self._currentBestSize == length_best and chromosomes[bestChromosomes[self._currentBestSize - 1]].fitness >=
            chromosomes[chromosomeIndex].fitness) or bestFlags[chromosomeIndex]:
            return

        j = self._currentBestSize
        for i in range(j, -1, -1):
            j = i
            pos = bestChromosomes[i - 1]
            if i < length_best:
                if chromosomes[pos].fitness > chromosomes[chromosomeIndex].fitness:
                    break

                bestChromosomes[i] = pos
            else:
                bestFlags[pos] = False

        bestChromosomes[j] = chromosomeIndex
        bestFlags[chromosomeIndex] = True

        if self._currentBestSize < length_best:
            self._currentBestSize += 1

    def isInBest(self, chromosomeIndex) -> bool:
        return self._bestFlags[chromosomeIndex]

    def clearBest(self):
        self._bestFlags = len(self._bestFlags) * [False]
        self._currentBestSize = 0

    def initialize(self, population):
        prototype = self._prototype
        length_chromosomes = len(population)

        for i in range(0, length_chromosomes):
            population[i] = prototype.makeNewFromPrototype()

    def selection(self, population):
        length_chromosomes = len(population)
        return (population[randrange(32768) % length_chromosomes],  population[randrange(32768) % length_chromosomes])

    def replacement(self, population, replaceByGeneration) -> []:
        mutationSize = self._mutationSize
        numberOfCrossoverPoints = self._numberOfCrossoverPoints
        crossoverProbability = self._crossoverProbability
        mutationProbability = self._mutationProbability
        selection = self.selection
        isInBest = self.isInBest
        length_chromosomes = len(population)
        offspring = replaceByGeneration * [None]
        for j in range(replaceByGeneration):
            parent = selection(population)

            offspring[j] = parent[0].crossover(parent[1], numberOfCrossoverPoints, crossoverProbability)
            offspring[j].mutation(mutationSize, mutationProbability)

            ci = randrange(32768) % length_chromosomes
            while isInBest(ci):
                ci = randrange(32768) % length_chromosomes

            population[ci] = offspring[j]

            self.addToBest(ci)
        return offspring

    def run(self, maxRepeat=9999, minFitness=0.999):
        self.clearBest()
        length_chromosomes = len(self._chromosomes)

        self.initialize(self._chromosomes)
        random.seed(round(time() * 1000))

        currentGeneration = 0

        repeat = 0
        lastBestFit = 0.0

        while 1:
            best = self.result
            print(best.fitness, currentGeneration)

            if best.fitness > minFitness:
                break

            difference = abs(best.fitness - lastBestFit)
            if difference <= 0.0000001:
                repeat += 1
            else:
                repeat = 0

            if repeat > (maxRepeat / 100):
                random.seed(round(time() * 1000))
                self.set_replace_by_generation(self._replaceByGeneration * 3)
                self._crossoverProbability += 1

            self.replacement(self._chromosomes, self._replaceByGeneration)

            lastBestFit = best.fitness
            self._fitness_per_generation.append(lastBestFit)
            currentGeneration += 1

    def __str__(self):
        return "Genetic Algorithm"