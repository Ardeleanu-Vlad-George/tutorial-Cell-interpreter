#!/usr/bin/python3
# Standard Library
import sys
# The components of the interpreter
import comp.evaluator
import comp.parser
import comp.lexer
import comp.scope

with open(sys.argv[1], 'r') as source:
    source = source.readlines()
    code = ''
    for line in source:
        code += line

# print(code, end='')
envt = comp.scope.scope(stdin = sys.stdin, stdout = sys.stdout, stderr = sys.stderr)
print('No, I am the printer:', comp.evaluator.eval_ast( comp.parser.parse(comp.parser.nps(comp.lexer.lex(code))), envt))
