'''
Вместо формы ** и метода pop словарей используются аргументы, которые могут
передаваться только по именам, появившиеся в версии 3.0.
В версии 3.0 нет необходимости выносить вызов range() за пределы цикла, так как эта
функция возвращает генератор, а не список
'''

import time, sys, math

trace = lambda *args: None # or print

timefunc = time.clock if sys.platform == 'win32' else time.time

def timer(func, *pargs, _reps=10000, **kargs):
    trace(func, pargs, kargs, _reps)
    start = timefunc()
    for i in range(_reps):
        ret = func(*pargs, **kargs)
    elapsed = timefunc() - start
    return (elapsed, ret)


def best(func, *pargs, _reps=50, **kargs):
    best = 2 ** 32
    for i in range(_reps):
        (time, ret) = timer(func, *pargs, _reps=1, **kargs)
        if time < best: best = time
        return (best, ret)


mSqrt = math.sqrt
doubleStar = lambda x: x ** 0.5
powFunc = lambda x: pow(x, 0.5)

t = timer
b = best

print(sys.version)
for tester in ( t, b ):
    print('\n')
    print('<%s>' % tester.__name__)
    for fn in ( mSqrt, doubleStar, powFunc ):
        elapsed, result = tester(fn, 2, _reps=10000)
        print('function %-9s: elapsed %.9f => [%s]' % ( fn.__name__, elapsed, result))

seq = list(range(1000))
dictGen = lambda x: { i: i for i in x }
def dictGen2(x):
    d = {}
    for i in x:
        d[i] = i
    return d

print('---dict construction---')
for tester in ( t, b ):
    print('\n')
    print('<%s>' % tester.__name__)
    for fn in ( dictGen, dictGen2):
        elapsed, result = tester(fn, seq, _reps=10000)
        print('function %-9s: elapsed %.9f => [%s ... %s]' % ( fn.__name__, elapsed, result[list(result.keys())[0]], result[list(result.keys())[-1]]))

#print(timer(math.sqrt, 2))
#print(timer(lambda x,y: x ** y, 2, 0.5))
#print(timer(pow, 2, 0.5))
#print(best(math.sqrt, 2))
#print(best(lambda x,y: x ** y, 2, 0.5))
#print(best(pow, 2, 0.5))
