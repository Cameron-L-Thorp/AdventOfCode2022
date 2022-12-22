# AdventOfCode2022

My work on the 2022 Advent of code, mistakes included!

https://adventofcode.com/


##Day1:
The code for day one parses through the input data, and for each elf, finds the total value of calories they are carrying, then checks to see if they are carrying the largest amout of calories. Once a '\n' is found (signifying the end of that elf's snacks) the id of the elf is incremented, and the calories are reset for the next calorie total to start.
In order to find the highest three elves, the list of calorie totals is sorted, reversed, and then the sum of the first tree indecies is taken (could be done without 'reverse' with negative indecies in python).
