def sequencer(maxValue = 0, counter = 0):  
    """
        Prints the maximum value of sequence of inputs from the user
        and the number of times this value appeared in the sequence
        
        :param maxValue: maximum value in the sequence (integer)
        :param counter: number of times maximum value appeared in the sequence
        :return: None
    """
    
    # Get input from user
    num = input("Please enter your number: ")
    
    try:
        # Try casting int on the string we got from user input
        num = int(num)
    except ValueError:
        print("Input must be of type int! \t")
        return
    
    # counter the number of times max value appears in the sequence
    if num == maxValue:
        counter += 1
    
    # if the currect number is greater than the max value, it becomes the new max value and reset the counter to 1
    if num > maxValue:
        maxValue = num
        counter = 1
    
    # Stop condition
    if num == 0:
        print("({0}; {1})".format(maxValue, counter))
        return
    
    sequencer(maxValue, counter)
  
sequencer()