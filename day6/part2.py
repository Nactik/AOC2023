TEST = False

input_file = "input-test.txt" if TEST else "input.txt"

with open(f"input/{input_file}", "r") as fp:
    content = fp.read().split("\n")

times = [i for i in content[0].split(":")[1].strip() if not i.isspace()]
time = int("".join(times))


records = [i for i in content[1].split(":")[1].strip() if not i.isspace()]
record = int("".join(records))

result = 1

nb_ways = 0
for i in range(time):
    actual_record = i * (time - i)
    if actual_record > record:
        nb_ways += 1

result *= nb_ways

print("Result: ", result)
