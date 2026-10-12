# range (n) -> give sequential order upto [0,1,...n-1]

# range(start , stop ,step )

# range(start, stop, step)
# start: Optional, default = 0
# stop: Required, excluded
# step: Optional, default = +1

for i in range(1, 10, +2):
    print(i)
    
    # op -> 1,3,5,7,9

# ---------------------

# for i in range (5):
#     print(i)
    
# '''
# Remember this rule
# - range(5) starts from 0 by default.

# - range(start, stop) lets you specify the starting number and the stopping limit.
# - The stop value is excluded.


# '''
# for i in range(1, 6):
#     print(i)
    
# # Output: 1 2 3 4 5