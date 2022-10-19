def compose(f, g):
    return f (g)

def f(function):
    return function ** 2

def g(x):
    return x + 1

print(compose(f,g(12)))