# -*- coding:utf-8 -*-

import re
mat = re.match(r"^(\d{3})\-(\d{3,8})$","010-12345")
print mat.group(0)
print mat.group(1)
print mat.group(2)
print mat.groups()
print mat.groups()[0]
print mat.groups()[1]

# 用()表示的就是要提取的分组（Group）

test_str = "12-45-65"
matcher = re.compile(r"^(\d{2})\-(\d{2})\-(\d{2})$")
print matcher
print matcher.match(test_str).groups()

# 默认贪婪匹配
print re.match(r'^(\d+)(0*)$', '102300').groups()
# 非贪婪匹配（也就是尽可能少匹配）
print re.match(r'^(\d+?)(0*)$', '102300').groups()

# 有些时候，用正则表达式也无法做到完全验证

# re也有split
print 'a b   c'.split(' ')
print re.split(r'\s+', 'a b   c')
print re.split(r'[\s\,]+', 'a,b, c  d')
# [\s\,\;]+的意思是说，这三个里面任意凑，数量至少为1,不一定全都是一个字母
print re.split(r'[\s\,\;]+', 'a,b;; c  d')

