from advent_of_code import get_input
from typing import List


def calculate_visible_trees(forest: List[str]) -> int:
    visible = 0
    for index_x in range(1, len(forest) - 1):
        for index_y in range(1, len(forest[0]) - 1):
            tree = forest[index_x][index_y]
            top = bottom = left = right = True
            for index_i in range(0, index_x):
                if tree <= forest[index_i][index_y]:
                    top = False
            for index_i in range(0, index_y):
                if tree <= forest[index_x][index_i]:
                    left = False
            for index_i in range(index_y + 1, len(forest[0])):
                if tree <= forest[index_x][index_i]:
                    right = False
            for index_i in range(index_x + 1, len(forest)):
                if tree <= forest[index_i][index_y]:
                    bottom = False
            if any([top, bottom, left, right]):
                visible += 1
    return visible


def find_scenic_scores(forest: List[str]) -> List[int]:
    scenic_scores: list[int] = [0]
    for index_x in range(1, len(forest) - 1):
        for index_y in range(1, len(forest[0]) - 1):
            tree = int(forest[index_x][index_y])
            top_neighbours = (
                bottom_neighbours
            ) = left_neighbours = right_neighbours = 0
            for index_i in range(0, index_x):
                neighbour = int(forest[index_x - index_i - 1][index_y])
                top_neighbours += 1
                if tree <= neighbour:
                    break
            for index_i in range(index_x + 1, len(forest)):
                neighbour = int(forest[index_i][index_y])
                bottom_neighbours += 1
                if tree <= neighbour:
                    break
            for index_i in range(0, index_y):
                neighbour = int(forest[index_x][index_y - index_i - 1])
                left_neighbours += 1
                if tree <= neighbour:
                    break
            for index_i in range(index_y + 1, len(forest[0])):
                neighbour = int(forest[index_x][index_i])
                right_neighbours += 1
                if tree <= neighbour:
                    break
            scenic_scores.append(
                top_neighbours
                * bottom_neighbours
                * left_neighbours
                * right_neighbours
            )
    return scenic_scores

input_str = get_input(8).strip()
input_list = input_str.split('\n')

top_line = bottom_line = len(input_list[0])
left_line = right_line = len(input_list) - 2
visible_from_the_egde = top_line + bottom_line + left_line + right_line
n_visible_trees = calculate_visible_trees(input_list) + visible_from_the_egde
print(n_visible_trees)

print(max(find_scenic_scores(input_list)))
