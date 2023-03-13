import re
search_string = "hello world"
pattern = "hello world"

match = re.match(pattern, search_string)

"""
if match:
    print("regex matches")
"""

if match:
    template = "'{}' matches pattern '{}'"
else:
    template = "'{}' does not match pattern '{}'"
print(template.format(search_string, pattern))
