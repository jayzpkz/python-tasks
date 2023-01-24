def summer(num: int):
    """
        Sum the digits of num using recursion
        
        :param num: number of type int
        :return: the sum of the digits of the number
    """
    if not isinstance(num, int):
        raise ValueError("Input must be of type int")
    
    # Stop condition
    if num == 0:
        return 0
    # Take the last digit of the number and sum it with the result of the summer for the number without this digit
    return (num % 10) + summer(int(num / 10))

print(summer(2347623))

#  Optional implementation: if num is negative - raise error || return absolut digit sum
