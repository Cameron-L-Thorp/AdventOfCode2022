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

## Day6:
This day, I used a function to check the next four characters, looping through the signal one character at a time. These characters are appended to a list only if they are unique, which is returned to the loop. The loop then measures the length of the returned list, if it is 4, then the signal position is recorded and the loop breaks. The same approach was taken for the second part, where it was a string of size 14.

## Day7:
I think this approach is likely non-optimized, but it was the first day that broke my brain at first. Initially and eventually, I attempted to parse through the commands, turning each one into a list and then sent through conditionals to check if it was a user command, a directory or a file that needed to be measured. After multiple attempts and using different angles, it ended up working properly when a function was called for each command. At this point however, I didn't trust that it was opperating correctly and was confused by the incorrect answer despite the number of directories existing being the same number that were measured. It all boiled down to an index issue, where one extra index was included in the conditionals, causing the directory level to be incorrect. This would add top-level files from the next directory. 
Unfortunately, many of the file names on the input were the same as directory names, or also existed with different sizes in a different directory. Eventaully it was solved though and part two was a matter of finding the current total size of the '/' directory, and then the smallest directory that could increase the free space to 30000000 of 70000000. This was accomplished by itterating through the sizes of each directory measured and finding the closest one to that threshold.

## Day8:
Currently unsolved. My program can accurately measure the interior trees from the top-left, or top-right, but seems to have issues when trying to compare values from the bottom, or right sides. I haven't been able to isolate where the issue is coming from as it occasionally produces the correct answer for the test case and then provides the wrong answer for the input. I think to solve this I need to get more comfortable with matrix manipulation (about half the time I spent on this one, I wasn't using the indecies for the multi-dimentional lists properly -_-)
