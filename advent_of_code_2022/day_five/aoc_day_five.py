#         [C] [B] [H]                
# [W]     [D] [J] [Q] [B]            
# [P] [F] [Z] [F] [B] [L]            
# [G] [Z] [N] [P] [J] [S] [V]        
# [Z] [C] [H] [Z] [G] [T] [Z]     [C]
# [V] [B] [M] [M] [C] [Q] [C] [G] [H]
# [S] [V] [L] [D] [F] [F] [G] [L] [F]
# [B] [J] [V] [L] [V] [G] [L] [N] [J]
#  1   2   3   4   5   6   7   8   9 

stack_one = ['B', 'S', 'V', 'Z', 'G', 'P', 'W']
stack_two = ['J', 'V', 'B', 'C', 'Z', 'F']
stack_three = ['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C']
stack_four = ['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B']
stack_five = ['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H']
stack_six = ['G', 'F', 'Q', 'T', 'S', 'L', 'B']
stack_seven = ['L', 'G', 'C', 'Z', 'V']
stack_eight = ['N', 'L', 'G']
stack_nine = ['J', 'F', 'H', 'C']

stack_dictionary = {1:stack_one, 2:stack_two, 3:stack_three, 4:stack_four, 5:stack_five, 6:stack_six, 7:stack_seven, 8:stack_eight, 9:stack_nine}

with open('day_five\day_five_input.txt') as input:
    

    #move # from # to #
    for command in input.readlines():
        temp_list = list(command.strip().split(' '))
        command_numbers = [temp_list[1], temp_list[3], temp_list[5]]
        # print(command_numbers)
        amount = int(command_numbers[0])
        origin_pile = int(command_numbers[1])
        destination_pile = int(command_numbers[2])
        crane_stack = []
        for i in range(0, amount):
            crane_stack.append(stack_dictionary[origin_pile].pop())
        
        #for adding the stack one at a time
        #stack_dictionary[destination_pile] += crane_stack

        #for adding stacks in order
        while len(crane_stack) > 0:
            stack_dictionary[destination_pile].append(crane_stack.pop())

#^ Not working
print(stack_one[-1], stack_two[-1], stack_three[-1], stack_four[-1], stack_five[-1], stack_six[-1], stack_seven[-1], stack_eight[-1], stack_nine[-1])
