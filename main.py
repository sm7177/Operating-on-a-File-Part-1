#Activity-1 reading no. of characters----------------------------------------------------------------
# file=open("hi.txt","r")
# print(file.read(10))


#Activity-2 ------------------------------------------------------------------------------------------
# file=open("hi.txt","r")
# #print(file.readline())
# for line in file:
#     print(line)
# file.close()



#Activity-3 ------------------------------------------------------------------------------------------
# file1=open("hi.txt","r")
# file2=open("today.txt","w")

# for line in file1.readlines():
#     if not (line.startswith("Coding")):
#         print(line)
#         file2.write(line)
# file1.close()
# file2.close()



#Activity-4 ------------------------------------------------------------------------------------------
f1=open("hi.txt","r")
f2=open("today.txt","w")

counter=f1.readlines()
type(counter)

for i in range(1, len(counter)+1):
    if(i%2!=0):
        f2.write(counter[i-1])
    else:
        pass
f1.close()

f2=open("today.txt","r")
counter1=f2.read()

print(counter1)

