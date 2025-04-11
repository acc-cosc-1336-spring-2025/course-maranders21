#
def get_p_distance(list1, list2):
    diff_count = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            diff_count += 1
    p_distance = diff_count/len(list1)
    return p_distance

def get_p_distance_matrix(list1):
    matrix = []
    for i in range(len(list1)):
        inner_list = []
        for j in range(len(list1)):
            hem_val = get_p_distance(list1[i],list1[j])
            inner_list.append(hem_val)
        matrix.append(inner_list)
    return matrix