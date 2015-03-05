from sympy import lambdify

def _create_func(ex,lib):
    symbs = list(ex.free_symbols)
    names = [e.name for e in symbs]
    s = sorted(zip(names,symbs))
    names, symbs = zip(*s)
    return lambdify(symbs,ex,lib), names
    
def domath(df,exp,lib='math'):    
    afunc, names = _create_func(exp,lib)
    
    tdf = df.copy()
    
    for name in names:
        if name not in tdf.columns:
            if "_" in name:
                v,i = name.split("_")
                tdf[name] = tdf[v].shift(int(i)*-1)

    vals = tdf[list(names)].values
    return [afunc(*val) for val in vals]