import re

pattern = "[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|edu|net)"
user_input = input("Enter your email address: ")
if re.search(pattern, user_input):
    print("Valid email address")
else:
    print("Invalid email address")