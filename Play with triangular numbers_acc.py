def triangular_numbers(n):
    if not isinstance(n, int) or n <= 0:
        return "NoProceed"
    
    result = []
    for i in range(1, n + 1):
        triangular_number = i * (i + 1) // 2
        result.append(triangular_number)
    
    return ', '.join(map(str, result))

try:
    user_input = input()
    n = float(user_input)
    if n.is_integer():
        n = int(n)
        output = triangular_numbers(n)
    else:
        output = "NoProceed"
except ValueError:
    output = "NoProceed"

print(output)