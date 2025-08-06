# Technical Design Document: Fibonacci Sequence Generator

## Summary

This document details the technical design for a Python script that calculates and prints Fibonacci numbers using a recursive approach. The system focuses on calculating the Fibonacci sequence up to a specified number of terms.

## Components

*   Fibonacci Function
*   Sequence Generator
*   Output Module

## Sequence of Steps

1.  Define the Fibonacci calculation function (fibonacci_recursive(n)
2.  Set the desired number of terms (n_terms)
3.  Iterate from 1.  to n_terms
4.     Calculate the Fibonacci number for each term using the recursive function
5.  Print the calculated Fibonacci number to the console

## Constraints

*   The recursive approach can become computationally expensive for large values of n.
*   The script is designed for generating the Fibonacci sequence up to a fixed number of terms.

## Assumptions

*   Input 'n' will always be a non-negative integer.
*   The script runs in an environment with Python interpreter installed.
*   Output is directed to the console.