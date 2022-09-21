import cgi

content = cgi.FieldStorage()

print("Content-type: text/html")

user_sex = content.getfirst("sex")
print(user_sex)
