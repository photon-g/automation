
import sys

#todo allows to pass x args
def execute_predicat(_handler,_arg):
    if not _handler(_arg):
        sys.exit(1)

#todo allows to pass x args
def execute_predicat_with_cond(_cond,_handler,_arg):
    if _cond:
        _handler(_arg)
        sys.exit(1)
