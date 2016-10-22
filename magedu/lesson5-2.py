def partial(fn,*p_args,**p_kwargs):
    def warps(*args,**kwargs):
        return fn(*p_args,*args,**p_kwargs,**kwargs)
    return warps
def add(x,y):
    return x+y
inc = partial(add,y=1)
print(inc(3))