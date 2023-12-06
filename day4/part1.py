TEST = False

input_file = "input-test.txt" if TEST else "input.txt"

with open(f"input/{input_file}", "r") as fp:
    content = fp.read().splitlines()

result = 0

for id, game in enumerate(content):

    cards = game.split(":")[1].strip()

    win_cards = cards.split("|")[0].split()
    my_cards = cards.split("|")[1].split()
    union = [x for x in my_cards if x in win_cards]

    result += int(2 ** (len(union) - 1))

print("Result: ", result)
