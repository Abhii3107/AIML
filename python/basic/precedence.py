
# Python: Operator Precedence

## Meaning
# Operator precedence decides which operator is evaluated first in an expression.

# ## Order of Precedence (High to Low)

# | Priority | Operator                  | Meaning                                      |
# |----------|---------------------------|----------------------------------------------|
# | 1        | `()`                      | Parentheses                                  |
# | 2        | `**`                      | Exponentiation                               |
# | 3        | `*`, `/`, `//`, `%`       | Multiplication, Division, Floor Division, Modulus |
# | 4        | `+`, `-`                  | Addition, Subtraction                        |
# | 5        | `==`, `!=`, `>`, `<`, `>=`, `<=` | Comparison                           |
# | 6        | `not`                     | Logical NOT                                  |
# | 7        | `and`                     | Logical AND                                  |
# | 8        | `or`                      | Logical OR                                   |

## Example Code

# ```python
# Operator Precedence Examples

# 1. Parentheses
print((2 + 3) * 4)       # 20

# 2. Exponentiation
print(2 ** 3)             # 8

# 3. Multiplication, Division, Floor Division, Modulus
print(5 * 5)              # 25
print(10 / 2)             # 5.0
print(10 // 3)            # 3
print(10 % 3)             # 1

# 4. Addition and Subtraction
print(10 + 5 - 2)         # 13

# 5. Comparison Operators
print(5 == 5)             # True
print(5 != 3)             # True
print(5 > 3)              # True
print(5 >= 5)             # True
print(3 < 5)              # True
print(5 <= 5)             # True

# 6. Logical NOT
print(not True)           # False

# 7. Logical AND
print(True and False)     # False

# 8. Logical OR
print(True or False)      # True

# Combined Examples
print(5 + 2 * 3)          # 11
print((5 + 2) * 3)        # 21
print(2 ** 3 ** 2)        # 512
# ```

## Remember

# `()` → `**` → `*`, `/`, `//`, `%` → `+`, `-` → Comparison → `not` → `and` → `or`

# **Note:** Parentheses can change the normal order of evaluation. Most arithmetic operators at the same precedence level evaluate from left to right, while exponentiation (`**`) evaluates from right to left.
