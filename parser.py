#!/usr/bin/python3
from no_put_stack import no_put_stack as nps
from lexer import lex as lx

# Deleted class 'Parser'
# To me it seems silly to introduce a class for this part of the design
# The first one sort of made sense to me, but this one didn't 
# If there is no class called 'lexer', why should there be one called 'parser'
# For simmetry's sake, the 'parser' file will NOT contain a 'parser' class
# Just the 'parse' method

def expr_chain(toks, sep_tok, end_tok):
    """
        'toks' - the tokens that will be processed, an object of type 'nps'
        'sep_tok' - the ending tokens, in 'Cell' these can be ';', ')', '}'
                    they are the tokens that signal the end of an expression
        'end_tok' - the token that signals the end of the current expr of the expression currently being build
    """
    chain = []
    typ = toks.next[0]
    if typ == end_tok:
        toks.pop_next()
        return []
    else:
        while typ != end_tok:
            part = next_expr(toks, (sep_tok, end_tok), None)
            if part is not None:
                chain.append(part)
            typ = toks.next[0]
            toks.pop_next()
    return chain

def parameter_list(toks):
    if toks.next[0] != ':':
        return []
    toks.pop_next()
    if toks.next[0] == '(':
        toks.pop_next()
        return expr_chain(toks, ',', ')')
    pass

# 'expr' stands for expression
def next_expr(toks, end_tok, prv_expr):
    """
        'toks' - the tokens that will be processed, an object of type 'nps'
        'end_tok' - the ending tokens, in 'Cell' these can be ';', ')', '}'
                    they are the tokens that signal the end of an expression
        'prv_tok' - the previous token of the expression currently being build
    """
    typ, val = toks.next # extract tokens type and value
    if typ in end_tok: # if it's an ending token
        return prv_expr # return the previous token 
    # eliminate the already extracted token so the list may be prepared 
    # for the recursive calls of 'next_expr'
    toks.pop_next()
    #if the following conditions are true, we are at the beginning of an expression
    if typ in ('nr', 'id', 'sr') and prv_expr is None:
        return next_expr(toks, end_tok, (typ, val)) 
        # feed the token to the next expression it itself as an expression
        # 'nr' will be converted to numbers, 'id' will point to their value 
    elif typ == 'op': # if an operation was detected
        # build up the second operand 
        nxt = next_expr(toks, end_tok, None) # yes, start the previus from 'None'
        return next_expr(toks, end_tok, ('comp', val, prv_expr, nxt))
    elif typ == '(':
        args = expr_chain(toks, ',', ')')
        return next_expr(toks, end_tok, ('call', prv_expr, args))
    elif typ == '{':
        params = parameter_list(toks)
        body = expr_chain(toks, ';', '}')
        return next_expr(toks, end_tok, ('func', params, body))
    elif typ == '=':
        nxt = next_expr(toks, end_tok, None)
        return next_expr(toks, end_tok, ('asgn', prv_expr, nxt))



def parse(toks):
    while toks.next is not None:
        part = next_expr(toks, ';', None)
        if part is not None:
            yield part
        toks.pop_next()


if __name__ == "__main__":

    # this is the list of tokens we expect from the lexer, ordered based on the line of code
    # to which they belong
    avg_tok = (
        ('id', 'x'), ('=', ''), ('nr', '10'), (';', ''),
        ('id', 'y'), ('=', ''), ('id', 'x'), ('op', '+'), ('nr', '101'), (';', ''),
        ('id', 'print'), ('(', ''), ('sr', 'This is the result:'), ('op', '+'), ('id', 'y'), (')', ''), (';', '')
    )

    # here is a list of tokens that only do a simple assignment
    ezy_tok = (
        ('id', 'x'), ('=', ''), ('nr', '-2.4'), (';', '')
    )
    # print("AST of %s" % (ezy_tok,), tuple(parse(nps(ezy_tok))), sep='\n', end='')
    print(tuple(parse(nps(avg_tok))))

(('id', 'x'), ('=', ''), ('nr', '10'), (';', ''), ('id', 'y'), ('=', ''), ('id', 'x'), ('op', '+'), ('nr', '101'), (';', ''), ('id', 'MSG'), ('=', ''), ('sr', 'This is the result:'), (';', ''), ('id', 'print'), ('(', ''), ('id', 'MSG'), (',', ''), ('id', 'y'), (')', ''), (';', ''))
