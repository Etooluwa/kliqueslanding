import re

with open("index.html", "r") as f:
    content = f.read()

# Replace emdash with regular dash
content = content.replace("—", "-")

with open("index.html", "w") as f:
    f.write(content)

print("Em dashes replaced.")
