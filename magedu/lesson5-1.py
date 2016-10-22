from functools import wraps
def typed(*type_args,**type_kwargs):
    def dec(fn):
        @wraps(fn)
        def wrap(*args,**kwargs):
            for i,t in enumerate(type_args):
                if not isinstance(args[i],t):
                    print('pos {} argument {}'.format(i,args[i]))
                    return None
            for k,t in type_kwargs.items():
                if not isinstance(kwargs[k],t):
                    print('pos {} argument {}'.format(k, args[k]))
                    return None
            return fn(*args,**kwargs)
        return wrap
    return dec

@typed(x=int,y=int)
def add(x,y):
    return x + y

add(1,2)
