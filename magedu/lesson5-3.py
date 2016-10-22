def dict_eq(a,b):
    for k,v in a.items():
        if k not in b.keys():
            return False
        else:
            if not isinstance(v,(dict,list,set)):
                if v != b[k]:
                    return False
            if isinstance(v,list):
                for i,item in enumerate(v):
                    if len(b[k]) <= i:
                        return False
                    if b[k][i] != item:
                        return False
            if isinstance(v,dict):
                ret = dict_eq(v,b[k])
                if ret is False:
                    return ret

