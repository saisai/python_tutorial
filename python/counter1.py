from collections import Counter

c = Counter()

# a dict with its key not necessary to be setted before visiting (automatically)
# and with its value a number
for ch in "laozhikun":
	c[ch] = c[ch] + 1

print c