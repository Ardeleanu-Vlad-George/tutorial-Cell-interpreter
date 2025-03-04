#!/usr/bin/python3
from env import env as E

def eval_ast(ast, env):
    ret = ("none",)
    for expr in ast:
        ret = expr
    return ret

def eval_exp(exp,env):
    act = exp[0]
    if act == 'nr':
        return ('nr', float(exp[1]))
    elif act == 'sr':
        return ('sr', exp[1])
    elif act == 'comp':
        return comp(exp, env)
    elif act == 'id':
        name = exp[1]
        ret = env.search(name)
        return ret
    elif act == 'asgn':
    # to continue


def comp(exp, env):
    p1 = eval_exp(exp[2], env)
    p2 = eval_exp(exp[3], env)
    if exp[1] == '+':
        return ('nr', p1+p2)
    elif exp[1] == '/':
        return ('nr', p1/p2)
    elif exp[1] == '*':
        return ('nr', p1*p2)
    elif exp[1] == '-':
        return ('nr', p1-p2)

