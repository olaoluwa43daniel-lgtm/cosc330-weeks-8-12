COSC 330 - WEEK 8 HOME WORK ASSIGN
Oluwafemi Olaoluwa

SUBMISSION STATUS
The Python programs, Makefile, and questions 1-3 are implemented and tested
locally on Linux. The AWS account/EC2 Ubuntu setup has NOT been completed
or verified for this submission. AWS_SETUP.txt contains the remaining steps.
No AWS screenshots or cloud execution results are claimed.

FILES AND REQUIREMENTS
hello.py: prints Hello, world!
add.py: reads two integers and returns their sum.
calculate.py: subtracts or multiplies two integers.
q1_add_shell.sh: repeats add/exit.
q2_calculator_shell.sh: repeats add/subtract/multiply/exit.
q3_menu_shell.sh: numbered menu plus listing a requested directory.
Makefile: runs each Python program and each shell script.
TEST_RESULTS.txt: actual local checks and recorded output.

RUNNING
Extract the ZIP and open a terminal in the Week8_Homework directory:

    make hello
    make q1
    make q2
    make q3

For addition, enter each integer on a separate line.
Use make add, make subtract, or make multiply to run one operation directly.

EXPLANATION
Each shell uses a while loop to keep prompting. The case statement selects
the command. Exit uses break to leave the loop. EOF also ends the loop.
Arithmetic is performed by Python, launched through a Makefile target.
Subtraction computes the first number minus the second.
The third menu reads a directory path, checks that it exists, and runs ls.
Quoted paths allow directory names with spaces. Invalid choices and invalid
integers print an error. Only predefined commands are run.

QUESTION 4
The assignment says not to publish question 4. No question 4 solution or
copied Brennan shell code is included in this submission.
