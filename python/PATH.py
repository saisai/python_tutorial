# -*- coding:utf-8 -*-
import optparse
import os
import sys

os.environ["PATH"]='''/usr/bin:/Users/Laozhikun/.pyenv/libexec:/Users/Laozhikun/.pyenv/plugins/python-build/bin:/Users/Laozhikun/.pyenv/shims:/Users/Laozhikun/.pyenv/bin:/Users/Laozhikun/Downloads/cocos2d-x-3.0rc0/tools/cocos2d-console/bin:/opt/local/bin:/opt/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/Applications/Server.app/Contents/ServerRoot/usr/bin:/Applications/Server.app/Contents/ServerRoot/usr/sbin:/Users/Laozhikun/Qt5.1.1/5.1.1/clang_64/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:/Users/Laozhikun/.pyenv/bin:/Users/Laozhikun/Downloads/cocos2d-x-3.0rc0/tools/cocos2d-console/bin:/opt/local/bin:/opt/local/sbin:/usr/local/share/python:/usr/local/share/python/bin:/usr/local/share/python/sbin:/usr/local/share/npm/bin:/Users/Laozhikun/.cask/bin:/Users/Laozhikun/.cabal/bin:/usr/local/bin:/usr/bin:/Users/Laozhikun/.pyenv/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Applications/Server.app/Contents/ServerRoot/usr/bin:/Applications/Server.app/Contents/ServerRoot/usr/sbin:/Users/Laozhikun/.pyenv/shims:/Users/Laozhikun/.pyenv/bin:/Users/Laozhikun/Downloads/cocos2d-x-3.0rc0/tools/cocos2d-console/bin:/opt/local/bin:/opt/local/sbin:/Users/Laozhikun/Qt5.1.1/5.1.1/clang_64/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:/usr/local/share/python:/usr/local/share/python/bin:/usr/local/share/python/sbin:/usr/local/share/npm/bin:/Users/Laozhikun/.cask/bin:/Users/Laozhikun/.cabal/bin:/usr/local/sbin:/Users/Laozhikun/workspace/golang/bin:/Users/Laozhikun/workspace/golang/bin:/Users/Laozhikun/Qt5.1.1/5.1.1/clang_64/bin'''

p = optparse.OptionParser()

# append new variable to PATH
# 1
p.add_option("-a",action="store",dest="append_item")
p.add_option("--append",action="store",dest="append_item")

# prepend new variable to PATH
# 2
p.add_option("-p",action="store",dest="prepend_item")
p.add_option("--prepend",action="store",dest="prepend_item")

# show the PATH
# 3
p.add_option("-s",action="store_true",dest="isShow")
p.add_option("--show",action="store_true",dest="isShow")

# insert at specific index
# 4
# p.add_option("-i",action="store",dest="insert_index")
# p.add_option("--insert",action="store",dest="insert_index")

# to remove the last variable from PATH
# 5
p.add_option("--pop",action="store_true",dest="isPop")

# client mode
# 6
p.add_option("--silent",action="store_true",dest="isSilent")

p.set_defaults(isShow=False,isPop=False,isSilent=False)

opts,args = p.parse_args()

# 有--show会覆盖--silent
if opts.isShow:
	print os.environ["PATH"]
	SystemExit(1)

if opts.isSilent:
	sys.stdout = open("../resource/temp.txt","w")

if opts.isPop:
	lst = os.environ["PATH"].split(":")
	lst.pop()
	os.environ["PATH"] = ":".join(lst)
	print os.environ["PATH"]
	SystemExit(1)

append_item = opts.append_item
if append_item:
	os.environ["PATH"] = "%s:%s"%(os.environ["PATH"],append_item)
	print os.environ["PATH"]
	SystemExit(1)

prepend_item = opts.prepend_item
if prepend_item:
	os.environ["PATH"] = "%s:%s"%(prepend_item,os.environ["PATH"])
	print os.environ["PATH"]
	SystemExit(1)





# priority:

os.environ["PATH"] = '''/usr/bin:/Users/Laozhikun/.pyenv/libexec:/Users/Laozhikun/.pyenv/plugins/python-build/bin:/Users/Laozhikun/.pyenv/shims:/Users/Laozhikun/.pyenv/bin:/Users/Laozhikun/Downloads/cocos2d-x-3.0rc0/tools/cocos2d-console/bin:/opt/local/bin:/opt/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/Applications/Server.app/Contents/ServerRoot/usr/bin:/Applications/Server.app/Contents/ServerRoot/usr/sbin:/Users/Laozhikun/Qt5.1.1/5.1.1/clang_64/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:/Users/Laozhikun/.pyenv/bin:/Users/Laozhikun/Downloads/cocos2d-x-3.0rc0/tools/cocos2d-console/bin:/opt/local/bin:/opt/local/sbin:/usr/local/share/python:/usr/local/share/python/bin:/usr/local/share/python/sbin:/usr/local/share/npm/bin:/Users/Laozhikun/.cask/bin:/Users/Laozhikun/.cabal/bin:/usr/local/bin:/usr/bin:/Users/Laozhikun/.pyenv/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Applications/Server.app/Contents/ServerRoot/usr/bin:/Applications/Server.app/Contents/ServerRoot/usr/sbin:/Users/Laozhikun/.pyenv/shims:/Users/Laozhikun/.pyenv/bin:/Users/Laozhikun/Downloads/cocos2d-x-3.0rc0/tools/cocos2d-console/bin:/opt/local/bin:/opt/local/sbin:/Users/Laozhikun/Qt5.1.1/5.1.1/clang_64/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:/usr/local/share/python:/usr/local/share/python/bin:/usr/local/share/python/sbin:/usr/local/share/npm/bin:/Users/Laozhikun/.cask/bin:/Users/Laozhikun/.cabal/bin:/usr/local/sbin:/Users/Laozhikun/workspace/golang/bin:/Users/Laozhikun/workspace/golang/bin:/Users/Laozhikun/Qt5.1.1/5.1.1/clang_64/bin'''
