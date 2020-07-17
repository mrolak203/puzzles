

def insertion_sort(array):

	#loop through element 1 to element n-1 of the array
	for i in range(1,len(array)):

		element = array[i]
		x = i - 1
		#while the element is less than the value on its left, shift that value over by one to make
		#space for the insertion of the element at its proper location 
		while(element < array[x] and x > -1):
			array[x + 1] = array[x]
			x = x - 1
		#insert the element into the sorted sequence, if the sequence was already sorted, this will just be
		# the same as the orriginal i location 
		array[x + 1] = element 

	


nums = [31,0,0,0,0,1,1,1,1,20]
print(nums)
insertion_sort(nums)
print(nums)