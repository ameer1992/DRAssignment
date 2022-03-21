def reverse_docorator(func):
    def wrapper(* args, **kwargs):
        reversed_args = args[::-1]
        return func(*reversed_args, **kwargs)
    return wrapper

@reverse_docorator
def sub(a,b):
    return a -b 

print (sub(1, 2))

print (sub(a=1, b=2))

print (sub(1, b=2))

