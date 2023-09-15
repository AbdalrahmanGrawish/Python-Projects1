# Exercise (taka the user fname , lname , age , schoolname).
# capitalize the fname and lanme and concatenate them.
# make the schoolname lowercase.

fname = input('Please Enter your first name:')
lname = input('Please Enter your last  name:')
age = input('Please Enter your age:')
schoolname = input('Please Enter your school name')
fname = fname.title()
lname = lname.title()
full_name = fname + " " + lname

schoolname = schoolname.lower()

print('your fuul name',full_name)
print('your age now is',age)
print('your school name',schoolname)
