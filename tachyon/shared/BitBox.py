def CalcZeros(number):
    b = bin(number)
    zeros = 0
    for bit in reversed(b):
        if bit != "0":
            break
        zeros += 1

    return zeros
