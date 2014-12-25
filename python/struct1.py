# -*- coding:utf-8 -*-

# Python提供了一个struct模块来解决str和其他二进制数据类型的转换。
import struct

# >表示字节顺序是big-endian，也就是网络序，I:4字节无符号整数。
print struct.pack(">I",10240099)

# H:2字节无符号整数
print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')

s = ""
with open("/Users/Laozhikun/Pictures/wood.bmp","rb") as f:
	s = f.read(30)  # 这个size按照字节算

# Windows的位图文件（.bmp）是一种非常简单的文件格式，我们来用struct分析一下。
# s = '\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

# 'BM'表示Windows位图，'BA'表示OS/2位图
print struct.unpack('<ccIIIIIIHH', s)