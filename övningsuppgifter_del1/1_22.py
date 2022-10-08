namn_1 = str(input("Vad är ditt namn?"))

ålder_1 = int(input("när är du född?"))

namn_2 = str(input("Vad är ditt namn?"))

ålder_2 = int(input("när är du född?"))

if 2021 >= ålder_1 >=1900 and 2021 >= ålder_2 >= 1900:
    if ålder_1 < ålder_2:
        print(namn_1, "är äldst", namn_2, "är yngre")

    if ålder_2 < ålder_1:
        print(namn_2, "är äldst", namn_1, "är yngre")

    if ålder_1 == ålder_2:
        print(namn_1, "och", namn_2, "är lika gamla")

else:
    print("mellan åren 1900-2021 endast")