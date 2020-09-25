def bubblesort(list):

# Swapping the index to organize in the correct order 
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp


list = [59,81,47,45,49,71,140,30]
bubblesort(list)
print(list)