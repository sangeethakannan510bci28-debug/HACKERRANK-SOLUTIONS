def fun(s):
    try:
        n, m = s.split("@")
        w, e = m.split(".", 1)
    except ValueError:
        return False
    if not n or not w or not e:
        return False
    sp= "_-"
    def cond1(n):
        for i in n:
            if not (i.isupper() or i.islower() or i.isdigit() or i in sp):
                return False
        return True
        
    def cond2(w):
        for i in w:
            if not (i.isupper() or i.islower() or i.isdigit()):
                return False
        return True
        
        
    def cond3(e):
        if len(e) > 3:
            return False
        for i in e:
            if not (i.isupper() or i.islower()):
                return False
        return True
    result = all([cond1(n),cond2(w),cond3(e)])
    return result
            
            
    # return True if s is a valid email, else return False
