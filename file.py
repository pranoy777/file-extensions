filename = input("File Name : ")
a = filename.split(".")

c = {"doc": "wordfile",
              "py" : "python",
              "html": "hypertext markup language",
              "jpg": "Image file",
              "txt": "Txt file",
              "png": "Image file",
              "xls": "Excel sheet",}

if a[-1] in c:
        print(c[a[-1]])
else:
        print("un-known extension") 

  
