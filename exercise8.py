formatter = "%r %r %r %r "
formatter1 = "%r %r %r %r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False) #This are working as boolean, if you put "True" > it will become string
print formatter % (formatter, formatter, formatter, formatter)
print formatter1 % (
	"I had this thing",
	"That you could type up right",
	"But it didn't sing",
	"So I said good' night",
    "asd",
    "as d",
    "asdf as d'f af's."
)

# if you observe the behaviour if sentence has s single quote in word it will be reflected in double quote
