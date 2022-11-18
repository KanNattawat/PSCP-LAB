'''PSCP Program'''
def main():
    '''8437-T-Score 18/11/2022'''
    total_stu = int(input())
    _ = int(input())
    all_score = [int(input()) for i in range(total_stu)]
    mean = sum(all_score)/total_stu
    temp = 0
    for i in all_score:
        temp += (i - mean)**2
    s_d = ((total_stu*temp)/(total_stu*(total_stu-1)))**0.5
    for i in all_score:
        var_z = (i-mean)/s_d if s_d != 0 else 0
        print("%.2f"% ((var_z*10)+50))
main()
