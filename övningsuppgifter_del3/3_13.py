def mRNA_tanscript(DNA):
    result =""
    rule = {"A":"U" ,"T":"A","C":"G","G":"C" }
    for key in DNA:
        result += rule[key]
    return result


print(mRNA_tanscript("ATCGATTG"))