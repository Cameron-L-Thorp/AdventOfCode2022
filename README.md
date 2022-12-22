# AdventOfCode2022

My work on the 2022 Advent of code, mistakes included!

https://adventofcode.com/


## Day1:
The code for day one parses through the input data, and for each elf, finds the total value of calories they are carrying, then checks to see if they are carrying the largest amout of calories. Once a '\n' is found (signifying the end of that elf's snacks) the id of the elf is incremented, and the calories are reset for the next calorie total to start.
In order to find the highest three elves, the list of calorie totals is sorted, reversed, and then the sum of the first tree indecies is taken (could be done without 'reverse' with negative indecies in python).

## Day2:
For part one, three conditionals were used to determine then result of the match, as there are three possible options ('rock', paper', or 'scissors'). Once a conditional is met, the score is added based on the move and win result.
For part two, each option from the oppnent can be responded to with three different player options. This resulted in an additional three nested conditionals but a definitive score.
