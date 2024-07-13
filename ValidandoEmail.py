import re

def fun(s):
    pattern = r'^[\w|\-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$'
    return re.search(pattern, s) != None

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input("Enter a number of emails you want to check:"))
    emails = []
    for _ in range(n):
        emails.append(input("Email:"))

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(f"Valid emails: {filtered_emails}")