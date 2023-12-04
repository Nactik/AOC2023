TEST = False

file = "input-test.txt" if TEST else "input.txt"

with open(f"input/{file}", "r") as f:
    content = f.read().splitlines()

digits = [[x for x in line if x.isdigit()] for line in content]

two_digits = [int("".join([line[i] for i in (0, -1)])) for line in digits]

print(sum(two_digits))
