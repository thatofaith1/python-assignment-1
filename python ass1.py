name = input(" Enter your name")
age = int(input("Enter your age"))
location = input("Enter your location")

# first approach 
print ("Hello", name, "You are", age, "Year old and live in", location,)

#second approach %
print ("second approach")
print("Hello %s You are %d Years old and you live in %s"%(name, age, location))

#third approach format
print("theird approach")
print("Hello {} You are {} Years old and you live in {}".format(name, age, location))