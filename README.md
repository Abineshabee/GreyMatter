
---

# GreyMatter Programming Language

GreyMatter is a lightweight experimental programming language designed and implemented in Python for educational and learning purposes. The main objective of the GreyMatter language is to help beginners understand the core concepts behind programming language design, interpreters, lexical analysis, parsing, and runtime execution.

The language provides a simple and expressive syntax that allows developers and students to write programs easily while exploring how a custom programming language works internally. GreyMatter supports many fundamental programming constructs including variables, arithmetic expressions, loops, conditional statements, functions, and built-in utilities.

GreyMatter focuses on simplicity, creativity, and educational exploration. Instead of building a highly optimized production language, the goal is to demonstrate how a programming language can be created from scratch using Python.

The project was created to help learners explore topics such as:

* Interpreter design
* Programming language implementation
* Abstract Syntax Tree execution
* Parsing and lexical analysis
* Runtime evaluation of expressions

GreyMatter is implemented using Python and parsing tools based on **SLY**, which provides an efficient way to build lexers and parsers.

---

# Inspiration

The name **GreyMatter** and the design philosophy of this language are inspired by the intelligent alien character **Grey Matter** from the animated television series **Ben 10**.

In the Ben 10 universe, Grey Matter is known for extraordinary intelligence, problem-solving ability, and analytical thinking. Inspired by this concept, the GreyMatter programming language represents logical thinking, experimentation, and innovation in programming.

Many of the built-in function names in GreyMatter are inspired by **alien characters and abilities from the Ben 10 cartoon universe**. These names symbolically represent different capabilities or behaviors of the language.

---

# Project Goals

The key objectives of the GreyMatter project include:

* Teaching the fundamentals of interpreter development
* Demonstrating how programming languages are implemented
* Providing an experimental platform for language design
* Encouraging students to explore compiler and interpreter concepts
* Creating a fun and creative programming environment

---

# Technology Stack

GreyMatter is built using the following technologies:

* Python Programming Language
* Lexer and Parser implemented with **SLY**
* Abstract Syntax Tree (AST) execution model
* Standard Python runtime libraries

---

# Core Language Features

GreyMatter provides the following programming capabilities:

* Variable declaration and assignment
* Arithmetic expressions
* Conditional statements
* Logical operations
* Loop constructs
* Function definitions
* Input and output handling
* String utilities
* Memory storage system
* Time utilities
* Experimental AI and Web query features

---

# Basic Syntax Example

```
x = 10
y = 20

z = x + y

PRINT(z)
```

---

# Variables

Variables are dynamically created during assignment.

Example:

```
x = 5
name = "GreyMatter"
```

There is no need for explicit type declaration.

---

# Arithmetic Operators

GreyMatter supports common arithmetic operators.

| Operator | Description    |
| -------- | -------------- |
| +        | Addition       |
| -        | Subtraction    |
| *        | Multiplication |
| /        | Division       |
| %        | Modulus        |

Example:

```
x = 10
y = 3

PRINT(x + y)
PRINT(x * y)
```

---

# Increment and Decrement

```
x++
x--
```

---

# Compound Assignment

```
x += 5
x -= 3
x *= 2
x /= 4
```

---

# Input and Output

### PRINT

Displays output to the console.

```
PRINT("Hello World")
```

---

### INPUT

Reads user input.

```
name = INPUT("Enter name: ")
```

---

### INT

Converts input to integer.

```
age = INT(INPUT("Enter age: "))
```

---

### STR

Converts input to string.

```
text = STR(INPUT("Enter message: "))
```

---

# Conditional Statements

Example:

```
IF (x > 10) {

   PRINT("Greater")

}
ELSE {

   PRINT("Smaller")

}
```

---

# Logical Operators

| Operator | Meaning     |
| -------- | ----------- |
| AND      | Logical AND |
| OR       | Logical OR  |

---

# Loops

### While Loop

```
x = 1

WHILE(x <= 5){

  PRINT(x)
  x++

}
```

---

### For Loop

```
FOR(i = 0 ; i <= 10 ; i++){

   PRINT(i)

}
```

Short loop:

```
FOR(5){

 PRINT("Hello")

}
```

---

# Functions

Functions allow reusable code blocks.

```
FUNCTION add(x , y){

   result = x + y
   FEEDBACK(result)

}
```

Calling the function:

```
sum = add(5 , 6)
PRINT(sum)
```

---

# Return Statement

GreyMatter uses the keyword **FEEDBACK** instead of return.

```
FUNCTION square(x){

   FEEDBACK(x * x)

}
```

---

# Built-in Functions Overview

GreyMatter includes multiple built-in functions and utilities. Many of them are named after alien abilities from the Ben 10 universe.

---

# Complete Function List

| Function           | Description                                |
| ------------------ | ------------------------------------------ |
| PRINT()            | Displays output to the console             |
| INPUT()            | Accepts input from the user                |
| INT()              | Converts input or value to integer         |
| STR()              | Converts value to string                   |
| LEN()              | Returns length of a string                 |
| ECHO               | Prints a blank line                        |
| ECHOECHO           | Prints multiple blank lines                |
| FASTTRACK()        | Returns character at specific index        |
| WAYBIG()           | Converts string to uppercase               |
| NANOMECH()         | Converts string to lowercase               |
| ISWAYBIG()         | Checks if text is uppercase                |
| ISNANOMECH()       | Checks if text is lowercase                |
| PARADOX.SLEEP()    | Pauses program execution                   |
| PARADOX.UNITIME()  | Returns system time                        |
| PARADOX.UNIDATE()  | Returns system date                        |
| BRAINSTORM.READ()  | Stores data in internal memory             |
| BRAINSTORM.WRITE() | Writes stored data                         |
| BRAINSTORM.GET()   | Retrieves stored data                      |
| JETRAY()           | Executes fast interpreter/system operation |
| @WEB_SEARCH        | Performs web search query                  |
| @AI                | Sends query to AI service                  |
| BREAK              | Terminates loop execution                  |
| FUNCTION           | Declares a function                        |
| FEEDBACK           | Returns value from function                |

---

# Example Program

```
FUNCTION multiply(x , y){

   FEEDBACK(x * y)

}

x = INT(INPUT("Enter first number: "))
y = INT(INPUT("Enter second number: "))

result = multiply(x , y)

PRINT("Result:", result)
```

---

# Interpreter Architecture

GreyMatter follows a typical interpreter architecture:

1. Lexical Analysis (Tokenizer)
2. Syntax Parsing
3. Abstract Syntax Tree Construction
4. Runtime Evaluation

This architecture allows programs written in GreyMatter to be parsed and executed dynamically.

---

# Educational Value

This project helps developers learn about:

* Programming language design
* Interpreter development
* Parsing algorithms
* Runtime execution models
* Custom language experimentation

---

# Future Improvements

Potential improvements include:

* File input/output support
* Standard library modules
* Error handling system
* Debugging tools
* Bytecode compilation
* Package manager
* IDE integration

---

# Author

Abinesh N

GitHub
[https://github.com/Abineshabee](https://github.com/Abineshabee)

---

