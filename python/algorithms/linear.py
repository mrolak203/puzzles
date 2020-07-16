#!/usr/bin/env python3

def linear_search(array, num):

	for x in array:
		if x == num:
			print("found ", num)
			return
	print("not found")

#this algorithm runs in O(n) time


linear_search([1,2,3,4,5], 4)
linear_search([1,2,3,4,5], 1)
linear_search([1,2,3,4,5], 40)
linear_search([1,2,3,4,5], -0)