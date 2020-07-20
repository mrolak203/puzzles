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

