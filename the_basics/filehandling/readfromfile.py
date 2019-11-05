myfile=open('importantstuff.txt')
thecontent = myfile.read()
print(f'Content of the file { thecontent }')
myfile.close()

myfile=open('doesnotexistyet.txt','r')
thecontent = myfile.read()
print(f'Content of the file { thecontent }')
myfile.close()


