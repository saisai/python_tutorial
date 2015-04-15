# -*- coding:utf-8  -*-

array = [1,4,12,23,76,25]

def findpivot(array):
	return len(array)/2-1


def partition(array):
	pass

def swap(array,i,j):
	# super elegant
	array[i],array[j] = array[j],array[i]

def quicksort(array,l,r):
	# 首先找pivot
	pivot_index = findpivot(array)
	pivot_value = array[pivot_index]
	print "pivot_value",pivot_value

	# 然后将pivot放到数据的末尾
	swap(array,pivot_index,len(array)-1)
	print array

	while r - l > 1:
		while array[l] <= pivot_value and l<=len(array)-2:
			l += 1
			print "l",l
			continue
		
		while array[r] > pivot_value and r >= 0:
			r -= 1
			print "r",r
			continue

		swap(array,l,r)
		print array

	swap(array,l,r)
	print array

	# 现在pivot就在l了
	swap(array,l,len(array)-1)
	print array

	quicksort(array,0,l)
	quicksort(array,l+1,len(array)-1)






if __name__ == "__main__":
	quicksort(array,0,len(array)-2)
