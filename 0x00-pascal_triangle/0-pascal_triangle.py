"""" pascal triangle function """


def pascal_triangle(n):
    """ check if n is less than
    zero return empty list
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        # Start each row with 1
        row = [1] * (i + 1)
        
        # Calculate the values for the row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        triangle.append(row)
    
    return triangle
