from sys import argv

script, filename = argv

print "We are going to erase a file first %r" % filename
print "If you dont want that plese enter Ctrl + C "
print " If you dont want that then hit return"

raw_input ("?")

print "Opening the file..."
target = open (filename, 'w')

print "truncating the file......goodbye"
target.truncate ()

print " Now I am going to ask you this three lines"

line1 = raw_input ("line1: ")
line2 = raw_input ("Line2: ")
line3 = raw_input ("Line3: ")

print "I am going to write these to the file "

target.write(line1 + "\n" + line2 + "\n" + line3)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#target.write("\n".join(line1, line2, line3)+ "\n")
print "Finally we close it"
#target.close()
