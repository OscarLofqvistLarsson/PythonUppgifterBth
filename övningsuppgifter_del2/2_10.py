def find_and_replace(find_str, replace_str, infile, outfile):
    """
    Replaces all occurances of find_str in infile with replace_str
    and writes the result to outfile
    """
    in_file = open(infile, 'r')
    out_file = open(outfile, 'w')
    for line in in_file:
        if find_str in line:
            line = line.replace(find_str, replace_str)
        out_file.write(line)
    in_file.close()
    out_file.close()


if __name__ == "__main__":
    find_and_replace("Alice", "Dumbeldore", "Alice.txt", "MyStory.txt")