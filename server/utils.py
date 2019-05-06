import pulp

from planes import *

def optimize(V, S, D):
    opt_model = pulp.LpProblem('Model', pulp.LpMinimize)
    x = pulp.LpVariable.dicts('X', [i for i in range(cnt_planes)], lowBound = 0, upBound = None, 
                                    cat = pulp.LpInteger)

    opt_model += sum([ planes[i].Price * x[i] for i in range(cnt_planes)])
    opt_model += sum([planes[i].Voice * x[i] for i in range(cnt_planes)]) >= V
    opt_model += sum([planes[i].Sms * x[i] for i in range(cnt_planes)]) >= S
    opt_model += sum([planes[i].Data * x[i] for i in range(cnt_planes)]) >= D

    opt_model.solve()
    r=[]
    for i in range(cnt_planes):
        r.append(x[i].value())
    return r

def answer_formatter(a):
    r = ""
    for i in range(cnt_planes):
        if a[i] > 0:
            r += f'{int(a[i])} de {planes[i]} \n'
    return r

