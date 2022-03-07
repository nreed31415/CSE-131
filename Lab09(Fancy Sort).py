
def sort(array):
    size = len(array)
    src = array
    des = [0] * size
    num = 2
    
    while num > 1:
        num = 0
        begin1 = 0

        while begin1 < size:
            end1 = begin1 + 1
            while end1 < size and src[end1 - 1] <= src[end1]:
                end1 += 1

            begin2 = end1
            if begin2 < size:
                end2 = begin2 + 1
            else:
                end2 = begin2
            while end2 < size and src[end2 -1] <= src[end2]:
                end2 += 1
            
            num += 1
            des = combine(src, des, begin1, begin2, end2)
            begin1 = end2
        return des 

def combine(source, destination, i_begin1, i_begin2, i_end2):
    i_end1 = i_begin2
    
    for i in range(i_begin1, i_end2):
        if i_begin1 < i_end1 and (i_begin2 == i_end2 or source[i_begin1] < source[i_begin2]):
            destination[i] = source[i_begin1]
            i_begin1 += 1
        else:
            destination[i] = source[i_begin2]
            i_begin2 += 1
    return destination

sorted = False

an_array = [12, 3, 45, 23, 6, 33, 76]


while not sorted:
    an_array = sort(an_array) 
    is_sorted = (input(f'Is {an_array} sorted correctly? (True or False) \n'))
    if is_sorted == 'True':
        sorted = True
