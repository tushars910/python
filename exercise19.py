def cheese_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!!!!!" % cheese_count
    print "you have %d boxes of crackers!!!" %boxes_of_crackers
    print "Man thats enough for the party"
    print "Get a blanket"


print "We can just give function numbers directly:"
cheese_crackers (10,20)

print "Use variables from our script:"
amount_of_cheese =int(raw_input())
amount_of_crackers = 40

cheese_crackers (amount_of_cheese, amount_of_crackers)

print "Even we can do this inside too:"
cheese_crackers (20+20 , 50+50)

print "And we can combine the two variables and math:"
cheese_crackers (amount_of_cheese +1000, amount_of_crackers +1000)
