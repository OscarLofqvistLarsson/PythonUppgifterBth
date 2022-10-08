def introduce(name="unknown", age=None):
    print("My name is", name, end='')
    if age is None:
        print(". My age is a secret.")
    else:
        print(". I am", age, "years old.")


introduce("Linn", 19)
introduce("Carina")
introduce()
