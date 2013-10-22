# Based on
# http://norvig.com/lispy.html
# http://norvig.com/lispy2.html
#
# http://julien.danjou.info/blog/2013/lisp-python-hy
#
# if (x.val() > 0) {
#   z = f(a * x.val() + b[i]);
# }
#
# (if (> (val x) 0)
#   (let z
#       (f (+ (* a (val x))
#             (aref b i)))))
#
#
# (if (> (val x) 0)
#   (let z
#       (f (+ (* a (val x))
#             (__getitem__ b i)))))
#

global_env = None

# Typedefs
Symbol = str
isa = isinstance

def eval(x, env=global_env):
    """ Evaluate an expression in an environment """
    if isa(x, Symbol):
        return env.find(x)[x]
    elif not isa(x, list):
        return x
    elif x[0] == 'quote':
        (_, exp) = x
        return exp
    elif x[0] == 'if':
        (_, test, conseq, alt) = x
        return eval((conseq if eval(test, env) else alt), env)

def add_globals(env):
    """ Add some LISP standard procedures to an environment """
    import math, operator as op
    env.update(vars(math))

    env.update({
        # Arity 2 operators
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '/': op.div,
        '>': op.gt,
        '<': op.lt,
        '>=': op.ge,
        '<=': op.le,
        '=': op.eq,
        'equal?': op.eq,
        'eq?': op.is_,
        'cons': lambda x, y: [x] + y,
        'car': lambda x: x[0],
        'cdr': lambda x: x[1:],
        'append': op.add,
        'list': lambda *x: list(x),
        ',list?': lambda x: isa(x, list),
        'null?': lambda x: x == [],
        'symbol?': lambda x: isa(x, Symbol),
        # Arity 1 operators
        'not': op.not_,
        'length': len,
        })

    return env
