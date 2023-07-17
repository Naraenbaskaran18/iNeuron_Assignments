#!/usr/bin/env python
# coding: utf-8
1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.

* - mathematical 
'hello' - value
-87.8 - value
- - mathematical
/ - mathematical
+ - mathematical
6 - value2. What is the difference between string and variable?

String is nothing but an datatype which stores an sequence of characters like letters, numbers, symbols & whitespace. It is denoted as str.

Varaible is nothing but an memory container to store an data and manipulate the data. 3. Describe three different data types.

List - It is mutable and ordered. It is denoted by square brackets.
tuple - It is immuntable and ordered. It is denoted by brackets.
dict - It is unordered and stores the value in key-value pairs.4. What is an expression made up of? What do all expressions do?

An expression is made up of one or more operands and operators.

Operands: These are the values or entities that the expression operates on. They can be variables, constants, or function calls that return values. For example, in the expression 2 + 3, the operands are the numbers 2 and 3.

Operators: Operators define the operations to be performed on the operands. They can perform arithmetic operations, logical comparisons, assignment, and more. For example, the + operator in 2 + 3 performs addition on the operands.5. This assignment statements, like spam = 10. What is the difference between an
expression and a statement?

In this, spam = 10 is an assignment statement. It assigns 10 to the variable name called spam.

Experession is made up of one or more operands and operators6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1

It still contains 22 only.7. What should the values of the following two terms be?

'spam' + 'spamspam'  - spamspamspam
'spam' * 3  - spamspamspam8. Why is eggs a valid variable name while 100 is invalid?

The 'eggs' is a valid variable name, while '100' is invalid due to its starting character being a number.9. What three functions can be used to get the integer, floating-point number, or string
version of a value?

int()
float()
str()10. Why does this expression cause an error? How can you fix it?
'I have eaten'  + 99 +  'burritos.'

In this str is trying to add with int directly. So, it cause an error.
To fix it we can convert int to str by the following way.
'I have eaten'  + str(99) +  'burritos.'