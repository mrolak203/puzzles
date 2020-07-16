#!/usr/bin/env python3
import math
#this function assumes array is sorted
def binary_search(array, num):

	low = 0
	high = len(array)-1
	
	while low <= high:

		#floor the mid value, index at half of the array based on the high and low values
		mid = low + (high - low)//2 #get median, with the offset of the low index
		#check if num is at mid 
		if array[mid] == num:
			print(num," was found at index ",mid)
			return
		#if num is smaller than mid, search the left part of the array
		elif num < array[mid]:
			high = mid - 1
		#if num is larger than mid, search the right part of the array
		else:
			low = mid + 1

	print(num, "was not found")



def recur_helper(array,num):
	recursive_bs(array, num, 0, len(array)-1)

def recursive_bs(array, num, low, high):

	mid = low + (high - low)//2
	#base case
	if low > high:
		print(num, "was not found")
		return
	#check if mid contains num
	elif array[mid] == num:
		print(num," was found at index ",mid)
		return 
	#if num less than mid, call recursive_bs on left half of array
	elif num < array[mid]:
		return recursive_bs(array,num,low,mid-1)
	#if num greater than mid, call recursive_bs on right half of array
	else:
		return recursive_bs(array,num,mid+1,high)


#this algorithm runs in O(log n) time

binary_search([1,2,3,4,5], 4)
binary_search([1,2,3,4,5], 1)
binary_search([1,2,3,4,5], 40)
binary_search([1,2,3,4,5], -4)


recur_helper([1,2,3,4,5], 5)
recur_helper([1,2,3,4,5], 20)
recur_helper([1,2,3,4,5], -5)