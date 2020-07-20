#check if a string is a palindrome

def palindrome(str1):
	if len(str1) <= 1:
		return True
	elif str1[0] != str1[len(str1)-1]:
		return False
	else:
		return palindrome(str1[1:len(str1)-1])


print(palindrome("racecar"))
print(palindrome("tattarrattat"))
print(palindrome("racerrecar"))
print(palindrome("area"))