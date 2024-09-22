# Syntax Error

a = 10
b = 2 3                         # syntax error

print(a b)

#=============================================================

# Namr Error

a = 10
b = c + 1                       # Namr Error

#=============================================================

# Type Error

a = 10
b = 1 + 'hello'                 # Type Error

#=============================================================

# Index Error

a = [1, 2, 3]

print(a[12])                    # Index Error

#=============================================================

# Value Error

a = [1, 2, 3]
a.remove('hello')               # Value Error

print(a)

#=============================================================

# key Error

a = {
    'name': 'negar'
} 
print(a['age'])                 # key Error


#=============================================================
# ZeroDivision Error

a = 10
b = 0
print(a/b)                     # ZeroDivision Error

#=============================================================
# ModuleNotFoundError

import mymodule
