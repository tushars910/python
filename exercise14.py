from sys import argv
script, user_name = argv
pro = '--'

print "Hi %s , I'm the %s script" % (user_name, script)
print "I would like to ask you few questions"
print "do you like me %s?" % user_name
likes = raw_input(pro)

print "where do you live %s" % user_name
lives = raw_input (pro)

print "what kind of computer you have?"
computer = raw_input(pro)

print """
Alright you said %r about liking me. You live in %r. Not sure where that is. And you have a %r computer """ % (likes, lives , computer)
