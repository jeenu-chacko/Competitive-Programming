
def ref(array,index):
    
    if index > 2:
        print(array)
        return
    
    array.append(s[index])
    ref(array,index+1)
              
    array.remove(s[index])
    ref(array,index+1)
    
s = ['a','b','c']
n = 3
array = []
index = 0
ref(array,index)
