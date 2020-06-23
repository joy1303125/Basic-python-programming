import re
text=" ring. joydatta@gmail.com. he is good also"
pattern= re.compile("[a-zA-Z0-9\_\-]+ @[a-zA-Z0-9]+\.[a-zA-Z0-9]+ ")
result=pattern.search(text)
print(result)