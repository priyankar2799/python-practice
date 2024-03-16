import re
# pattern matching with search,find function
name ="A school vision statement focuses on the school's future; its purpose is to state how a school, together, can grow. A successful vision statement is clear and concise (usually less than 20 words) but can go over if necessary to detail its goals."
pattern =r"school"
result = re.search(pattern,name)
if result:
    print("pattern found:", result.group())
    print(len(result.group()))
else:
    print("pattern not found")

# split regexp
pattern= ","
print(re.split(pattern,name))

# replace regexp
pattern = "school"
replacement = "home"
print(re.sub(pattern,replacement,name))