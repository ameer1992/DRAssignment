import random
def random_number():
    return random.randint(0, 100000000)

def solve_formula(formula, n=100):
    compiled_formula = compile(formula, '', 'eval')
    
    for _i in range(n):
        
        A, B, C = random_number(), random_number(), random_number()
        
        evaluted_formula = eval(compiled_formula)
        
        effctive_formula = formula.replace('A', str(A)).replace('B', str(B)).replace('C', str(C))

        print (effctive_formula, '=' , evaluted_formula)

    return 

solve_formula("2*A+B")
