import sympy as sp
from sympy import symbols, factorial, sympify, E, pi, Function, expand
from sympy.core.function import AppliedUndef

def format_term(coeff, x, center, n):
    """Format a single term of the Taylor series in a readable way."""
    if coeff == 0:
        return ""
    
    # Format the coefficient
    if coeff == 1 and n > 0:
        coeff_str = ""
    elif coeff == -1 and n > 0:
        coeff_str = "-"
    else:
        coeff_str = str(coeff)
    
    # Format the (x - center) term
    if center == 0:
        var_str = "x"
    else:
        var_str = f"(x - {center})"
    
    # Format the power and factorial
    if n == 0:
        return coeff_str
    elif n == 1:
        return f"{coeff_str}{var_str}"
    else:
        return f"{coeff_str}{var_str}^{n}/{n}!"

def get_taylor_series(expr, var, center, order):
    """Calculate Taylor/Maclaurin series for the given expression."""
    x = symbols(var)
    terms = []
    
    for n in range(order + 1):
        # Calculate the nth derivative
        derivative = expr.diff(x, n)
        # Evaluate at the center point
        coeff = derivative.subs(x, center) / factorial(n)
        # Format and store the term
        term_str = format_term(coeff, x, center, n)
        if term_str:
            terms.append(term_str)
    
    # Join terms with proper signs
    result = terms[0]
    for term in terms[1:]:
        if term[0] != '-':
            result += " + " + term
        else:
            result += " " + term
    
    return result

def get_general_term(expr, var, center):
    """Generate the general term and sigma notation for the Taylor series."""
    x = symbols(var)
    # Calculate the general form of the nth derivative
    n = symbols('n')
    derivative = expr.diff(x, n)
    
    # Format the general term
    if center == 0:
        var_str = "x"
    else:
        var_str = f"(x - {center})"
    
    return f"∑(n=0 to ∞) [f^(n)({center})/{n}!]·{var_str}^n"

def main():
    print("Welcome to the Taylor/Maclaurin Series Calculator!")
    print("\nYou can use any mathematical function! Examples:")
    print("- Basic functions: x^2, sqrt(x), 1/x")
    print("- Trigonometric: sin(x), cos(x), tan(x), arcsin(x)")
    print("- Exponential/Logarithmic: exp(x), log(x), x^(1/3)")
    print("- Custom functions: f(x) (will be treated as an undefined function)")
    print("- Constants: e, pi, rational numbers like 1/2")
    print("- Combinations: sin(x^2), exp(sin(x)), etc.")
    
    while True:
        try:
            # Get the function from user
            func_str = input("\nEnter your function in terms of 'x' (or 'quit' to exit): ")
            if func_str.lower() == 'quit':
                break
                
            # Convert string to symbolic expression
            x = symbols('x')
            try:
                expr = sympify(func_str)
            except:
                # Handle undefined functions
                expr = Function(func_str.split('(')[0])(x)
            
            # Get expansion point
            center_str = input("Enter the center point (0 for Maclaurin series): ")
            # Handle the center point as a rational number
            if '/' in center_str:
                num, den = map(int, center_str.split('/'))
                center = sp.Rational(num, den)
            else:
                center = sp.Integer(center_str)
            
            # Get number of terms
            order = int(input("Enter the number of terms: "))
            
            # Calculate series
            series = get_taylor_series(expr, 'x', center, order)
            
            print("\nTaylor series expansion:")
            print("f(x) ≈")
            print(series)
            
            # Add general form in sigma notation
            print("\nInfinite series representation:")
            print("f(x) =", get_general_term(expr, 'x', center))
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please check your input and try again.")

if __name__ == "__main__":
    main()