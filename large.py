def largest(arr,n):
	max=arr[0]
	for i in range(1,n):
                  if arr[i]>max:
                      	max=arr[i]
	return max
arr=[5, 4, 3, 2, 1, 7, 6, 10, 8, 9]
n=len(arr)
Ans=largest(arr,n)
print(Ans)
