import re
def func(s):
    if re.search('^\w*(\w.\d)@\w*(\.\w)',s):
        print("Valid Email-ID")
    else:
        print("Invalid Email-ID")
s=input("Enter the Email-ID:")
func(s)


'''
output:

Enter the Email-ID:theena@gmail.com
Valid Email-ID


Enter the Email-ID:theenathayalan0706@gmail.com
Valid Email-ID


Enter the Email-ID:theena@gmail23.com
Invalid Email-ID


Enter the Email-ID:theenathayalan0706
Invalid Email-ID


Enter the Email-ID:3@gmail.com
Invalid Email-ID


Enter the Email-ID:theena@.com
Invalid Email-ID


Enter the Email-ID:theena@23.com
Invalid Email-ID


Enter the Email-ID:theena@23gmail.com
Invalid Email-ID
