horizontal_tree_grid = []
vertical_tree_grid = []

with open('day_eight/day_eight_input.txt') as input:
    for line in input.readlines():
        horizontal_tree_grid.append(line.strip())

# for line in tree_grid:
#     print(line)

visibility_counter = 0

#rotates 90 degrees left
for i in range(1, (len(horizontal_tree_grid) + 1)):
    vertical_tree_col = ''
    for tree_row in horizontal_tree_grid:
        vertical_tree_col += tree_row[-i]
    vertical_tree_grid.append(vertical_tree_col)

for column in vertical_tree_grid:
    print(column)


#count visible trees on horizontal plane (line)
#see if visible trees are visible on vertical plane (same index of different lines)

for i in range(len(horizontal_tree_grid)):
    if i == 0 or i == (len(horizontal_tree_grid) - 1):
        visibility_counter += len(horizontal_tree_grid[i])
    else:
        visibility_counter += 2
    index = 0

for tree_row in range(len(horizontal_tree_grid)):

    left_highest = horizontal_tree_grid[tree_row][0]
    right_highest = horizontal_tree_grid[tree_row][-1]
    top_highest = vertical_tree_grid[-(tree_row + 1)][0]
    bottom_highest = vertical_tree_grid[-(tree_row + 1)][-1]

    if tree_row == 0 or tree_row == len(horizontal_tree_grid) - 1:
        continue
    index = 1
    while index < len(horizontal_tree_grid) / 2:
#compares each item to the item 'in front' of it from the nearest side.
        if horizontal_tree_grid[tree_row][index] > horizontal_tree_grid[tree_row][index - 1]:
            visibility_counter += 1
            left_highest = horizontal_tree_grid[tree_row][index]
        if horizontal_tree_grid[tree_row][-index] > horizontal_tree_grid[tree_row][-(index - 1)]:
            visibility_counter += 1
            right_highest = horizontal_tree_grid[tree_row][-index]
        if vertical_tree_grid[-tree_row][index] > vertical_tree_grid[-tree_row][index - 1]:
            visibility_counter += 1
            top_highest = vertical_tree_grid[tree_row][index]
        if vertical_tree_grid[-tree_row][-index] > vertical_tree_grid[-tree_row][-(index - 1)]:
            visibility_counter += 1
            bottom_highest = vertical_tree_grid[tree_row][-index]
        if (index == tree_row) or (-index == -tree_row - 1):
            visibility_counter -= 1
        index += 1
    
print(visibility_counter)


# if (tree_grid[y_coord][x_coord] > top_highest[y_coord]) or (tree_grid[y_coord][x_coord] > left_highest[y_coord]) or (tree_grid[y_coord][x_coord] > right_highest[y_coord]) or (tree_grid[y_coord][x_coord] > bottom_highest[y_coord]):
#          increase = True

#          if tree_grid[y_coord][x_coord] > top_highest[y_coord]:
#              top_highest[y_coord] = tree_grid[y_coord][x_coord]
#          if tree_grid[y_coord][x_coord] > left_highest[y_coord]:
#              left_highest[y_coord] = tree_grid[y_coord][x_coord]
#          if tree_grid[y_coord][x_coord] > right_highest[y_coord]:
#              right_highest[y_coord] = tree_grid[y_coord][x_coord]
#          if tree_grid[y_coord][x_coord] > bottom_highest[y_coord]:
#              bottom_highest[y_coord] = tree_grid[y_coord][x_coord]