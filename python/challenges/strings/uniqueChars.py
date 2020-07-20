#implement an algorithm that checks if a string has all unique chars

def uniqueChars(string):
	#create a hashtable to store char values
	dict = {}
	#loop through the string
	for i in range(0, len(string)):
		#if the current char exists in the dict this string is not unique, end search and return
		if string[i] in dict:
			print(string, " contains duplicate chars")
			return
		#if the current char does not exist in the dict, add it in
		else:
			dict[string[i]] = 1

	print(string, " is unique")


uniqueChars("racecar")
uniqueChars("abcdefg")

#implement this method without using additional data structures 

#one way to approach this problem without the use of additional data strcutures would be to use
# a double for loop to traverse the string and compare it with every other element of the string, 
# breaking if there is a match. But this algorithm takes O(n^2) 

#an alternative approach would be to sort the string, then check for 'matching neighbors'

def unique_chars(string):

	#sorted() creates a list of sorted chars
	sorted_list = (sorted(string))

	#loop through the sorted_list and check to see if neighbors match
	for i in range(0, len(sorted_list)-1):
		if sorted_list[i] == sorted_list[i+1]:
			print(string, " contains duplicate chars")
			return
	print(string, " is unique")

unique_chars("abcde")
unique_chars("racecar")

