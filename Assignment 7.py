import re

text = """
Please contact us at roshanibhapkar5@mail.com or roshani@gmail.com.
You can also email bhapkarroshani@college.edu.in for further information.
"""

# Pattern to find email addresses
pattern = r'[\w.-]+@[\w.-]+\.\w+'

# Find emails from the text
emails = re.findall(pattern, text)

print("Email addresses found:")

for email in emails:
    print(email)