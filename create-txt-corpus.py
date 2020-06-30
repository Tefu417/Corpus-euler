import glob

with open('corpus-euler.txt', 'a') as newfile :

    for f in glob.glob('txt-euler/*.txt') :
        with open(f, 'r') as oldfile :
            for line in oldfile :
                line = line.replace('\t', '')
                n = line.find(' # ')
                c = line[: n]
                ja = line[n + 3 :]
                l = str(c + '\t' + ja)
                newfile.write(l)
