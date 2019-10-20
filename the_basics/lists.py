
mymagicnumbers=[1,4,6,88,123,144,786]
mymagicnumbers=mymagicnumbers+[2,3,4,5,6]
mymagicnumbers[2] = 2000
for item in mymagicnumbers:
    print(item)
print("out of the for loop")

myint=100
while myint > -1000:
    myint=myint-5
    print(myint)
print("out of the while loop")

for myitem in range(10,21):
    print(myitem)

print("Out of range 10 to 20 for loop")

print("Number of elements {}".format(len(mymagicnumbers)))
