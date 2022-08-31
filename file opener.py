
n = raw_input("Enter file name: ")

f = open(n,"r+")
w = raw_input("Enter your text here:  ")
f.write(w)
f.close


