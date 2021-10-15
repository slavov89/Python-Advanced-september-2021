# Python-Advanced-september-2021
Tasks completed during Python advanced course at SoftUni


    1. Negative vs Positive
You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from the positive. Find the total sum of the negatives and positives, and print the following:
    • On the first line, print the sum of the negatives
    • On the second line, print the sum of the positives
    • On the third line:
        ◦ If the absolute negative number is larger than the positive number:
	"The negatives are stronger than the positives"
        ◦ If the positive number is larger than the absolute negative number:
	"The positives are stronger than the negatives"
Note: you will not receive any zeroes in the input.

    2. Odd or Even
On the first line, you will receive a command - "Odd" or "Even". You will receive a sequence of numbers (integers) on the second line, separated by a single space.
    • If the command is "Odd", print the sum of the odd numbers multiplied by the count of all numbers.
    • If the command is "Even", print the sum of the even numbers multiplied by the count of all numbers.

    3. Arguments Length
Create a function called args_length() that returns the number of the arguments. Submit only the function in the judge system.

    4. Concatenate
Write a function called concatenate() that receives some strings, concatenates them, and returns the result.

    5. Even or Odd
Create a function called even_odd() that can receive a different quantity of numbers and a command at the end. The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list. Submit only the function in the judge system.

    6. Function Executor
Create a function called func_executor() that can receive a different number of tuples, each of which will have exactly 2 elements: first will be a function, and the second will be a tuple of the arguments that need to be passed to that function. Create a list that will contain all the results of the executed functions with their corresponding arguments and return it after executing all functions. For more clarification, see the examples below. Submit only your function in the judge system.

    7. Keyword Arguments Length
Create a function called kwargs_length() that can receive some keyword arguments and return their length. Submit only the function in the judge system.

    8. Age Assignment
Create a function called age_assignment that receives a different number of names and a different number of key-value pairs. The key will be a single letter (the first letter of each name) and the value - a number (age). Find its first letter in the key-value pairs for each name and assign the age to the person's name. It the end, return a dictionary with all the names and ages as shown in the example. Submit only the function in the judge system.

    9. Recursion Palindrome
Write a recursive function called palindrome() that will receive a word and an index (always 0). Implement the function, so it returns "{word} is a palindrome" if the word is a palindrome and "{word} is not a palindrome" if the word is not a palindrome using recursion. Submit only the function in the judge system.

    10. Recursive Power
Create a recursive function called recursive_power() which should receive a number and a power. Using recursion, return the result of number ** power. Submit only the function in the judge system.

    11. *Fill the Box
Write a function called fill_the_box that receives a different number of arguments representing:
    • the height of a box
    • the length of a box
    • the width of a box
    • n-times a different number of cubes with exact size 1 x 1 x 1
    • a string "Finish"
Your task is to fill the box with the given cubes until the current argument equals "Finish".
Note: Submit only the function in the judge system
Input
    • There will be no input. Just parameters passed to your function.
Output
The function should return a string in the following format:
    • If, at the end, there is free space left in the box, print:
        ◦ "There is free space in the box. You could put {free space in cubes} more cubes."
    • If there is no free space in the box, print:
        ◦ "No more free space! You have {cubes left} more cubes."


    12. *Math Operations
Write a function named math_operations that receives a different number of integers as arguments and 4 keyword arguments. The keys will be single letters: "a", "s", "d", "m", and the values will be numbers.
You need to take each integer argument from the sequence and do mathematical operations as follows:
    • The first element should be added to the value of the key "a" 
    • The second element should be subtracted from the value of the key "s" 
    • The third element should be divisor to the value of the key "d" 
    • The fourth element should be multiplied by the value of the key "m"
    • Each result should replace the value of the corresponding key
    • You must repeat the same steps consecutively until you run out of numbers
Beware: You cannot divide by 0. If the operation could throw an error, you should delete the element from the sequence and continue to the next operation.
For more clarifications, see the examples below.
Note: Submit only the function in the judge system
Input
    • There will be no input. Just parameters passed to your function.
    • All of the given numbers will be valid integers in the range [-100, 100]
Output
    • The function should return the final dictionary
