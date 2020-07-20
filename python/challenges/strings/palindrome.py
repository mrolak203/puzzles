#check if a string is a palindrome

def palindrome(str1):
	if len(str1) <= 1:
		return True
	elif str1[0] != str1[len(str1)-1]:
		return False
	else:
		return palindrome(str1[1:len(str1)-1])

#check if a string is a permutation of a palindrome 

def perm_of_pal(str1):
	#dictionary to count occurence of characters
	dic = {}
	#remove white space chars
	str1 = str1.replace(' ','')

	#iterate through each char and put them into the dict
	for char in str1:
		if char not in dic:
			dic[char] = 1
		else:
			dic[char]+=1
	#check how many odd values exist, if there is more than 1 this cannot be a palindrome
	oddCount = 0
	for key in dic:
		if dic[key]%2 != 0:
			oddCount+=1

	if len(str1)%2 != 0 and oddCount == 1:
		return True
	elif oddCount == 0 and len(str1)%2 == 0:
		return True
	else:
		return False

print(perm_of_pal("atco cta"))
print(perm_of_pal("taco cat"))
print(perm_of_pal("taco car"))