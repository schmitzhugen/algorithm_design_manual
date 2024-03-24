# The Collatz Conjecture

def collatz(i):
    arr = [i]
    while i != 1:
        if i % 2 == 1:
            i = 3 * i + 1
            arr.append(i)
        elif i % 2 == 0:
            i = i / 2
            arr.append(i)
    return len(arr)


# print(collatz(100))  # should be 26


def problem(i, j):
    max_cycle = 0
    for i in range(i, j + 1):
        if collatz(i) > max_cycle:
            max_cycle = collatz(i)
    return max_cycle


# print(problem(1, 10))  # should be 20
# print(problem(100, 200))  # should be 125
# print(problem(201, 210))  # should be 89
# print(problem(900, 1000))  # should be 174

if __name__ == "__main__":
    while True:
        try:
            # Get user input for the two parameters
            i, j = map(int, input().split())
            # Call the function and print the result
            result = problem(i, j)
            print(f"{i} {j} {result}")
        except EOFError:
            break