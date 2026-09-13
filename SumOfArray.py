class Array:
    def sum(self,arr):
        
    
        arr_sum  = 0
        for num in arr:
                arr_sum = arr_sum + num

        return arr_sum


n = int(input("enter the  size of the array"))
arr = []
for i in range(n):
     a = int(input("Enter numbers"))
     arr.append(a)

                

obj = Array()

c = obj.sum(arr)
print(c)

