import random
def random_number():
    return random.randint(0, 100000000)

def solve_formula(formula, n=100):
    
    effctive_formula = formula.replace('A', str(random_number())).replace('B', str(random_number())).replace('C', str(random_number()))

    print (effctive_formula, '=' , eval(effctive_formula))

    if n==1:
        return 
    
    return solve_formula(formula, n-1)
    

solve_formula("2*A+B")
