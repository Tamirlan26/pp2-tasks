import re

text = "play playing played player"

result = re.findall(r"play(?:ing|ed)?", text)

print(result)