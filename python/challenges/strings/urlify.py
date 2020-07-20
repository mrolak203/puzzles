#replace all spaces in a string with '%20'. 
#Assume the string has enough appended space to hold the full url
#You are given the 'true' length of the string

def urlify(str1, length):
	#this value will keep track of the updated length of the array
	expanded_size = length
	#convert the string into a list for easier character manipulation
	s = list(str1)

	#iterate over each char in the list
	for i in range(0, length):
		#if the character at i is a space, the string must be expanded
		if s[i] == ' ':
			#move every char 2 spaces to the right
			for j in range(expanded_size-1, i, -1):
				s[j+2] = s[j]
			#insert the '%20'
			s[i] = "%"
			s[i+1] = '2'
			s[i+2] = '0'
			#increase the index of i to the next char after the '%20'
			i = i + 3
			#expand the size of the string by 2 chars
			expanded_size+=2

	#turn the char list back into a string
	str1 = "".join(s)
	print(str1)


urlify("Mr Thor Finch    ", 13)




