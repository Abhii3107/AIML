# Character Set

Python Variable Naming Rules

Allowed characters: A-Z, a-z, 0-9, \_

Must start with a letter or underscore (\_).

Cannot start with a number.

Cannot contain spaces or special characters like @, #, $, -.

Variable names are case-sensitive (name ≠ Name). - these will be two different variables or identifiers

Cannot use Python keywords like if, for, class, True.

Examples

# Valid

name = "Abhay"
\_age = 22
user1 = "Alex"
total_marks = 90

# Invalid

1name = "Abhay" # Starts with a number
user-name = "Alex" # Hyphen not allowed
user name = "Alex" # Space not allowed
class = "Python" # Reserved keyword

Convention: Use snake_case for variable names, e.g. total_marks, user_name.



# Python Fundamentals (Part 1)

**Concepts:** Output, Input, Variables, Data Types, Type Casting & Operators

---

## 1. Output in Python

The `print()` function is used to display text, numbers, and calculation results on the screen.

### Example: Printing Text

```python
print("Hello World")
print("Welcome to Python")
```

### Example: Printing Numbers and Calculations

```python
print(3.14)
print(2 + 3)
print(5 * 5)
```

**Output:**
```text
3.14
5
25
```

## 2. Python Character Set

A character set is a collection of characters that Python can recognize and use.

- **Letters:** `A-Z`, `a-z`
- **Digits:** `0-9`
- **Special symbols:** `+`, `-`, `*`, `/`, `=`
- **Whitespace:** spaces and tabs
- **Escape characters:** `\n` (new line), `\t` (tab)

### Example

```python
print("Hello\nWorld")
print("Hello\tWorld")
```

## 3. Variables

A variable is a named container used to store data in a program.

### Example

```python
name = "Abhay"
age = 24
PI = 3.14

print(name)
print(age)
print(PI)
```

### Variable Naming Rules

1. A variable name must start with a letter or underscore (`_`).
2. It can contain letters, digits, and underscores.
3. It cannot start with a digit.
4. Python keywords cannot be used as variable names.
5. Variable names are case-sensitive.

### Example

```python
name = "Abhay"
_age = 24
student1 = "Rahul"

# Invalid examples:
# 2name = "Bob"
# class = 10
```

### Important Notes

- Python is dynamically typed.
- `age` and `Age` are different variables.
- Indentation is important in Python; use four spaces per indentation level.
- Keywords include `if`, `for`, `while`, `class`, and `else`.

## 4. Data Types

A data type defines the kind of value a variable can store.

| Data Type | Description | Example |
|---|---|---|
| `int` | Integer | `10` |
| `float` | Decimal number | `3.14` |
| `str` | String or text | `"Hello"` |
| `bool` | Boolean value | `True`, `False` |
| `complex` | Complex number | `2 + 3j` |
| `NoneType` | No value | `None` |

Other Python data types include `list`, `tuple`, `set`, and `dict`.

### Example: Checking Data Types

```python
a = 10
b = 3.14
name = "Abhay"
is_student = True

print(type(a))
print(type(b))
print(type(name))
print(type(is_student))
```

## 5. Type Conversion and Type Casting

**Type conversion** means changing one data type into another.

- **Implicit conversion:** Python converts data types automatically.
- **Explicit conversion (type casting):** The programmer converts data types manually.

### Example: Implicit Conversion

```python
a = 10
b = 2.5

result = a + b

print(result)        # 12.5
print(type(result))  # <class 'float'>
```

### Example: Explicit Conversion

```python
a = "10"

b = int(a)
c = float(a)

print(b)  # 10
print(c)  # 10.0
```

### Common Type Casting Functions

| Function | Description | Example |
|---|---|---|
| `int()` | Converts to integer | `int("10")` |
| `float()` | Converts to float | `float("3.5")` |
| `str()` | Converts to string | `str(100)` |
| `bool()` | Converts to Boolean | `bool(1)` |
| `list()` | Converts to list | `list("abc")` |
| `tuple()` | Converts to tuple | `tuple([1, 2])` |
| `set()` | Converts to set | `set([1, 1, 2])` |

### Important Examples

```python
print(int(5.8))       # 5
print(float(10))      # 10.0
print(str(100))       # "100"
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("Hello"))  # True
```

**Note:** `int(5.8)` removes the decimal part; it does not round the number. Invalid conversions, such as `int("hello")`, raise a `ValueError`.

