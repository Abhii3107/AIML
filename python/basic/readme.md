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
