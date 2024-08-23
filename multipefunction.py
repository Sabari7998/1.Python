class addtionalfunction():
    def marriage():
        gender=input("enter your gender male or female:")
        age=int(input("enter your age:"))
        if(gender=="male" and age>21):
            print("you are eligible for marriage")
            msg="you are eligible for marriage"
        elif(gender=="female" and age>18):
            print("you are eligible for marriage")
            msg="you are eligible for marriage"
        else:
            print("you are not eligible for marriage") 
            msg="you are not eligible for marriage"
        return msg
    def oddeven():
        num=int(input("Enter a number:"))
        if(num %2==0):
            print(num,"number is even")
            msg="number is even"
        else:
            print(num,"number is odd")
            msg="number is odd"
        return msg
    def BMI():
        user=int(input("Enter the BMI Index:"))
        if(user<19):
            print("low weight")
            msg=("low weight")
        elif(user<25):
            print("normal weight")
            msg=("normal weight")
        elif(user<29):
            print("heavy weight")
            msg=("heavy weight")
        else:
            print("very heavy weight")
            msg=("very heavy weight")
        return msg
