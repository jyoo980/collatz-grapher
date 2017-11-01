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


def generate_data(n):
    x_data = range(1, n + 1)
    y_data = [collatz(x) for x in x_data]
    plt.scatter(x_data, y_data, s=0.5)
    plt.title("Collatz Conjecture Visualization")
    plt.xlabel("Input value")
    plt.ylabel("Steps", rotation=0)
    plt.show()


upper = input("Enter the number you'd like to go up to: ")
generate_data(int(upper))


