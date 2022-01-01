file1 = open("output.html", "r")


mylist = []
for i in file1:
    if i == "--toberemove--\n":
        pass
    else:
        mylist.append(i)











strx = ""
for i in mylist:
    strx+=i


file1 = open("output.html", "w") 
file1.write(strx)
file1.close() 



x = input('enter ')