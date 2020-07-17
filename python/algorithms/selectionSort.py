# the selection sort algorithm sorts an array by finding the minimum element from the unsorted part
# and putting it at the beginning. The algorithm maintaines two subarrays within a given array.

def selection_sort(array):

	index = 0
	maxn = len(array)
	
	#iterate through all indcies 
	while index < maxn:
		#minnum will be the index of the smallest num in the array 
		minnum = index
		#iterate to find the index smallest num
		for x in range(index+1, maxn):
			if array[x] < array[minnum]:
				minnum = x
		#once the smallest element in the unsorted subarray is found, it is swapped to the end of the sorted subarray 
		array[index],array[minnum] = array[minnum],array[index]

		index = index + 1


#this algorithm runs in O(n^2) time

nums = [31,0,0,0,0,1,1,1,1,2]
print(nums)
selection_sort(nums)
print(nums)


