from multiprocessing import Pool
import matplotlib.pyplot as plt

#   collatz.py
#   James Yoo
#   Created: October 31, 2017


def collatz(n):
    steps = 0
    while n > 0:
        if n == 1:
            return steps
        elif n % 2 == 0:
            n = n / 2
            steps += 1
        elif n % 2 == 1:
            n = (n * 3) + 1
            steps += 1

    return steps


def collatz_path(n):
    path = []
    while n > 0:
        path.append(n)
        if n == 1:
            return path
        elif n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3) + 1
    
    return path


def generate_steps(n):
    x_data = range(1, n + 1)
    p = Pool(10)
    y_data = p.map(collatz, x_data) 
    plt.scatter(x_data, y_data, s=0.5)
    plt.title("Collatz Conjecture Visualization")
    plt.xlabel("Input value")
    plt.ylabel("Steps", rotation=0)
    plt.show()


def generate_path(n):
    x_data = range(1, n + 1)
    p = Pool(10)
    y_data = p.map(collatz_path, x_data)
    
    for x_d, y_d in zip(x_data, y_data):
        plt.scatter([x_d] * len(y_d), y_d, s=0.5)

    plt.title("Collatz Path for Integers up to " + str(n))
    plt.xlabel("Input value")
    plt.ylabel("Path", rotation=0)
    plt.show()


upper = input("Enter the number you'd like to go up to: ")
generate_path(int(upper))


