"""Advent of code day 16"""
import re
from dataclasses import dataclass
from advent_of_code import get_input


VALVE_REGEX = r"Valve ([A-Z]{2}) has flow rate=(\d+)"
CAVE_REGEX = r"\s?tunnels? leads? to valves? ([A-Z,].*)"
TUNNEL_LEN = 1


@dataclass
class Node(dict):
    """class to represent a node in a graph"""

    valve_id: str
    visited: bool
    flow_rate: int
    tunnels: set[str]
    paths: dict[str, int]


def parse_input(input_text: str):
    input_list = input_text.splitlines()
    cave = {}  # type: Dict[str, Node]
    for line in input_list:
        valve_info, cave_info = line.split(";")
        valve_id, flow_rate = re.match(VALVE_REGEX, valve_info).groups()
        edges = re.match(CAVE_REGEX, cave_info).group(1).replace(" ", "").split(",")
        cave[valve_id] = Node(valve_id, False, int(flow_rate), edges, {})
    return cave


def breadth_first_search(graph: dict[str, Node], frontier: set[str], end: str):
    depth = 1
    while True:
        next_frontier = set()
        for node in frontier:
            if node == end:
                return depth
            for tunnel in graph[node].tunnels:
                next_frontier.add(tunnel)
        frontier = next_frontier
        depth += 1


def get_possible_paths(graph: dict[str, Node]):
    """appends all paths from the result of a BFS to the tunnels"""
    keys = sorted([x for x in list(graph.keys()) if graph[x].flow_rate != 0])
    for k in keys + ["AA"]:
        for k2 in keys:
            if k2 != k:
                graph[k].paths[k2] = breadth_first_search(graph, graph[k].tunnels, k2)


def part1(cave: dict[str, Node]):
    """do the first part of the puzzle"""
    best = 0

    def search(opened: set[str], flowed: int, current_room: str, depth_to_go: 29):
        nonlocal best
        if flowed > best:
            best = flowed

        if depth_to_go <= 0:
            return

        if current_room not in opened:
            search(
                opened.union([current_room]),
                flowed + cave[current_room].flow_rate * depth_to_go,
                current_room,
                depth_to_go - 1,
            )
        else:
            for key in [x for x in cave[current_room].paths.keys() if x not in opened]:
                search(opened, flowed, key, depth_to_go - cave[current_room].paths[key])

    search(set(["AA"]), 0, "AA", 29)
    return best


def part2(cave: dict[str, Node]):
    best = 0

    def search(
        opened: set[str],
        flowed: int,
        current_room: str,
        depth_to_go: 29,
        elephants_turn: bool,
    ):
        nonlocal best
        if flowed > best:
            best = flowed

        if depth_to_go <= 0:
            return

        if current_room not in opened:
            search(
                opened.union([current_room]),
                flowed + cave[current_room].flow_rate * depth_to_go,
                current_room,
                depth_to_go - 1,
                elephants_turn,
            )
            if not elephants_turn:
                search(
                    set([current_room]).union(opened),
                    flowed + cave[current_room].flow_rate * depth_to_go,
                    "AA",
                    25,
                    True,
                )
        else:
            for k in [x for x in cave[current_room].paths.keys() if x not in opened]:
                search(
                    opened,
                    flowed,
                    k,
                    depth_to_go - cave[current_room].paths[k],
                    elephants_turn,
                )

    search(set(["AA"]), 0, "AA", 25, False)
    return best


if __name__ == "__main__":
    puzzle_input = get_input(16)
    cave = parse_input(puzzle_input)
    get_possible_paths(cave)
    print(part1(cave))
    print(part2(cave))
