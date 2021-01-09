from Lexer import Lexer
from Parser import Parser
from PolishNotation import PN
from Stack_Machine import stack_machine
from Processing_Triad import Triad
from Manager_Of_Threads import Thread_manager
from Thread import Thread

f = open('3TestingProg.txt')
inp = f.read()
f.close()

print('\nLexer:')
l = Lexer()
tokens = l.lex(inp)

p = Parser(tokens)
pars = p.lang()
print('\nParser:', pars)

if pars:
    pn = PN(tokens)
    transfer, fun = pn.transfer_PN()

    tr = Triad(transfer, fun)
    t, val = tr.triad_op()

    for i in range(len(fun)):
        print("\nFunctions triads processing:")
        triad = Triad(fun[i][-1], fun)
        fun[i][-1] = triad.triad_op(False)

    sm = stack_machine(t, val, fun)
    thread_flag = 'n'
    print('\nDo you want to run multi thread? [y/n]')
    thread_flag = input()
    if thread_flag == 'y':
        main_th = Thread('main', stack_machine(t, val, fun))
        th_manager = Thread_manager([main_th])
        th_manager.run()
        pass
    else:
        print('\nStack machine\nValue table:')
        sm.stack_machine_run()
