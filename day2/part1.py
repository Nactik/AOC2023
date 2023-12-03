import re

TEST = False
LIMITS = {"green": 13, "red": 12, "blue": 14}

input_file = "input-test.txt" if TEST else "input.txt"

with open(f"input/{input_file}", "r") as fp:
    content = fp.read().splitlines()

result = 0

for idx, game in enumerate(content):
    flag = False

    game_id = idx + 1

    game_content = game.split(":")[1]

    balls = re.split(",|;", game_content)

    for toss in balls:
        nb, color = toss.strip().split()

        if int(nb) > LIMITS.get(color, 0):
            flag = True
            print("nop")
            break

    if not flag:
        result += game_id

print("Result: ", result)
