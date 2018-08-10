#What is Function?

#-> They name pieces o hhe code the eay variable name strings and numbers
#-> They take arguments the way your scripts take argv
#-> 1 and 2 help you to make your own "mini-scripts" or tiny commands

#to take inputs like your  :"argv"

def print_two(*args):
    arg1, arg2= args
    print "arg1: %r, arg2: %r" %(arg1, arg2)

#okay args are actually point less

def print_two_again (arg1, arg2):
    print "arg1: %r, arg2: %r" %(arg1,arg2)

def print_one (arg1):
    print "Arg1: %r" % arg1

def print_none():
    print "I got nothing"
Tushar= "hahahahahahahahahahahahahahahahahahah"
print_two(Tushar,"Ruchira")
print_two_again("Ruchira", "Tushar")
print_one("Ruchira only")
print_none()

#defining  function is pretty easy consider it as defining a definition that you would like to use in the future
#everytime functon has to be closed with a :
