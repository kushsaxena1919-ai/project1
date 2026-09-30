Simple python calculator



A calculator written in the python language that accepts two numbers and an operator from the user and prints the result of the operation on the screen



Features



1. Addition (‘+’)

2. Subtraction (‘-’)

3. Multiplication (‘’)

4. Division (‘/’)



5. Division by ‘0’ is handled

6. Operator is checked for validity

7. Decimal numbers are handled by using float

The requirements

1. Python 3.x



How to run



1. Save the code in a file named ‘calculator.py’

2. Open the terminal in the folder where the file is saved

3. Run the command ‘python calculator.py’



How to use

1. The program will ask for the first number, operator (‘+’, ‘-’, ‘’, or ‘/’), and the second number

2. Then, the result of the operation will be printed on the screen

Examples

Enter the first number 10

Enter operator(+,-,/,):

Enter the second number 5

Result: 50.0

Enter the first number 8

Enter operator(+,-,/,): /

Enter the second number 0

Result: we cannot divide by the zero

Enter the first number 4

Enter operator(+,-,/,): %

Enter the second number 2

Result: invalid operator

How it works

1. Numbers are read as float

2. Operator is read as a string

3. If / elif / else is used to determine which operator is entered and calculate the result

4. If the operator is ‘/’ then the second number is checked whether it is 0

5. Finally, the result is printed

What to change or add

1. You can make the program run in a loop so that it does not close after one calculation

2. You can add other operators such as power (‘’), modulus (‘%’), and floor division (‘//’)

3. You can make the program run by using try / except to handle exceptions

4. You can make the code neater by putting the code in a function

Author

Your Name

License

All rights reserved for learning purposes. However, you are free to use and modify it for learning purposes.