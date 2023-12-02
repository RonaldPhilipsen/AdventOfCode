from advent_of_code import get_input

DIRECTIONS = {1j, -1 + 1j, 1 + 1j}


class StopException(Exception):
    pass


class Simulator:
    def __init__(self, points: list[complex], threshold) -> None:
        self.points = points
        self.threshold = threshold

    def drop_grain(self) -> bool:
        grain = complex(500, 0)
        grain_at_rest = False

        if grain in self.points:
            return False

        while not grain_at_rest:
            for direction in DIRECTIONS:
                new_pos = grain + direction

                if new_pos not in self.points:
                    grain = new_pos

                    if grain.imag >= self.threshold:
                        return False
                    break

                self.points.append(grain)
                return True


def simulate_grain(points, threshold, threshold_is_floor=False):
    grain = complex(500, 0)

    if grain in points:
        raise StopException

    directions = [complex(0, 1), complex(-1, 1), complex(1, 1)]

    while True:
        keep_falling = False

        for direction in directions:
            new = grain + direction

            if new not in points:
                grain = new

                if not threshold_is_floor and grain.imag >= threshold:
                    raise StopException

                keep_falling = True
                break

        if not keep_falling:
            points.add(grain)
            return

        if threshold_is_floor and grain.imag == threshold - 1:
            points.add(grain)
            return


if __name__ == "__main__":
    text = get_input(14).strip()

    input_points = [
        complex(int(rock.split(",")[0]), int(rock.split(",")[1]))
        for scan in text.split("\n")
        for rock in scan.split(" -> ")
    ]
    abyss = max(point.imag for point in input_points)
    sim = Simulator(input_points, abyss)
    grains_dropped = 0

    while sim.drop_grain():
        grains_dropped += 1

    print(grains_dropped)

    points = input_points
    abyss = max(point.imag for point in points)

    grains = 0
    while True:
        try:
            simulate_grain(points, abyss)
        except StopException:
            print(grains)
            break
        else:
            grains += 1


#!/usr/bin/python3


def recursive_split(x, *args):
    y = []
    x = x.split(args[0])
    for part in x:
        if len(args) > 1:
            y += [recursive_split(part, *args[1:])]
        else:
            y += [part]
    return y


# returns 1 if the sand comes to rest before the max row
# returns 2 if the sand comes to rest after the max row
# returns 0 if the source location is blocked
def drop_sand():
    if sand_source in rock:
        return 0

    loc = sand_source
    while True:
        # check below
        maybe = (loc[0] + 1, loc[1])
        if maybe not in rock:
            loc = maybe
            continue

        # check below-left
        maybe = (loc[0] + 1, loc[1] - 1)
        if maybe not in rock:
            loc = maybe
            continue

        # check below-right
        maybe = (loc[0] + 1, loc[1] + 1)
        if maybe not in rock:
            loc = maybe
            continue

        # came to rest
        rock[loc] = 2
        if loc[0] > max_row:
            return 2
        else:
            return 1


data = recursive_split(text.rstrip("\n"), "\n", " -> ", ",")

ans1 = 0
ans2 = 0
rock = {}
max_row = 0
sand_source = (0, 500)

# build rock hash from input
for line in data:
    for idx in range(1, len(line)):
        fr = int(line[idx - 1][1])
        fc = int(line[idx - 1][0])
        tr = int(line[idx][1])
        tc = int(line[idx][0])
        if fr > max_row:
            max_row = fr
        if tr > max_row:
            max_row = tr
        if fr == tr:  # col varies
            if fc > tc:
                fc, tc = tc, fc
            for i in range(fc, tc + 1):
                rock[(fr, i)] = 1
        else:  # row varies
            if fr > tr:
                fr, tr = tr, fr
            for i in range(fr, tr + 1):
                rock[(i, fc)] = 1

# build floor for part 2
# as sand can only move down or diagonal, the max deviation in column is about the same as the max height
# so easy enough to just hard code something wide enough.
for c in range(500 - max_row - 10, 500 + max_row + 10):
    rock[(max_row + 2, c)] = 1

# part 1 ends when sand first passes the input floors and hits the part-2 floor
while drop_sand() != 2:
    ans1 += 1
print(f"Part 1: {ans1}")

# part 2 ends when sand source is blocked with sand
ans2 += ans1 + 1  # (plus 1 for the one that triggered the end of part 1)
while drop_sand() != 0:
    ans2 += 1
print(f"Part 2: {ans2}")
