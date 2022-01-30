from cgi import print_directory


def max(num1, num2):

                if num1 > num2:
                    return num1

                else:
                    return num2

num1 = int(input("Number one"))
num2 = int(input("Number two"))


print(str (max(num1, num2))  + "\n Is the gretest of two numbers" )

