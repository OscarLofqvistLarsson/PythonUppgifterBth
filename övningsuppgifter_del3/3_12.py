def show_word_list(w_list):
    for key in w_list:
        print(f"{key} - {w_list[key]}")

numbers = {"one": 1, "two": 2, "seven": 6, "eight": 9}
show_word_list(numbers)