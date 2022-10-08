def write2file(string,num):
    out = open(string, "w")
    for i in range(1,num+1):
        for j in range(0,101):
            out.write(f"{i} * {j} = {i*j}\n")
        out.write("\n")
    out.close()

write2file("övningsuppgifter_del2\output.txt",101)
