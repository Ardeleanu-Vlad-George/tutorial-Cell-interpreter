#!/usr/bin/python3
from no_put_stack import no_put_stack as nps
from lexer import lex as lx

# Deleted class 'Parser'
# To me it seems silly to introduce a class for this part of the design
# The first one sort of made sense to me, but this one didn't 
# If there is no class called 'lexer', why should there be one called 'parser'
# For simetries sake, the 'parser' file will NOT contain a 'parser' class
# Just the 'parse' method

def many_expr():
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
        args = many_expr(toks, ',', ')')
        return next_expr(toks, end_tok, ('call', prv_expr, args))
    elif typ == '{':
        params = parameter_list(toks, )
        body = many_expr(toks, ';', '}')
        return next_expr(toks, end_tok, ('func', params, body))
    elif typ == '=':
        nxt = next_expr(toks, end_tok, None)
        return next_expr(toks, end_tok, ('asgn', prv_expr, nxt))



def parse():
    pass


if __name__ == "__main__":

    # this is the list of tokens we expect from the lexer, ordered based on the line of code
    # to which they belong
    avg_tok = (
        ('id', 'x'), ('=', ''), ('nr', '10'), (';', ''),
        ('id', 'y'), ('=', ''), ('id', 'x'), ('op', '+'), ('nr', '101'), (';', ''),
        ('id', 'print'), ('(', ''), ('sr', 'This is the result:'), ('op', '+'), ('id', 'y'), (')', ''), (';', '')
    )

    print(avg_tok)

    # here is a list of tokens that only do a simple assignment
    ezy_tok = (
        ('id', 'x'), ('=', ''), ('nr', '-2.4'), (';', '')
    )
