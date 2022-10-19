def add_one(x):
    return x + 1

def use_function(function, x):
        return function(x) * function(x)

print(use_function(add_one, 0))