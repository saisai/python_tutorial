s = "for i in range(0,10): print i"
c = compile(s,"","exec")
eval(c)
exec(c)