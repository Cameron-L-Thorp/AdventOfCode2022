with open('day_two\day_two_input.txt') as input:
    rps_opp = {'A':1, 'B':2, 'C':3}
    rps_you = {'X':1, 'Y':2, 'Z':3}
    score_helper = (1, 2, 3)
    score = 0
    round_num = 0
    for line in input.readlines():
        round = list(line.strip().split(' '))
        
        #For part one
        # if (round[0] == "A" and round[1] == "X") or (round[0] == "B" and round[1] == "Y") or (round[0] == "C" and round[1] == "Z"):
        #     score += (rps_you[round[1]] + 3)

        # elif (round[0] == "A" and round[1] == "Z") or (round[0] == "B" and round[1] == "X") or (round[0] == "C" and round[1] == "Y"):
        #     score += (rps_you[round[1]])

        # else:
        #     score += (rps_you[round[1]] + 6)

        #For part two

        if round[1] == "X":
            if round[0] == "A":
                score += 3
            elif round[0] == "B":
                score += 1
            elif round[0] == "C":
                score += 2
        elif round[1] == "Y":
            if round[0] == "A":
                score += 4
            elif round[0] == "B":
                score += 5
            elif round[0] == "C":
                score += 6
        elif round[1] == "Z":
            if round[0] == "A":
                score += 8
            elif round[0] == "B":
                score += 9
            elif round[0] == "C":
                score += 7

 
    print(f"Total score: {score}.")



        # print(f"{round[0]} : {round[1]}")
        # choice = 0
        # result = 0
        
        # opponent_choice = rps_opp[round[0]]
        # your_choice = rps_you[round[1]]

        # if your_choice == opponent_choice:
        #     score += (your_choice + 3)

        # if your_choice < opponent_choice:
        #     score += (your_choice)

        # if your_choice > opponent_choice:
        #     score += (your_choice + 6)

        # print(score)

        # if rps_you[round[1]] == rps_opp[round[0]]:
        #     choice = rps_you[round[1]]
        #     result = 3
        #     round_num += 1
        #     print(round_num)
        #     print(f"Choice: {choice}, Result: {result}, Total {(choice + result)}")
        #     score += (choice + result)

        # elif rps_you[round[1]] < rps_opp[round[0]]:
        #     choice = rps_you[round[1]]
        #     result = 0
        #     round_num += 1
        #     print(round_num)
        #     print(f"Choice: {choice}, Result: {result}, Total {(choice + result)}")
        #     score += (choice + result)

        # elif rps_you[round[1]] > rps_opp[round[0]]:
        #     choice = rps_you[round[1]]
        #     result = 6
        #     round_num += 1
        #     print(round_num)
        #     print(f"Choice: {choice}, Result: {result}, Total {(choice + result)}")
        #     score += (choice + result)

        # else:
        #     print("Something isn't adding up.")

    print(f"Total score: {score}")