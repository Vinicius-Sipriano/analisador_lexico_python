import re

txt = "The rain in Spain"
x = re.findall("Spain", txt)
print(x)

txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# Exemplos:
# https://www.w3schools.com/python/python_regex.asp
# https://www.youtube.com/watch?v=H0sLFn7EmnU