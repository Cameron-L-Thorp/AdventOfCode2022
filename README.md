# AdventOfCode2022

My work on the 2022 Advent of code, mistakes included!

https://adventofcode.com/


## Day1:
The code for day one parses through the input data, and for each elf, finds the total value of calories they are carrying, then checks to see if they are carrying the largest amout of calories. Once a '\n' is found (signifying the end of that elf's snacks) the id of the elf is incremented, and the calories are reset for the next calorie total to start.
In order to find the highest three elves, the list of calorie totals is sorted, reversed, and then the sum of the first tree indecies is taken (could be done without 'reverse' with negative indecies in python).

## Day2:
For part one, three conditionals were used to determine then result of the match, as there are three possible options ('rock', paper', or 'scissors'). Once a conditional is met, the score is added based on the move and win result.
For part two, each option from the oppnent can be responded to with three different player options. This resulted in an additional three nested conditionals but a definitive score.

## Day3:
Initially, a dicionary is set to define the values of the different items in a pack. Since the packs are always even in items, and have the same amount of items in each pouch, I split the packs in half to itterate through one side and check if each item was containted in the other. Once found, the value of that item is added to the total of item priorities and the loop is broken to move onto the next pack (this break is to ensure that only one copy is added to the sum).
For part two, every third packs' items are checked against the next two and once an item is found in all three, that item is added to the badges (a sum of all common items between groups).

## Day4:
The numbers given in each input pair are used to create a range, and then turned into a list of those numbers. 
Part one measures to see if either range fully contains the other.
Part two checks to see if they overlap at all based on the 0th and -1st indicies.


## Day5:
The stacks of crates provided were turned into lists with the top item located at index -1 so the pop method can be used effectively on the python collections. 
For part one, the items are popped and appended directly to the target pile as the crane can only move one crate at a time. 
Part two allows for the movement of multiple crates, while maintaining the order of the stack they pick up. To accomplish this, a temp stack is created that the crates are popped into and then popped out of, into the target pile allowing for the crates to maintain their original order.
This was done to emulate stacks in python, but it would likely have been simpler to use negative indecies to append a collection range, and then remove them from their original list.
