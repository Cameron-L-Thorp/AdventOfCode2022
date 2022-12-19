with open('day_four_input.txt') as input:

    overlapped_pairs = 0

    for pair in input.readlines():
        ranges = pair.strip().split(',')
        pair1 = ranges[0].split('-')
        pair2 = ranges[1].split('-')

        pair1l = int(pair1[0])
        pair1h = int(pair1[1])
        pair2l = int(pair2[0])
        pair2h = int(pair2[1])

        #Didn't convert to ints at first -_-

        pair1_range = list(range(pair1l, (pair1h + 1)))
        pair2_range = list(range(pair2l, (pair2h + 1)))

        if ((pair1l <= pair2l) and (pair1h >= pair2h)) or ((pair1l >= pair2l) and (pair1h <= pair2h)):
            print(f"Pair1: {pair1} \nPair2: {pair2}")
            overlapped_pairs += 1

        

        elif ((pair1_range[-1] in pair2_range) or (pair2_range[-1] in pair1_range)) or ((pair1_range[0] in pair2_range) or (pair2_range[0] in pair1_range)):
            overlapped_pairs += 1

    print(overlapped_pairs)

        

