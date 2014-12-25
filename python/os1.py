import os
import sys

# print os.path.dirname()

absp = os.path.abspath(".")
print list(os.walk(absp))[0][2]
# 这种方法是在运行时修改，运行结束后失效。
sys.path.append(absp)
# os.environ["PATH"] += "" 运行完保持