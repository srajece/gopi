import re
a="srjece@gmail.com theena123@gmail.com gmail"
b=re.split("@\w+.\w+\s",a)
print(b)
