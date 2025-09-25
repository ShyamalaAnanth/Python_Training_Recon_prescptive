#Check Palindrome in single line 
print('madam'=='madam');

#Extract letters and digits
str1='Python@123'
print("Given input string is:",str1,"and its length is",len(str1));
print("Extracted letters from given string is:",str1[:6]);
print("Extracted digits from given string is:",str1[7:]);

#Remove spaces from input
str2='''" Python is fun "'''
print("Input string is:",str2);
str3=str2.replace(" ","",1);
str4=str3[14:16].replace(" ","");
str5=str3[:14]+str4
print("Output string is:",str5);

#Checking methods for numeric and alphanumberic
string1="12345";
string2="1231/3";
string3="Python3";
string4="Python 3";
#Check String1 fo all methods
print(string1,"is a alphanumeric:",string1.isalnum());
print(string1,"is a digit:",string1.isdigit());
print(string1,"is a numeric:",string1.isnumeric());
#Check String2 fo all methods
print(string2,"is a alphanumeric:",string2.isalnum());
print(string2,"is a digit:",string2.isdigit());
print(string2,"is a numeric:",string2.isnumeric());
#Check String3 fo all methods
print(string3,"is a alphanumeric:",string3.isalnum());
print(string3,"is a digit:",string3.isdigit());
print(string3,"is a numeric:",string3.isnumeric());
#Check String4 fo all methods
print(string4,"is a alphanumeric:",string4.isalnum());
print(string4,"is a digit:",string4.isdigit());
print(string4,"is a numeric:",string4.isnumeric());

#Input a number and print positive negative or zero
num=int(input("Enter a number to proceed:"));
if num > 0:
    print("Entered number is a positive number");
elif num < 0:
    print("Entered number is a positive number");
else:
    print("Entered number is zero");

#Find grade based on mark
mark=int(input("Enter mark to find grade:"));
if mark >= 90:
    print("Grade is A+");
elif mark >= 80 and mark <= 89 :
    print("Grade is B");
elif mark >=70 and mark <=79:
    print("Grade is C");
else: 
    print("Grade is fail");

#greatest of three numbers based on user input 
num1=int(input("Enter num1 to proceed:"));
num2=int(input("Enter num2 to proceed:"));
num3=int(input("Enter num3 to proceed:"));
print("The user inputed numbers are:",num1,num2,num3);
if (num1 > num2) and (num1 > num3):
    print(num1,"is greatest of the three numbers");
elif (num2 > num1) and (num2 > num3):
    print(num2,"is greatest of the three numbers");
else:
    print(num3,"is greatest of the three numbers");

#Check if the inputted number is a multiple of 7
a=int(input("Enter a number to continue:"));
if ((a%7) == 0):
    print(a,"is a multiple of 7");
else:
    print(a,"is not a multiple of 7");
