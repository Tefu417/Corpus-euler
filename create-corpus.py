import re
import sys
# 入力するファイル名をコマンドライン引数から受け取る
# ターミナルで実行
# python3 create-corpus.py corpus-euler/euler02.txt
import pathlib
import os

f = sys.argv[1]
p_f = pathlib.Path(f)

with open(p_f, "r") as oldfile, \
        open("corpus-euler/c_euler" + str(f[15:17]) + ".txt", "w") as newfile :

    F = oldfile.read()
    F = F.replace(" # ", ",")
    F = F.replace("\t", "")

    newfile.write(F)
