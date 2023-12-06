TEST = False

input_file = "input-test.txt" if TEST else "input.txt"

with open(f"input/{input_file}", "r") as fp:
    content = fp.read().split("\n")

times = [int(i) for i in content[0].split(":")[1].strip().split()]
records = [int(i) for i in content[1].split(":")[1].strip().split()]

result = 1

for idx, time in enumerate(times):
    nb_ways = 0
    for i in range(time):
        record = i * (time - i)
        if record > records[idx]:
            nb_ways += 1

    result *= nb_ways

print("Result: ", result)
