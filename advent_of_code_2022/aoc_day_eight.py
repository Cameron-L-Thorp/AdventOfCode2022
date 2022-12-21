horizontal_tree_grid = []
vertical_tree_grid = []

with open('day_eight/day_eight_input.txt') as input:
    for line in input.readlines():
        horizontal_tree_grid.append(line.strip())

# for line in tree_grid:
#     print(line)

visibility_counter = 0

#rotates 90 degrees left
for i in range(1, 100):
    vertical_tree_col = ''
    for tree_row in horizontal_tree_grid:
        vertical_tree_col += tree_row[-i]
    vertical_tree_grid.append(vertical_tree_col)

for column in vertical_tree_grid:
    print(column)


#count visible trees on horizontal plane (line)
#see if visible trees are visible on vertical plane (same index of different lines)

# for i in range(len(tree_grid)):
#     if i == 0 or i == (len(tree_grid) - 1):
#         visibility_counter += len(tree_grid[i])
#     else:
#         visibility_counter += 2
#     index = 0
#     for tree in tree_grid[i]:
        


#print(visibility_counter)