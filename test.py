import re

lines = ["one", "two", "three", "four"]
with open("test.txt", "w") as file:
    for line in lines:
        file.write(line)
        file.write("\n")

codelist = ["asdada-123", "asd123", "asd 123", "1wasd223zsd-123"]
pattern = re.compile("[a-zA-Z]{1,}[- ]{0,}[0-9]{1,}")

resultList = []

for code in codelist:
    match = pattern.search(code)
    if match:
        resultList.append(match.group())

print(resultList)
