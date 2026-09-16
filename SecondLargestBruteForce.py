class Solution:
    def getSecondLargest(self, arr):
        
        arr = sorted(set(arr),reverse = True)
        
        if len(arr) < 2:
            return -1
            
        return arr[1]
        
        # here set is the python built function where it will remove the 
        # duplicates and converts it into set
        
        
        
        
        
        
        
        
    
    