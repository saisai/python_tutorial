# -*- coding:utf-8  -*-
# import sys
# if len(sys.argv) != 3:
# 	sys.stderr.write("Usage : python %s inputfile outputfile\n"%sys.argv[0])
# 	raise SystemExit(1)
# inputfile = sys.argv[1]
# outputfile = sys.argv[2]
# print "done"

import optparse
p = optparse.OptionParser()

# action="store"说明必须带一个参数
p.add_option("-o",action="store",dest="outfile")
p.add_option("--output",action="store",dest="outfile")

# action="store_true"说明只用来作为标记位
p.add_option("-d",action="store_true",dest="debug")
p.add_option("--debug",action="store_true",dest="debug")

p.set_defaults(debug=False)

opts,args = p.parse_args()

outfile = opts.outfile
debug = opts.debug

if outfile:
	print "get outfile"
if debug:
	print "debugging"