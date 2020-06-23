import glob

with open("corpus-euler.csv", "a") as newfile :

    for f in glob.glob("csv-euler/*.csv") :
        F = open(f, "r")
        F = F.read()
        F = F.replace("\n\n", "")

        print(F, file = newfile)