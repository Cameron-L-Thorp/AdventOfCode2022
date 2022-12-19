with open('day_one\day_one_input.txt') as input:
    calories = 0
    max_calories = 0
    elf = 1
    snack_elf = 0
    calories_per = []
    for line in input.readlines():
        if line != '\n':
            calories += int(line)

            if calories > max_calories:
                max_calories = calories
                snack_elf = elf

        elif line == '\n':
            print(f"Elf {elf} has {calories} calories.")
            calories_per.append(calories)
            elf += 1
            calories = 0
        
    print(f"Elf {snack_elf} had the most snacks ({max_calories} calories!)")

    calories_per.sort(reverse=True)
    top_three_total = calories_per[0] + calories_per[1] + calories_per[2]
    print(f"The top three elves are carrying {top_three_total} calories.")
