a = "a"

assert a == "a","a is not a"

assert True,"haha"
# assert False,"oh gosh"

print __debug__

# when python -O is called it will be False
# and all sentences controlled by __debug__ will be deleted from memory