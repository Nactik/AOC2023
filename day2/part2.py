import re

TEST = False

input_file = "input-test.txt" if TEST else "input.txt"

with open(f"input/{input_file}", "r") as fp:
    content = fp.read().splitlines()

result = 0

for idx, game in enumerate(content):
    nb_balls = {"green": 0, "red": 0, "blue": 0}
    game_id = idx + 1

    game_content = game.split(":")[1]

    balls = re.split(",|;", game_content)

    for toss in balls:
        nb, color = toss.strip().split()
        if int(nb) > nb_balls.get(color, 0):
            nb_balls[color] = int(nb)

    power = 1
    for key, val in nb_balls.items():
        power *= val

    result += power

print("Result: ", result)
