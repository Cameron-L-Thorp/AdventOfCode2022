import regex as re

directories = {'/':{}}
directory_level = 0
last_dir = ['/']

def cmdln_reader(command):
    command = str(command).strip()
    input_char = '$'
    command = list(command.split(' '))
    dlevel = directory_level
    current_dir = last_dir[-1]
    
    try:
        if int(command[0]) != '':
            command[0] = int(command[0])
    except:
        pass

    if command[0] == input_char:
        if command[1] == 'cd':
            if command[2] != '..' and command[2] != '/':
                if command[2] not in directories:
                    directories[command[2]] = 0
                    dlevel += 1
                current_dir = command[2]

            elif command[2] == '..':
                dlevel -= 1
                
            elif command[2] == '/':
                dlevel = 0

        elif command[1] == 'ls':
            pass

    elif command[0] == 'dir':
        last_dir.append(command[1])

    elif type(command[0]) == int:
        if current_dir in directories.keys():
            directories[current_dir] += command[0]
        else:
            directories[current_dir] = command[0]

    else:
        print('Command not recognized.')    
    
    


with open('day_seven\day_seven_input.txt') as input:

    for command in input.readlines():
        cmdln_reader(command)

print(directories)