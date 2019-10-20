
myname="Mike Møller\" Nielsen's house"
myname2='Mike Møller Nielsen'
print(myname)
mychrs=myname[5:10]
print(mychrs)
mychrs=myname[5:]
print(mychrs)
mychrs=myname[::3]
print(mychrs)

mychrs=myname[-6:]
print(mychrs)

mymulti='''
jsækdfjælasdf
sdf
adsf
asdf
blalkalla
\'''
\n\n\n\n
End of string
'''
print(mymulti)

mymulti="""
*** my multi line string
new line...
end of string ***
"""
print(mymulti)



myname3='Mike Møller Nielsen'
myage=41
print("Name: {name}, Age: {age}".format(age=myage, name=myname3))
print("Name: %s, Age: %s" % (myname3, myage))