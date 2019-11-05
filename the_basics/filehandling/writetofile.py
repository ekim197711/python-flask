
myfile = open('outputfile1.txt','w')

for i in range(100):
    contentline = f'This is the {i} time that we write to the file!\n'
    print(contentline)
    myfile.write(contentline)

myfile.close()


myfile=open('outputfile3.txt','a')
myfile.write("Lets see if we can write to this file...")
myfile.close()

myfile=open('outputfile3.txt','r')
print(f'Heres the content: {myfile.read()}')
