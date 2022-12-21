tree_graph = []

with open('day_eight/day_eight_testcase.txt') as input:
    for tree_row in input.readlines():
        tree_row = tree_row.strip()
        tree_nums = []
        for tree in tree_row:
            tree_nums.append(int(tree))
        tree_graph.append(tree_nums)

#[1, 2, 3] first index for list
# second index for item in list
#list[0][2] = 3

visible_trees = 0
recorded_trees = []

left_highest = []
for row in tree_graph: left_highest.append(row[0])
right_highest = []
for row in tree_graph: right_highest.append(row[-1])
top_highest = []
for tree in tree_graph[0]: top_highest.append(tree)
bottom_highest = []
for tree in tree_graph[-1]: bottom_highest.append(tree)

# for row in tree_graph:
#     if tree_graph.index(row) == 0 or tree_graph.index(row) == -1:
#         visible_trees += len(row)
#         continue
#     for tree in range(1, len(row)-1):
#         if row[tree] > left_highest[tree_graph.index(row)]:
#             left_highest[tree_graph.index(row)] = row[tree]
#             visible_trees += 1
#             recorded_trees.append([tree_graph.index(row), tree])
#         if row[-tree] > right_highest[tree_graph.index(row)]:
#             right_highest[tree_graph.index(row)] = row[-tree]
#             visible_trees += 1
#             recorded_trees.append([tree_graph.index(row), tree])

# for tree in range(1, len(tree_graph) - 1):
#     for row in tree_graph[1:-1]:
#         index = 1
#         if row[tree] > top_highest[tree]:
#             top_highest[tree] = row[tree]
#             visible_trees += 1
#             recorded_trees.append([row[index], tree])
#         if row[-(tree + 1)] > bottom_highest[tree]:
#             bottom_highest[tree] = row[-(tree + 1)]
#             visible_trees += 1
#             recorded_trees.append([row[index], tree])
#         index += 1

print(recorded_trees)
print(visible_trees)

# for line in tree_graph:
#     print(line)