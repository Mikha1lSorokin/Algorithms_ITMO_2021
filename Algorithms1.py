#Initialization of libraries
import numpy as np
import timeit
import matplotlib.pyplot as plt


#Time spent on each N info gathering
def timespent(function, k, n):
    timeseries = []
    for y in range(n):
        t = 0
        for x in range(k):
            number = list(np.random.random(y))
            start = timeit.default_timer()
            function(number)
            end = timeit.default_timer()
            t += (end - start)
        timeseries.append(t / k)
    return timeseries


#Exercises
#1. Cost function
def constant(input):
    return 0

#2. The sum of elements
def summorizing(input):
    sum = 0
    for i in range(len(input)):
        sum += input[i]
    return sum

#3. The product of elements
def product(input):
    prod = 1
    for i in range(len(input)):
        prod *= input[i]
    return prod

#4.1 Polynomial normal method
def polynominal_normal(input):
    x = 1.5
    result = 0
    for i in range(len(input)):
        result += input[i] * x ** i
    return result

#4.2 Polynomial Horner method
def polynominal_horner(input): 
    x = 1.5
    result = 0
    for i in range(len(input), 0, -1):
        result = input[i - 1] + x * result
    return result

#5. Bubble sort
def bubblesort(input):
    for z in range(len(input)):
        for x in range(len(input)-1):
            if input[x] > input[x + 1]:
                input[x], input[x + 1] = input[x + 1], input[x]
    return input

#6. Quick sort
def quicksort(input):
    return np.sort(input, kind='quicksort')

#7. Timsort
def timsort(input):
    return np.sort(input, kind='stable')


#Collecting time spent data
ex_1 = timespent(constant, 5, 2000)
ex_2 = timespent(summorizing, 5, 2000)
ex_3 = timespent(product, 5, 2000)
ex_4_1 = timespent(polynominal_normal, 5, 1500)
ex_4_2 = timespent(polynominal_horner, 5, 2000)
ex_5 = timespent(bubblesort, 5, 500)
ex_6 = timespent(quicksort, 5, 2000)
ex_7 = timespent(timsort, 5, 2000)


#Visualization
plt.figure(figsize=(10,5))
plt.plot(ex_1)
plt.ylabel('Time (seconds)')
plt.xlabel('N')
plt.legend(['Constant'])
plt.show()

plt.figure(figsize=(10,5))
plt.plot(ex_2)
plt.ylabel('Time (seconds)')
plt.xlabel('N')
plt.legend(['Summorizing'])
plt.show()

plt.figure(figsize=(10,5))
plt.plot(ex_3)
plt.ylabel('Time (seconds)')
plt.xlabel('N')
plt.legend(['Product'])
plt.show()

plt.figure(figsize=(10,5))
plt.plot(ex_4_1)
plt.ylabel('Time (seconds)')
plt.xlabel('N')
plt.legend(['Polynominal normal'])
plt.show()

plt.figure(figsize=(10,5))
plt.plot(ex_4_2)
plt.ylabel('Time (seconds)')
plt.xlabel('N')
plt.legend(['Polynominal horner'])
plt.show()

plt.figure(figsize=(10,5))
plt.plot(ex_5)
plt.ylabel('Time (seconds)')
plt.xlabel('N')
plt.legend(['Bubble sort'])
plt.show()

plt.figure(figsize=(10,5))
plt.plot(ex_6)
plt.ylabel('Time (seconds)')
plt.xlabel('N')
plt.legend(['Quicksort'])
plt.show()

plt.figure(figsize=(10,5))
plt.plot(ex_7)
plt.ylabel('Time (seconds)')
plt.xlabel('N')
plt.legend(['Timsort'])
plt.show()


#Time spent on each N info gathering for matrices
def timespent_matrix(k, n):
    timeseries = []
    for y in range(1, n + 1):
        t = 0
        for x in range(k):
            matrix1 = np.random.random((y, y))
            matrix2 = np.random.random((y, y))
            start = timeit.default_timer()
            matrix1 @ matrix2
            end = timeit.default_timer()
            t += (end - start)
        timeseries.append(t / k)
    return timeseries


#Ex. 8. Product of matrices
ex_8 = timespent_matrix(5, 200)

# Matrices product visualization
plt.figure(figsize=(10,5))
plt.plot(ex_8)
plt.ylabel('Time (seconds)')
plt.xlabel('N')
plt.legend(['Product of matrices'])
plt.show()