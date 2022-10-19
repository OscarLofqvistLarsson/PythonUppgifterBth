def use_function(function, x):
        return function(x) * function(x)

print(use_function(lambda x:x + 1, 4))