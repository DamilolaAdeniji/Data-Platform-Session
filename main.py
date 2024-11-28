print ("Welcome to my Container")

# create a list of all integers from 1 - 1000
master_list = list(range(1001))

# get a resulting list that gets the remainder of each num when divided by 2
mod_list = [ n % 2 for n in master_list]

# printing  all unique values in that list
print (f"Here are the unique values: {set(mod_list)}")