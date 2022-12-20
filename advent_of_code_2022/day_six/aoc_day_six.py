def unique(collection):
    unique_collection = []
    for x in collection:
        if x not in unique_collection:
            unique_collection.append(x)

    return unique_collection

with open('day_six\day_six_input.txt') as input:

    signal = input.read()
    signal_position = 0
    for i in range(len(signal)):
        sub_signal = unique(signal[i:(i+14)])
        
        if len(sub_signal) == 14:
            print(sub_signal)
            signal_position = i + 14
            break

    print(signal_position)
        


