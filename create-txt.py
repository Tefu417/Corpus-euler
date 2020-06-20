from pathlib import Path

for f in Path(".").rglob("txt-euler/*.py") :
    f.rename(f.stem+".txt")

print(f)
