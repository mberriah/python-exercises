## Exercise 1
Define a function `surface_circle(r)`. This function must return the surface area of a circle given the radius `r` as an argument.  
For example, executing the instruction : `print(surfCircle(2.5))` should give the result: `19.63495...`  
[Answer](./ex01.py)  

## Exercise 2
Define a function `volume_box(x1,x2,x3)` which returns the volume of a parallelepipedic whose three dimensions `x1`, `x2`, `x3` are given as arguments.  
For example, executing the instruction :  
`print(volume_box(5.2, 7.7, 3.3))` should give the result: `132.132`.  
[Answer](./ex02.py)

## Exercise 3
Define a function `maximum(n1,n2,n3)` which returns the largest of 3 numbers `n1`, `n2`, `n3` given as arguments.  
For example, executing the instruction :  
`print(maximum(2,5,4))` should give the result: `5`.  
[Answer](./ex03.py)

## Exercise 4
Define a function `count_char(c,str)` which returns the number of times the character `c` is encountered in the string `str`.  
For example, executing the instruction :  
`print(count_char('e', 'This sentence is an example'))` should give the result: `5`.  
[Answer](./ex04.py)  

## Exercise 5
Define a function `index_max(list)` which returns the index of the element with the highest value in the list passed as an argument.  
Example of use:  
`serie = [5, 8, 2, 1, 9, 3, 6, 7]`  
`print(index_max(serie))`  
`4`  
[Answer](./ex05.py)

## Exercise 6
Define a `name_month(n)` function which returns the name of the nth month of the year.  
For example, executing the instruction :  
`print(month_mame(4))` should give the result: `April`.  
[Answer](./ex06.py)

## Exercise 7
Modify the `volume_box(x1,x2,x3)` function that you defined in a previous exercise, so that it can be called with three, two, one or even no arguments. Use default values of `10` for these.  
For example,  
`print(volume_box())` should give the result: `1000`  
`print(volume_box(5.2))` should give the result: `520.0`  
`print(volume_box(5.2, 3))` should give the result: `156.0`  
[Answer](./ex07.py)

## Exercise 8
Modify the `volume_box(x1,x2,x3)` function above so that it can be called with one, two or three arguments. If only one is used, the box is considered to be cubic (the argument being the edge of this cube). If two are used, the box is considered to be a prism with a square base (in which case the first argument is the side of the square, and the second the height of the prism). If three arguments are used, the box is considered to be a parallelepiped.  
For example  
`print(volume_box())` should give the result: `-1` (indicating an error)  
`print(volume_box(5.2))` should give the result: `140.608`  
`print(volume_box(5.2, 3))` should give the result: `81.12`  
`print(volume_box(5.2, 3, 7.4))` should give the result : `115.44`  
[Answer](./ex08.py)

## Exercise 9
Define a function `change_char(str, c1, c2, sart, end)` which replaces all the characters `c1` with characters `c2` in the string `str`, starting from the subscript `start` and ending at the subscript `end`, although the last two arguments can be omitted (in which case the string is processed from one end to the other).  
[Answer](./ex09.py)  

## Exercise 10
Define a function `elem_max(list, start, end)` which returns the element with the highest value in the list passed. The two arguments `start` and `end`will indicate the indices between which the search should be performed, and each of them can be omitted (as in the previous exercise).  
Examples of the expected functionality:  
`serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]`  
`print(eleMax(serie))`  
`9`  
`print(eleMax(serie, 2, 5))`  
`7`  
`print(eleMax(serie, 2))`  
`8`   
`print(eleMax(serie, end =3, start =1))`  
`6`  
[Answer](./ex10.py)