## 6. Operators

An operator is a symbol that performs an operation on one or more values. The values are called operands.

### Example

```python
a = 5
b = 3

print(a + b)  # 8
```

## 7. Arithmetic Operators

Arithmetic operators perform mathematical calculations.

| Operator | Description | Example |
|---|---|---|
| `+` | Addition | `5 + 3 = 8` |
| `-` | Subtraction | `5 - 3 = 2` |
| `*` | Multiplication | `5 * 3 = 15` |
| `/` | Division | `5 / 2 = 2.5` |
| `//` | Floor division | `5 // 2 = 2` |
| `%` | Modulus (remainder) | `5 % 2 = 1` |
| `**` | Exponentiation | `2 ** 3 = 8` |

### Example

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

## 8. Relational (Comparison) Operators

Comparison operators compare two values and return `True` or `False`.

| Operator | Description |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

### Example

```python
a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True
```

## 9. Assignment Operators

Assignment operators assign values to variables or update their existing values.

| Operator | Equivalent Expression |
|---|---|
| `=` | `x = 10` |
| `+=` | `x = x + 5` |
| `-=` | `x = x - 3` |
| `*=` | `x = x * 2` |
| `/=` | `x = x / 4` |
| `//=` | `x = x // 2` |
| `%=` | `x = x % 3` |
| `**=` | `x = x ** 2` |

### Example

```python
x = 10

x += 5
print(x)  # 15

x -= 3
print(x)  # 12

x *= 2
print(x)  # 24

x /= 4
print(x)  # 6.0
```

## 10. Logical Operators

Logical operators combine conditions or reverse a Boolean result.

| Operator | Description |
|---|---|
| `and` | Returns `True` when both conditions are true |
| `or` | Returns `True` when at least one condition is true |
| `not` | Reverses the Boolean result |

### Truth Table

| A | B | A and B | A or B |
|---|---|---|---|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

### Example

```python
x = 10
y = 20
z = 5

print(x > z and y > x)  # True
print(x > y or y > z)   # True
print(not (x > y))      # True
```

## 11. Operator Precedence

Operator precedence determines the order in which operators are evaluated in an expression.

### Order of Precedence (High to Low)

| Priority | Operators | Description |
|---|---|---|
| 1 | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `+x`, `-x`, `~x` | Unary operators |
| 4 | `*`, `/`, `//`, `%` | Multiplication, division, floor division, modulus |
| 5 | `+`, `-` | Addition, subtraction |
| 6 | `<<`, `>>` | Bitwise shifts |
| 7 | `&` | Bitwise AND |
| 8 | `^` | Bitwise XOR |
| 9 | `\|` | Bitwise OR |
| 10 | `<`, `<=`, `>`, `>=`, `==`, `!=` | Comparisons |
| 11 | `not` | Logical NOT |
| 12 | `and` | Logical AND |
| 13 | `or` | Logical OR |

### Example

```python
print(5 + 2 * 3)       # 11
print((5 + 2) * 3)     # 21
print(2 ** 3 ** 2)     # 512
print(10 > 5 and 5 > 2)  # True
```

**Remember:**
- Parentheses can change the order of evaluation.
- Exponentiation evaluates from right to left.
- Most arithmetic operators at the same precedence level evaluate from left to right.

## 12. Input in Python

The `input()` function accepts information from the user while a program is running.

By default, `input()` returns a string (`str`).

### Example: Taking String Input

```python
name = input("Enter your name: ")

print(name)
print(type(name))  # <class 'str'>
```

### Example: Taking Integer Input

Use `int()` to convert the input string into an integer.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)
```

## 13. Practice Problem: Calculate the Average

Write a program that takes two numbers from the user and calculates their average.

**Formula:**

Average = (a + b) / 2

### Example

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

average = (a + b) / 2

print("Average =", average)
```

**Sample Input:**
```text
Enter first number: 5
Enter second number: 10
```

**Output:**
```text
Average = 7.5
```

## Quick Revision

- `print()` displays output.
- `input()` accepts user input as a string.
- Variables store values.
- `type()` checks a value's data type.
- `int()`, `float()`, `str()`, and `bool()` convert data types.
- Arithmetic operators perform calculations.
- Comparison operators return `True` or `False`.
- Assignment operators assign or update values.
- Logical operators combine conditions.
- Operator precedence determines the order of evaluation.

---

**Keep Learning & Keep Exploring!**
