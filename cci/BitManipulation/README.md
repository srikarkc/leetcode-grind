# Chapter 5 - Bit Manipulation

## Basics

Computers typically store integers in two's complement representation.

A positive number is represented as itself while a negative number is represented as 2's complement of its absolute value 
(with a 1 in its sign bit to indicate that its a negative value)

![2's complement](https://i.ytimg.com/vi/RbJV-g9Lob8/hqdefault.jpg)

2's complement of an n-bit number is the complement of a number with respect to 2^n.

binary representation of -k as a n-bit number = concat(1, 2^(N-1) - K)

(or) we invert all the bits in the positive representation and add 1.

### Shift Operators

There are 2 types of right shift operators:

1. Arithmetic right shift (approximately divides by 2) (>>)
2. Logical right shift operator (>>>)

A sequence of all 1's in a signed integer represents -1.

Only arithmetic shift operator natively available in Python.
