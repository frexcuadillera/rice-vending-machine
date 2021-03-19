

try:
    f = open("price.txt", "r")
except:
    f = open("price.txt", "w")
    l = f.write("one\ntwo\nthree")
    f = open("price.txt", "r")

l = f.readlines()
for x in l:
    print(x)

f.close()
