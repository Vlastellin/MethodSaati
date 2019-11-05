def is_correct_data(criteria_relationship, objects_relationship):
    flag = True
    flag = flag and (len(criteria_relationship) ==6)and (len(objects_relationship) ==4)
    for list in objects_relationship:
        flag = flag and (len(list) ==3)
    return flag
    
    
def test():
    return 6

def to_matrix(coefficients_list):
    length =len(coefficients_list)
    iterator=0
    while (length>0):
        iterator+=1
        length-=iterator
    result=[]
    length=iterator+1
    for i in range(length):
        result.append([])
        for j in range(length):
            result[i].append(1)
    iterator=0
    for i in range(length-1):
        for j in range(i+1, length):
            result[i][j]=coefficients_list[iterator]
            result[j][i]=1/coefficients_list[iterator]
            iterator+=1
    return result      

def matrix_weight(matrix):
    length = len(matrix)
    columns=[]
    weights=[]
    for i in range(length):
        columns.append(0)
        weights.append(0)
    for i in range(length):
        for j in range(length):
            columns[j]+=matrix[i][j]
    
    for i in range(length):
        for j in range(length):
            weights[i]+=matrix[i][j]/columns[j]
    for i in range(length):
        weights[i]=weights[i]/length
    return weights

def mult_matrix(matrix, l):
    result=[]
    for i in range(len(matrix[0])):
        el=0
        for j in range(len(l)):
            el+=matrix[j][i]*l[j]
        result.append(el)
    return result

def list_to_percent(l):
    summ=0
    for el in l:
        summ+=el
    new_list=[]
    max_id=0
    for i, el in enumerate(l):
        if l[max_id]<el:
            max_id=i
        new_list.append(round((el*100)/summ,2))
    return new_list, max_id

def FindSolution(criteria_relationship, objects_relationship):
    #if not is_correct_data(criteria_relationship, objects_relationship):
    #    return -1
    criteria_weight = matrix_weight(to_matrix(criteria_relationship))
    objects_weight = []
    for list_relationship in objects_relationship:
        weight=matrix_weight(to_matrix(list_relationship))
        objects_weight.append(weight)
    
    final_list= mult_matrix(objects_weight, criteria_weight)
    final_percent_list, max_id = list_to_percent(final_list)
    return final_list, final_percent_list, max_id