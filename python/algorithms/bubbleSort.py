#the bubble sort algorithm works by repeatedly swapping the adjacent elements if they are in the wrong order
def bubble_sort(array):
	for i in range(1, len(array)):

		x = i - 1
		#while x is an a valid index and the value of the right of x is less than it, swap the elements
		while(x > -1 and array[x+1] < array[x]):
			array[x],array[x+1] = array[x+1],array[x] 
			x = x - 1


#this algorithm runs in O(n^2) time

nums = [31,0,0,0,0,1,1,1,1,2]
print(nums)
bubble_sort(nums)
print(nums)

print('\n')

arr = [64, 34, 25, 12, 22, 11, 90] 
print(arr)
bubble_sort(arr)
print(arr)