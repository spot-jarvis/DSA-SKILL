class Solution:
	def maxProduct(self,arr):
		# code here
		maxprod = arr[0]
		curr_min = arr[0]
		curr_max = arr[0]
		n = len(arr)
		
		for i in range(1,n):
		    
		    temp = max(arr[i],curr_min * arr[i],curr_max * arr[i])
		    curr_min  = min(arr[i],curr_min * arr[i],curr_max * arr[i])
		    
		    curr_max = temp
		    
		    maxprod = max(curr_min,curr_max,maxprod)
		return maxprod

# There is an another  way,from lefttoright and righttoleft..
class Solution:
	def maxProduct(self,arr):
		# code here
		n = len(arr)
		left_to_right = 1
		right_to_left = 1
		max_prod = arr[0]
		for i in range(n):
		    if left_to_right == 0:
		        left_to_right = 1
		        
		    if  right_to_left ==0:
		        right_to_left = 1
		        
		    left_to_right *= arr[i]
		    
		    j = n-i-1
		    
		    right_to_left *= arr[j]
		    
		    max_prod = max(left_to_right,right_to_left,max_prod)
		    
		return max_prod
