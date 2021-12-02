# Exs: Looking at a person's characteristics : different types of ability

# math memory
# language math
#personality test

# Mutually exclusive responses
# Changing cultural contexts - tricky 

# factor_analyzer (the name of the package) : It is a newer package


import pandas
import numpy

from factor_analyzer import FactorAnalyzer

import matplotlib.pyplot as pyplot

dataset = pandas.read_csv("bfi.csv")
print(dataset)
dataset.drop(['gender','age','education'], axis=1, inplace=True)
dataset.drop(['Unnamed: 0'], axis=1, inplace=True)
dataset.dropna(inplace=True)

print(dataset)

machine = FactorAnalyzer(n_factors=25, rotation=None)
machine.fit(dataset)
ev, v = machine.get_eigenvalues()
print(ev)

#Data visualization
pyplot.scatter(range(1, dataset.shape[1]+1), ev)
pyplot.savefig("plot.png")
pyplot.close()

machine = FactorAnalyzer(n_factors=6, rotation='varimax')
machine.fit(dataset)
output = machine.loadings_
numpy.set_printoptions()
print(output)

#Interpretation: Each question (rows), each column()
# We don't even need the 


machine = FactorAnalyzer(n_factors=5, rotation='varimax')
machine.fit(dataset)
loadings = machine.loadings_
# numpy.set_printoptions()
print(output)


print("factor loadings:\n")
print(loadings)
print(machine.get_factor_variance())

dataset = dataset.values #transforms the data into array

print(result)
print(result.values)