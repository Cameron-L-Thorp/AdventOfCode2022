all_commands = []
cycle_counter = 0
freq_value = 1
total_signal_strength = 0
crt_rows = []
pixel_row = ''

def cycle_checker(count):
    signal_strength = 0
    if count == 20:
        signal_strength = count * freq_value
        print(f"{freq_value} * {count} = {signal_strength}")
    if count == 60:
        signal_strength = count * freq_value
        print(f"{freq_value} * {count} = {signal_strength}")
    if count == 100:
        signal_strength = count * freq_value
        print(f"{freq_value} * {count} = {signal_strength}")
    if count == 140:
        signal_strength = count * freq_value
        print(f"{freq_value} * {count} = {signal_strength}")
    if count == 180:
        signal_strength = count * freq_value
        print(f"{freq_value} * {count} = {signal_strength}")
    if count == 220:
        signal_strength = count * freq_value
        print(f"{freq_value} * {count} = {signal_strength}")
    return signal_strength

def pixel_drawer(freq, counter):
    char = ''
    if (freq % 40 == 1 and (counter % 40 == 0 or counter % 40 == 1)) or (freq % 40 == 0 and (counter % 40 == 38 or counter % 40 == 39)):
        char += '#'
    elif (freq >= (counter % 40) - 1) and (freq <= (counter % 40) + 1):
        char += '#'
    else:
        char += '.'
        
    return char
    



with open('day_ten/day_ten_input.txt') as input:
    for command in input.readlines():
        command = command.strip().split(' ')
        all_commands.append(command)

# for command in all_commands:
#     if command[0] == 'addx':
#         print(command[1])

for command in all_commands:
    
    if command[0] == 'noop':
        pixel_row += pixel_drawer(freq_value, cycle_counter)
        cycle_counter += 1
        
        if len(pixel_row) == 40:
            crt_rows.append(pixel_row)
            pixel_row = ''
        if cycle_counter == 20 or ((cycle_counter - 20) % 40) == 0:
            total_signal_strength += cycle_checker(cycle_counter)
        # if (freq_value == cycle_counter % 40) or (freq_value + 1 == cycle_counter % 40) or (freq_value - 1 == cycle_counter % 40):
        #     pixel_row += '#'
        # else:
        #     pixel_row += '.'
        # if cycle_counter % 40 == 0:
        #     crt_rows.append(pixel_row)
        #     pixel_row = ''
    if command[0] =='addx':
        pixel_row += pixel_drawer(freq_value, cycle_counter)
        cycle_counter += 1
        
        if len(pixel_row) == 40:
            crt_rows.append(pixel_row)
            pixel_row = ''
        if cycle_counter == 20 or ((cycle_counter - 20) % 40) == 0:
            total_signal_strength += cycle_checker(cycle_counter)
        # if (freq_value == cycle_counter % 40) or (freq_value + 1 == cycle_counter % 40) or (freq_value - 1 == cycle_counter % 40):
        #     pixel_row += '#'
        # else:
        #     pixel_row += '.'
        # if cycle_counter % 40 == 0:
        #     crt_rows.append(pixel_row)
        #     pixel_row = ''
        pixel_row += pixel_drawer(freq_value, cycle_counter)
        cycle_counter += 1
        
        if len(pixel_row) == 40:
            crt_rows.append(pixel_row)
            pixel_row = ''
        if cycle_counter == 20 or ((cycle_counter - 20) % 40) == 0:
            total_signal_strength += cycle_checker(cycle_counter)
        # if (freq_value == cycle_counter % 40) or (freq_value + 1 == cycle_counter % 40) or (freq_value - 1 == cycle_counter % 40):
        #     pixel_row += '#'
        # else:
        #     pixel_row += '.'
        freq_value += int(command[1])
        # if cycle_counter % 40 == 0:
        #     crt_rows.append(pixel_row)
        #     pixel_row = ''
    
            
print(cycle_counter)
print(total_signal_strength)

for row in crt_rows:
    print(row)

print(str(0%40), str(1 % 40), str(61 % 40))