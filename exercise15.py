from sys import argv
script, filename =argv
txt = open (filename)

print "Here is your file %r " % filename
print txt.read()

print "Type your file name again:"
file_name_again = raw_input (">")

txt_again = (file_name_again)
txt_again = open (file_name_again)
print txt_again.read()
