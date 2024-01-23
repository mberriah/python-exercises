## Exercise 1
Write a script that cycles through the values in the 'day' list 25 times:  
`day = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']`  
To do this, use two variables (one for iteration and the other to retrieve the index of the list element) and the modulo operator.  
[Answer](./ex06-01.py)  

## Exercise 2  
Let be the following lists:  
`t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]`  
`t2 = ['January', 'February', 'March', 'April', 'May', 'June',
 July', 'August', 'September', 'October', 'November', 'December']`  
Write a small program to create a new t3 list. This should contain all the elements of the two lists, alternating them so that each month name is followed by the the corresponding number of days:  
`['January',31,'February',28,'March',31, etc...]`.  
[Answer](./ex06-02.py)

## Exercise 3
Write a program that "cleanly" displays all the elements of a list. If you were to apply it to the list `l1` in the exercise above, for example, you'd get :  
`January February March April May June July August September October November
December`.  
[Answer](./ex06-03.py)

## Exercise 4
Write a program to find the largest element in a given list. 
For example, if applied to the list `[32, 5, 12, 8, 3, 75, 2, 15]`, this program should display:  
`The largest element in this list has the value 75`.  
[Answer](./ex06-04.py)  

## Exercise 5
Write a program that analyzes all the elements of a list of numbers one by one to generate two new lists. One will contain
only the even numbers of the initial list, and the other the odd numbers. 
For example, if the initial list is the one from the previous exercise, the program will have to construct an even list containing `[32, 12, 8, 2]`, and an odd list containing `[5, 3, 75, 15]`.  
[Answer](./ex06-05.py)  

## Exercise 6
Write a program that analyzes all the elements of a word list one by one (for example: `['John', 'Maximilian', 'Brigitte', 'Sonia', 'John-Peter', 'Sandra']`) to generate two new lists. 
One will contain words with less than 6 characters, the other will contain words of 6 characters or more.
