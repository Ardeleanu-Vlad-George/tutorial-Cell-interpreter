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
        var_name = exp[1][1]
        val = eval_exp(exp[2], env)
        env.items[var_name] = val
        return val
    elif act == 'call'
        return call(exp, env)
    # to complete with the part where you define a function


def call(exp, env):
    fn_name = exp[1]
    fn_args = list(eval_exp(_, env) for _ in exp[2])
    # keep it simple
    print(fn_name, fn_args)

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

