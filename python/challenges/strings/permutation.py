#check if one string is a permutation of the other

def check_perm(s1,s2):

	#if the lengths of the strings do not match, they cannot be permutations 
	if len(s1) != len(s2):
		print(s2," is not a permutation of ",s2)
		return

	#check each character in string 1
	for char in s1:
		#if s2 contains char, remove it from s2
		if s2.find(char) >= 0:
			s2 = s2[:s2.find(char)] + s2[s2.find(char)+1:]
		#if s2 does not contain char, this cannot be a permutation
		else:
			print("these strings are not permutations")
			return
	#if all the characters in s2 where not stripped away by the above process, this is not a permutation
	if len(s2) > 0:
		print("these strings are not permutations")
	else:
		print("these strings are permutations")


check_perm("as","sa")
check_perm("nowayisthisapermutation","n0wayisthisapermutation")