# GreyMatter Programming Language

GreyMatter is a **toy programming language interpreter written in Python** designed to help beginners learn programming concepts quickly and easily. The language focuses on simple syntax, readable structure, and interactive execution, making it ideal for understanding how programming languages work internally.

GreyMatter demonstrates the basic principles of **interpreter design, scripting languages, and programming fundamentals** while remaining lightweight and beginner-friendly.

---

# Motivation

Many new programmers find it difficult to start learning programming due to complex syntax and unfamiliar programming concepts. GreyMatter was created to:

* Simplify programming syntax
* Demonstrate interpreter-based language execution
* Help beginners understand how programming languages work internally
* Provide an experimental platform for learning language design

---

# Features

* Simple and readable syntax
* Python-based interpreter
* Interactive CLI execution
* Variable assignments
* Functions and recursion support
* Conditional statements
* Loops (`WHILE`, `FOR`)
* User input and output
* Built-in utilities
* Dictionary-style data storage with `BRAINSTORM`
* Educational interpreter structure

---

# Tech Stack

Language Used

* Python

Concepts Implemented

* Interpreter design
* Runtime execution
* Custom language syntax
* Control flow
* Function handling
* Basic data operations

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Abineshabee/GreyMatter.git
```

Navigate into the project folder:

```bash
cd GreyMatter
```

Make sure Python is installed:

```bash
python --version
```

---

# Running GreyMatter Programs

Run a GreyMatter script file:

```bash
python app.py calculator.txt
```

Run the **interactive CLI interpreter**:

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

# Language Syntax Examples

## Example 1 – Basic Variables and Output

```
x = 5
y = 6
PRINT( x + y )
```

Output

```
11
```

---

# Example 2 – Using BRAINSTORM Storage

```
x , y , z = 1 , 2 , 3

BRAINSTORM.READ( x )
BRAINSTORM.READ( y )
BRAINSTORM.READ( z )

x , y , z = 4 , 5 , 6

PRINT("x : ", x )
PRINT("y : ", y )
PRINT("z : ", z )

ECHO

BRAINSTORM.WRITE( x )
BRAINSTORM.WRITE( y )
BRAINSTORM.WRITE( z )

ECHO

BRAINSTORM.GET()
```

This works similar to a **dictionary-like storage system**.

---

# Example 3 – Functions and Calculator

```
FUNCTION add ( x , y ) {
    c = x + y
    FEEDBACK( c )
}

FUNCTION subtract ( x , y ) {
    FEEDBACK( x - y )
}

FUNCTION multiply ( x , y ) {
    FEEDBACK( x * y )
}

FUNCTION divide( x , y ) {
    IF ( y != 0 ) {
       FEEDBACK( x / y )
    }
    ELSE {
       FEEDBACK ( "Error! Division by zero." )
    }
}
```

---

# Example 4 – Fibonacci Series

```
FUNCTION fibonacci( n ) {

    a = 0
    b = 1

    PRINT("Fibonacci Sequence : ")

    FOR( i = 0 ; i <= n ; i++ ){

         PRINT( a )

         temp = a
         a = b
         b = temp + b

    }

}

n = 10
fibonacci(n)
```

---

# Example 5 – Simple Addition Loop

```
FUNCTION add( a , b ){

    c = a + b
    FEEDBACK( c )

}

WHILE( 1 ) {

     x = INT( INPUT("Enter The Number1 :"))
     y = INT( INPUT("Enter The Number2 :"))

     sum = add( x , y )

     PRINT("sum of ", x ," and ", y ," : ", sum )

}
```

---

# Example 6 – Prime Number Checker

```
FUNCTION isprime( n ){

      x = n
      n -= 1
      flag = 1

      FOR( 2 , n ){
          IF( x % fori == 0 ){
             flag = 0
          }
      }

      FEEDBACK( flag )
}
```

---

# Example 7 – Palindrome Checker

```
str = INPUT("Enter The String : ")
len = LEN( str )
result = ""

FOR( i = len - 1 ; i >= 0 ; i-- ){

    temp = str.FASTTRACK( i )
    result += temp

}

PRINT( str )
PRINT( result )

IF( str == result ) {

  PRINT( str ," is a palindrome ")

} ELSE {

  PRINT( str ," is not a palindrome ")

}

PRINT("END")
```

---

# Learning Outcomes

This project helps understand:

* How interpreters work
* Programming language syntax design
* Execution engines
* Control flow implementation
* Function parsing and execution
* CLI interpreter design

---

# Future Improvements

Possible future improvements for GreyMatter:

* Error handling improvements
* Module system
* File operations
* Standard library
* Package manager
* Syntax highlighting
* Bytecode execution
* Performance optimization

---

# Author

Abinesh N

GitHub
[https://github.com/Abineshabee](https://github.com/Abineshabee)

---

# License

Created For Educational Purposes.

---

If you want, I can also show you **4 improvements that can make this repo look like a real programming language project and attract recruiters**.
