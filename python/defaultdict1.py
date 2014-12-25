from collections import defaultdict


# return default value when key doesnt exist
d = defaultdict(lambda :"N/A")

d["key1"] = "value1"
d["key2"] = "value2"

print d["key1"]
print d["hello"]