TEST = False

input_file = "input-test.txt" if TEST else "input.txt"

with open(f"input/{input_file}", "r") as fp:
    content = fp.read().splitlines()

result = [0] * len(content)

for id, game in enumerate(content):

    result[id] += 1

    cards = game.split(":")[1].strip()

    win_cards = cards.split("|")[0].split()
    my_cards = cards.split("|")[1].split()

    union = [x for x in my_cards if x in win_cards]

    for i in range(len(union)):
        print("Gmae: ", id + 1, "copy of: ", (id + 1) + (i + 1))
        result[id + (i + 1)] += 1

    # Calculate copy
    for i in range(result[id] - 1):
        for i in range(len(union)):
            print("Gmae: ", id + 1, "copy of: ", (id + 1) + (i + 1))
            result[id + (i + 1)] += 1

print("Result: ", sum(result))
