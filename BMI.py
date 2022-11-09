""" BMI """
 
def main():
    """ BMI """
    name1 = input()
    weight1 = float(input())
    height1 = float(input())
    name2 = input()
    weight2 = float(input())
    height2 = float(input())
    name3 = input()
    weight3 = float(input())
    height3 = float(input())
    name4 = input()
    weight4 = float(input())
    height4 = float(input())
    name5 = input()
    weight5 = float(input())
    height5 = float(input())
    print(name1+"'s  BMI = " + "%.2f" %(weight1/(height1/100)**2))
    print(name2+"'s  BMI = " + "%.2f" %(weight2/(height2/100)**2))
    print(name3+"'s  BMI = " + "%.2f" %(weight3/(height3/100)**2))
    print(name4+"'s  BMI = " + "%.2f" %(weight4/(height4/100)**2))
    print(name5+"'s  BMI = " + "%.2f" %(weight5/(height5/100)**2))
 
main()
