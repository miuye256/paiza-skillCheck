import re

ns = input()

ans = re.sub(r"\D", "", ns)
print(ans)

"""
ns = input()

ans = ''.join(filter(str.isdigit, ns))
print(ans)
"""