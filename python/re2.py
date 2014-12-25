# -*- coding:utf-8  -*-
import re

# 分组可以用于对整组数据作判断
matcher = re.compile(r"^(<\w+\s\w+>\s)?([\w\.]+)@(\w+)\.(\w+)$")
print matcher.match("someone@gmail.com").groups()
print matcher.match("bill.gates@microsoft.com").groups()
print matcher.match("<Tom Paris> tom@voyager.org").groups()