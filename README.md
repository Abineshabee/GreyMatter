# GreyMatter Programming Language

GreyMatter is a **toy programming language interpreter implemented in Python**. The language is designed to help beginners learn programming concepts quickly and easily through a simplified syntax and interactive execution environment.

GreyMatter focuses on teaching fundamental programming concepts such as **variables, loops, functions, conditionals, and user input** while demonstrating how interpreters work internally.

---

# Inspiration

The **GreyMatter programming language** was inspired by the character **Grey Matter** from the animated series **Ben 10**.

In the series, Grey Matter represents intelligence, analytical thinking, and problem-solving abilities. This idea inspired the creation of a programming language that encourages logical thinking and experimentation while learning programming fundamentals.

---

# Motivation

Learning programming can be difficult for beginners due to complex syntax and unfamiliar concepts. GreyMatter was developed to:

* Simplify programming syntax
* Help beginners understand programming logic
* Demonstrate interpreter design concepts
* Provide a lightweight experimental programming environment
* Encourage exploration of language design and systems programming

---

# Features

* Simple and beginner-friendly syntax
* Python-based interpreter
* Interactive command-line interface
* Variable assignments
* Arithmetic operations
* Conditional statements
* Loops (WHILE, FOR)
* User input and output
* Function definitions
* Built-in helper utilities
* Dictionary-style storage using **BRAINSTORM**
* Educational interpreter implementation

---

# Tech Stack

Language

* Python

Concepts Implemented

* Interpreter design
* Runtime execution
* Custom scripting syntax
* Control flow
* Function handling
* Command-line interpreter

---

# Installation

Clone the repository

```bash
git clone https://github.com/Abineshabee/GreyMatter.git
```

Navigate to the directory

```bash
cd GreyMatter
```

Check Python installation

```bash
python --version
```

---

# Running GreyMatter

### Run a program file

```bash
python app.py calculator.txt
```

### Run interactive CLI

```bash
python GreyMatter.py
```

---

# CLI Example

```
$ GreyMatter <--version 0.01 <>

$ Release On Sept 25 <--@--> 2024 <>

________________________________________

  ╔═╗╦═╗╔═╗╦ ╦╔╦╗╔═╗╔╦╗╔╦╗╔═╗╦═╗
  ║ ╦╠╦╝║╣ ╚╦╝║║║╠═╣ ║  ║ ║╣ ╠╦╝
  ╚═╝╩╚═╚═╝ ╩ ╩ ╩╩ ╩ ╩  ╩ ╚═╝╩╚═
________________________________________
```

Example interaction

```
-> PRINT("hello World")

hello World

-> x = 1

-> WHILE ( x <= 10 ){
-> PRINT( x )
-> x += 1
-> }

1
2
3
4
5
6
7
8
9
10
```

---

# Language Syntax

## Variables

Variables are dynamically created during assignment.

```
x = 5
y = 6
PRINT(x + y)
```

Output

```
11
```

---

# Input and Output

```
name = INPUT("Enter your name : ")
PRINT("Hello ", name)
```

---

# Data Storage (BRAINSTORM)

GreyMatter includes a built-in storage system similar to dictionaries.

```
x , y , z = 1 , 2 , 3

BRAINSTORM.READ(x)
BRAINSTORM.READ(y)
BRAINSTORM.READ(z)

x , y , z = 4 , 5 , 6

BRAINSTORM.WRITE(x)
BRAINSTORM.WRITE(y)
BRAINSTORM.WRITE(z)

BRAINSTORM.GET()
```

---

# Conditional Statements

```
IF (x > 10) {
    PRINT("Large number")
}
ELSE {
    PRINT("Small number")
}
```

---

# Loops

## WHILE Loop

```
x = 1

WHILE (x <= 5) {

   PRINT(x)
   x += 1

}
```

---

## FOR Loop

```
FOR(i = 0 ; i <= 10 ; i++){
   PRINT(i)
}
```

---

# Functions

Functions are defined using the **FUNCTION** keyword.

```
FUNCTION add(x , y){

   result = x + y
   FEEDBACK(result)

}
```

Example usage

```
sum = add(5 , 6)
PRINT(sum)
```

---

# Example Programs

## Calculator

```
FUNCTION add ( x , y ) {
    c = x + y
    FEEDBACK(c)
}
```

Users can choose operations and perform calculations interactively.

---

## Fibonacci Series

```
FUNCTION fibonacci(n){

   a = 0
   b = 1

   FOR(i = 0 ; i <= n ; i++){

       PRINT(a)

       temp = a
       a = b
       b = temp + b

   }

}
```

---

## Prime Number Checker

```
FUNCTION isprime(n){

   flag = 1

   FOR(2 , n){

      IF(n % fori == 0){
         flag = 0
      }

   }

   FEEDBACK(flag)

}
```

---

## Palindrome Checker

```
str = INPUT("Enter The String : ")

len = LEN(str)
result = ""

FOR(i = len - 1 ; i >= 0 ; i--){

   temp = str.FASTTRACK(i)
   result += temp

}

PRINT(result)
```

---

# Built-in Utilities

| Function    | Description                |
| ----------- | -------------------------- |
| PRINT()     | Output values              |
| INPUT()     | User input                 |
| INT()       | Integer conversion         |
| LEN()       | String length              |
| ECHO        | Print empty line           |
| FEEDBACK()  | Return value from function |
| FASTTRACK() | Character indexing         |

---

# Project Structure

```
GreyMatter
│
├── GreyMatter.py
├── app.py
├── examples
│   ├── calculator.txt
│   ├── fibonacci.txt
│
└── README.md
```

---

# Learning Outcomes

This project helps understand:

* Programming language design
* Interpreter execution model
* Control flow parsing
* Function execution
* CLI interpreter development
* Python systems programming

---

# Future Improvements

Planned improvements include:

* Better error handling
* Standard library support
* Modules and packages
* Debugging tools
* Bytecode interpreter
* Performance optimization
* Syntax highlighting

---

# Author

Abinesh N

GitHub
[https://github.com/Abineshabee](https://github.com/Abineshabee)

---

# License

This Project Is Created For Educational Purposes.

---

