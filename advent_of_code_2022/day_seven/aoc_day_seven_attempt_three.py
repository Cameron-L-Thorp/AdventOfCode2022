#Take the name of each dir in order without a serial
#find the next cd that calls that dir name
#calc all values in dir and go deeper if needed
#repeat?

def directory_add(name, index):
    dir_level = 1
    directory_values[name] = 0
    for command in all_commands[index + 1:len(all_commands)]:
        if dir_level > 0:
            try:
                if int(command[0]) != '':
                    command[0] = int(command[0])
            except:
                pass
            
            if command[1] == 'cd' and command[2] == '..':
                dir_level -= 1
            elif type(command[0]) == int:
                directory_values[name] += command[0]
            elif command[1] == 'cd':
                dir_level += 1


all_directories = []
all_commands = []
directory_values = {}
with open('day_seven/day_seven_input.txt') as input:
    for command in input.readlines():
        all_commands.append(list(command.strip().split(' ')))
    
    for command in all_commands:
        if command[0] == 'dir':
            all_directories.append(command[1])
    # index = 0
    # for command in all_commands:
    #     if command[0] == 'dir':
    #         directory_values[command[1] + str(index)] = 0
    #         index += 1
# for command in all_commands:
#     print(command)

dir_index = 0
index = 0
for command in all_commands:
    if command[1] == 'cd' and command[2] in all_directories:
        directory_add((str(command[2]) + str(dir_index)), index)
        dir_index += 1
    index += 1

all_directories.reverse()

for dir in all_directories:
    print(dir)

for dirval in directory_values.items():
    print(dirval)

sum_of_under_hundred = 0
for value in directory_values.values():
    if value <= 100000:
        sum_of_under_hundred += value

print(sum_of_under_hundred)


space_used = 0
for command in all_commands:
    
    try:
        if int(command[0]) != '':
            space_used += command[0]
    except:
        pass

print(space_used)

delete_space = 10000000
for dir in directory_values.values():
    if ((space_used - dir) < 40000000) and (dir < delete_space):
        delete_space = dir

print(delete_space)