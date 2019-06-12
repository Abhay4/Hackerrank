batfirst = input("Who bats first")

print "Round 1 : %s is batting"%batfirst

a = input("A throws?")
b = input("B throws?")

# validate a and b
valid_score = [0,1,2,3,4,6]
if a not in valid_score:
	print "A , dont be naughty. Throw a valid move"
if b not in valid_score:
	print "B , dont be naughty. Throw a valid move"

a_score = 0   # can be made into a function
b_score = 0
count = 0
while(a!=b):
	if batfirst == "A": # repetative 
		a_score += a
	else:
		b_score += b
	count += 1
	if count == 6:
		print "Its an over"
		break 
	a = input("A throws?")
	b = input("B throws?")
	if a not in valid_score:
		print "A , dont be naughty. Throw a valid move"
	if b not in valid_score:
		print "B , dont be naughty. Throw a valid move"


print "%s is out"%batfirst
if batfirst == "A": # repetative 
	print "Score is %s"%a_score
else:
	print "Score is %s"%b_score


batnext = "B" if batfirst == "A" else "A"
print "Round 2 : %s is batting"%batnext

a = input("A throws?")
b = input("B throws?")
count =0
while(a!=b):
	if batnext == "A": # repetative 
		a_score += a
	else:
		b_score += b
	count += 1
	if count == 6:
		print "Its an over"
		break 
	a = input("A throws?")
	b = input("B throws?")
	if a not in valid_score:
		print "A , dont be naughty. Throw a valid move"
	if b not in valid_score:
		print "B , dont be naughty. Throw a valid move"

print "%s is out"%batnext
if batnext == "A": # repetative 
	print "Score is %s"%a_score
else:
	print "Score is %s"%b_score


if a_score > b_score:
	print "Winner is A"
elif a_score < b_score:
	print "Winner is B"
else:
	print "Its a tie"

# Score printing is missing
# Only 6 balls per over 
# if he throws an invalid move - let him know that. 

