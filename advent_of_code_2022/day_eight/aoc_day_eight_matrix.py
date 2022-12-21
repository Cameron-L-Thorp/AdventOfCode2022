tree_grid = []
visible_trees = 0

def tree_checker(y_coord, x_coord):
    increase = False
    if (tree_grid[x_coord][y_coord] > top_highest[x_coord]) or (tree_grid[x_coord][y_coord] > left_highest[x_coord]) or (tree_grid[x_coord][y_coord] > right_highest[x_coord]) or (tree_grid[x_coord][y_coord] > bottom_highest[x_coord]):
         increase = True

         if tree_grid[x_coord][y_coord] > top_highest[x_coord]:
             top_highest[x_coord] = tree_grid[x_coord][y_coord]
         if tree_grid[x_coord][y_coord] > left_highest[x_coord]:
             left_highest[x_coord] = tree_grid[x_coord][y_coord]
         if tree_grid[x_coord][y_coord] > right_highest[x_coord]:
             right_highest[x_coord] = tree_grid[x_coord][y_coord]
         if tree_grid[x_coord][y_coord] > bottom_highest[x_coord]:
             bottom_highest[x_coord] = tree_grid[x_coord][y_coord]

    elif (tree_grid[y_coord][x_coord] > top_highest[y_coord]) or (tree_grid[y_coord][x_coord] > left_highest[y_coord]) or (tree_grid[y_coord][x_coord] > right_highest[y_coord]) or (tree_grid[y_coord][x_coord] > bottom_highest[y_coord]):
          increase = True

          if tree_grid[y_coord][x_coord] > top_highest[y_coord]:
              top_highest[y_coord] = tree_grid[y_coord][x_coord]
          if tree_grid[y_coord][x_coord] > left_highest[y_coord]:
              left_highest[y_coord] = tree_grid[y_coord][x_coord]
          if tree_grid[y_coord][x_coord] > right_highest[y_coord]:
              right_highest[y_coord] = tree_grid[y_coord][x_coord]
          if tree_grid[y_coord][x_coord] > bottom_highest[y_coord]:
              bottom_highest[y_coord] = tree_grid[y_coord][x_coord]
    
    
    # if tree_grid[x_coord][y_coord] > top_highest[x_coord]:
    #     top_highest[x_coord] = tree_grid[x_coord][y_coord]
    #     increase = True

    #     if tree_grid[x_coord][y_coord] > left_highest[x_coord]:
    #         left_highest[x_coord] = tree_grid[x_coord][y_coord]
    #     if tree_grid[x_coord][y_coord] > right_highest[x_coord]:
    #         right_highest[x_coord] = tree_grid[x_coord][y_coord]
    #     if tree_grid[x_coord][y_coord] > bottom_highest[x_coord]:
    #         bottom_highest[x_coord] = tree_grid[x_coord][y_coord]

    # elif tree_grid[x_coord][y_coord] > left_highest[x_coord]:
    #     left_highest[x_coord] = tree_grid[x_coord][y_coord]
    #     increase = True

    #     if tree_grid[x_coord][y_coord] > top_highest[x_coord]:
    #         top_highest[x_coord] = tree_grid[x_coord][y_coord]
    #     if tree_grid[x_coord][y_coord] > right_highest[x_coord]:
    #         right_highest[x_coord] = tree_grid[x_coord][y_coord]
    #     if tree_grid[x_coord][y_coord] > bottom_highest[x_coord]:
    #         bottom_highest[x_coord] = tree_grid[x_coord][y_coord]

    # elif tree_grid[x_coord][y_coord] > right_highest[x_coord]:
    #     right_highest[x_coord] = tree_grid[x_coord][y_coord]
    #     increase = True

    #     if tree_grid[x_coord][y_coord] > left_highest[x_coord]:
    #         left_highest[x_coord] = tree_grid[x_coord][y_coord]
    #     if tree_grid[x_coord][y_coord] > top_highest[x_coord]:
    #         top_highest[x_coord] = tree_grid[x_coord][y_coord]
    #     if tree_grid[x_coord][y_coord] > bottom_highest[x_coord]:
    #         bottom_highest[x_coord] = tree_grid[x_coord][y_coord]

    # elif tree_grid[x_coord][y_coord] > bottom_highest[x_coord]:
    #     bottom_highest[x_coord] = tree_grid[x_coord][y_coord]
    #     increase = True

    #     if tree_grid[x_coord][y_coord] > left_highest[x_coord]:
    #         left_highest[x_coord] = tree_grid[x_coord][y_coord]
    #     if tree_grid[x_coord][y_coord] > right_highest[x_coord]:
    #         right_highest[x_coord] = tree_grid[x_coord][y_coord]
    #     if tree_grid[x_coord][y_coord] > top_highest[x_coord]:
    #         top_highest[x_coord] = tree_grid[x_coord][y_coord]

    return increase


with open('day_eight/day_eight_testcase.txt') as input:
    for line in input.readlines():
        line = line.strip()
        tree_row = []
        for num in line:
            tree_row.append(int(num))
        tree_grid.append(tree_row)

# for row in tree_grid:
#     print(row)
top_highest = []
for num in tree_grid[0]: top_highest.append(num)
bottom_highest = []
for num in tree_grid[-1]: bottom_highest.append(num)
left_highest = []
for row in tree_grid: left_highest.append(row[0])
right_highest = []
for row in tree_grid: right_highest.append(row[-1])

for row in tree_grid:
    if row == tree_grid[0] or row == tree_grid[-1]:
        temp = ''
        for num in row:
            temp += str(num)
            visible_trees += 1
    else:
        temp = ''
        for i in range(len(row)):
            if i == 0 or i == len(row) - 1:
                temp += str(row[i])
                visible_trees += 1
            else:
                if tree_checker(tree_grid.index(row), i):
                    temp += str(tree_grid[tree_grid.index(row)][i])
                    visible_trees += 1
                elif tree_checker(-(i + 1), -(tree_grid.index(row) + 1)):
                    temp += str(tree_grid[-(i + 1)][-(tree_grid.index(row) + 1)])
                    visible_trees += 1
                else:
                    temp += ' '
    print(temp)

#print(visible_trees)

for x in range(1, (len(tree_grid) - 1)):
    for y in range(1, (len(tree_grid) - 1)):
        if tree_checker(x, y):
            visible_trees += 1

for x in range(2, (len(tree_grid) - 1)):
    for y in range(2, (len(tree_grid) - 1)):
        if tree_checker(-x, -y):
            visible_trees += 1

print(visible_trees)
