# Chapter 12: Algebraic Expressions

## Introduction to Algebraic Expressions

In mathematics, we often use combinations of constants and variables. An **algebraic expression** is a mathematical phrase that is formed by combining variables and constants using mathematical operations like addition, subtraction, multiplication, and division.

*   **Variable:** A symbol (usually a letter like `x`, `y`, `a`) that can take on various numerical values. Its value is not fixed.
*   **Constant:** A quantity that has a fixed numerical value. For example, 5, -10, 2/3.

**Example:** The expression `4x + 7` is formed from the variable `x` and the constants `4` and `7`.

---

## Terms, Factors, and Coefficients

### 1. Terms of an Expression

Terms are the parts of an expression that are added or subtracted. They are the individual building blocks of an expression.

**Example:** In the expression `5xy - 3z + 8`, the terms are:
*   `5xy`
*   `-3z`
*   `8`

### 2. Factors of a Term

A term is a product of its factors. Factors can be numerical or algebraic (variables).

**Example:** Consider the term `5xy`.
*   The factors are `5`, `x`, and `y`.

We can represent this using a tree diagram:

```mermaid
graph TD
    subgraph Expression: 5xy - 3z
        A(5xy) --> B(5)
        A --> C(x)
        A --> D(y)
        E(-3z) --> F(-3)
        E --> G(z)
    end
```

### 3. Coefficients

The **numerical factor** of a term is called its numerical coefficient or simply the **coefficient**.

| Term | Coefficient | Variable Part |
| :--- | :--- | :--- |
| `7xy` | 7 | `xy` |
| `-5x²`| -5 | `x²` |
| `y` | 1 | `y` |
| `-ab` | -1 | `ab` |

---

## Like and Unlike Terms

This is a very important concept for performing operations on algebraic expressions.

*   **Like Terms:** Terms that have the **same algebraic factors** (i.e., the same variables raised to the same power). The numerical coefficients can be different.
    *   **Examples:**
        *   `2x` and `-9x` (Both have the variable `x`)
        *   `5a²b` and `a²b` (Both have variables `a²b`)
        *   `-3pq` and `10pq` (Both have variables `pq`)

*   **Unlike Terms:** Terms that have **different algebraic factors**.
    *   **Examples:**
        *   `7x` and `7y` (Different variables: `x` and `y`)
        *   `4m²` and `12m` (Different powers of the variable `m`)
        *   `6xy` and `8xyz` (Different variable combinations)

> **Key Idea:** We can only perform addition and subtraction on **like terms**.

---

## Types of Algebraic Expressions

Expressions are named based on the number of terms they contain.

| Type | Number of Terms | Example | Terms in the Example |
| :--- | :--- | :--- | :--- |
| **Monomial** | One term | `7xy` | `7xy` |
| **Binomial** | Two unlike terms | `a + 5` | `a`, `5` |
| **Trinomial** | Three unlike terms | `x + y - 3` | `x`, `y`, `-3` |
| **Polynomial**| One or more terms | `4x² + 2xy - z + 9` | `4x²`, `2xy`, `-z`, `9` |

**Note:** All monomials, binomials, and trinomials are also polynomials.

---

## Addition and Subtraction of Algebraic Expressions

The fundamental rule for adding or subtracting algebraic expressions is to **combine like terms**.

### Addition

To add expressions, we collect the like terms and add their numerical coefficients.

**Example:** Add `7x + 2y - 3z` and `3x - 5y + 4z`.

**Method 1: Horizontal Method**
1.  Write the expressions in a single line.
    `(7x + 2y - 3z) + (3x - 5y + 4z)`
2.  Group the like terms together.
    `(7x + 3x) + (2y - 5y) + (-3z + 4z)`
3.  Add the coefficients of the like terms.
    `(7+3)x + (2-5)y + (-3+4)z`
4.  Simplify to get the final answer.
    `10x - 3y + z`

**Method 2: Column Method**
1.  Write the expressions one below the other, ensuring like terms are in the same column.
    ```
      7x + 2y - 3z
    + 3x - 5y + 4z
    -----------------
    ```
2.  Add the coefficients in each column.
    ```
      7x + 2y - 3z
    + 3x - 5y + 4z
    -----------------
     10x - 3y +  z
    ```

### Subtraction

To subtract an expression, we **add its additive inverse**. This means we change the sign of **every term** in the expression being subtracted and then add the two expressions.

**Example:** Subtract `4a - 2b + c` from `9a + 3b - 5c`.

**Method 1: Horizontal Method**
1.  Write the expressions.
    `(9a + 3b - 5c) - (4a - 2b + c)`
2.  Change the sign of each term in the second bracket. The `-` outside becomes `+`.
    `9a + 3b - 5c + (-4a + 2b - c)`
3.  Group the like terms.
    `(9a - 4a) + (3b + 2b) + (-5c - c)`
4.  Combine the like terms.
    `5a + 5b - 6c`

**Method 2: Column Method**
1.  Write the expressions one below the other with like terms in the same column.
    ```
      9a + 3b - 5c
    - (4a - 2b + c)
    -----------------
    ```
2.  Change the sign of every term in the bottom row.
    ```
      9a + 3b - 5c
      -4a + 2b -  c   <-- Signs changed
    -----------------
    ```
3.  Add the columns as usual.
    ```
      9a + 3b - 5c
    - 4a + 2b -  c
    -----------------
      5a + 5b - 6c
    ```

---

## Finding the Value of an Expression

To find the value of an algebraic expression, we substitute the given numerical value for each variable and then simplify the resulting arithmetic expression.

**Example 1:** Find the value of `3x - 5` if `x = 4`.
1.  Substitute `x` with `4`: `3(4) - 5`
2.  Calculate: `12 - 5`
3.  Result: `7`

**Example 2:** Find the value of `a² + 2ab + b²` if `a = 2` and `b = 3`.
1.  Substitute `a` with `2` and `b` with `3`: `(2)² + 2(2)(3) + (3)²`
2.  Calculate: `4 + 12 + 9`
3.  Result: `25`

---

## Summary

*   An **algebraic expression** is a combination of constants and variables connected by mathematical operations.
*   **Terms** are the parts of an expression that are added.
*   A **coefficient** is the numerical factor of a term.
*   **Like terms** have the same variables raised to the same powers, while **unlike terms** do not.
*   Expressions are classified as **monomials** (1 term), **binomials** (2 terms), and **trinomials** (3 terms).
*   To add or subtract expressions, you must combine **like terms** only.
*   When subtracting, change the sign of every term in the expression being subtracted and then add.
*   To find the value of an expression, **substitute** the given values for the variables and simplify.