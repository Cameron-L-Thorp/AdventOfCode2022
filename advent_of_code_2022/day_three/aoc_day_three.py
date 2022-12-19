priorities = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}

with open('day_three/day_three_input.txt') as input:

    priority_sum = 0

    for pack in input.readlines():
        pack = pack.strip()
        #print(len(pack))
        middle = int(len(pack) / 2)
        pouch_one = list(pack[0:middle])
        pouch_two = list(pack[middle: int(len(pack))])
        if len(pouch_one) != len(pouch_two):
            #print("packs not even")
            break
        
        for item in pouch_one:
            if item in pouch_two:
                #print(f"{item} : {priorities[item]}")
                priority_sum += priorities[item]
                break
    
    print(priority_sum)

    # for item in range(len(pouch_one)):
        #     for x in range(len(pouch_two)):
        #         if pouch_one[item] == pouch_two[x]:
        #             print(f"{pouch_one[item]} : {priorities[pouch_one[item]]}")
        #             found = True
        #             break



with open('day_three/day_three_input.txt') as group_input:

    badge_sum = 0

    groups = []
    pack_counter = 0
    group_counter = 1

    for pack in group_input.readlines():
        groups.append(pack.strip())
        pack_counter += 1

        if pack_counter == 3:
            for i in groups[0]:
                if i in groups[1] and i in groups[2]:
                    print(f"{group_counter}: {i}")
                    badge_sum += priorities[i]
                    break
                



            print(f"Group {group_counter}: {groups}")
            group_counter += 1
            pack_counter = 0
            groups = []

    print(badge_sum)