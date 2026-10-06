from pathlib import Path
import os

print("press 1 creating a file")
print("press 2 read a file")
print("press 1 updating a file")
print("press 1 deleting a file")

a = int(input("tell your respose -> "))


def createfile():
    try:
        name = input("Please tell your file name :- ")
        path = Path(name)
        if not path.exists():
           with open(path,"w") as fs:
            data = input("what do you want to write :- ")
            fs.write(data)
        print("file created successfully")
    except Exception as err:
        print(f"error occurred {err}")

def readfile():
    name = input("Please tell your file name :- ")
    path = Path(name)
    if path.exists():
        with open(path,"r") as fs:
            content = fs.read()
            print(f"your file content is \n {content}")

def updatefile():
    pass
def deletingfile():
    pass

if a == 1:
    createfile()
if a == 2:
    readfile()
if a == 3:
    updatefile()
if a == 4:
    deletingfile()
