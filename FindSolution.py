def is_correct_data(criteria_relationship, objects_relationship):
    flag = True
    flag = flag and (len(criteria_relationship) ==6)and (len(objects_relationship) ==4)
    for list in objects_relationship:
        flag = flag and (len(list) ==3)
    return flag
    

def FindSolution(criteria_relationship, objects_relationship):
    if not is_correct_data(criteria_relationship, objects_relationship):
        return -1
    criteria_weight = matrix_weight(matrix(criteria_relationship))
    objects_weight = []
    for list_relationship in objects_relationship:
        weight=matrix_weight(matrix(list_relationship))
        objects_weight.append(weight)
    final_list= mult_matrix(objects_weight, criteria_weight)
    final_percent_list, max_id = list_to_percent
    return final_list, final_percent_list, max_id