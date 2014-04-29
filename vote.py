age = input("Enter Your Age: ")
citizen = raw_input("Are you a citizen [Y/N] ")

#if the user is 18 or older then they can vote.
if age >= 18 and citizen == "Y":
	print "You are elible to vote"
	print "Congratulations"
else:
	print "Sorry you are not eligible to vote"
print "EOE"

