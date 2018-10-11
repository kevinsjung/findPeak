def findPeak(numbers):

    '''
    Background: This was an interview question to find an optimal implementation of finding the maximum of a reliably increasing
    then decreasing series of numbers
    There could also be a section that is flat where adjacent values are the same.

    :param a 1D array of numbers:
    :return: peak value and index
    '''


    def recurse(numbers, c, offset):
        listlen = len(numbers)

        if listlen == 1:
            return 0+offset
        elif listlen == 2:
            if numbers[0] > numbers[1]:
                return 0+offset
            elif numbers[1] > numbers[0]:
                return 1+offset

        midval = numbers[listlen/2]
        leftval = numbers[listlen/2 - c]
        rightval = numbers[listlen/2 + c]

        if leftval < midval and rightval < midval: #at peak
            return listlen/2
        elif leftval > midval:
            return recurse(numbers[0:listlen/2+1-c], 1, offset+0)
        elif rightval > midval:
            return recurse(numbers[listlen/2+c::], 1, offset+listlen/2+1)
        elif leftval == rightval: # at a flat part
            return recurse(numbers, 2)

    listlen = len(numbers)

    if listlen % 2 == 0:
        numbers.append(numbers[-1]-1)
    return recurse(numbers, 1, 0)

print findPeak([-1,2,1,1])
print findPeak([-1,1,2,1])
print findPeak([-1,2,1,1])
print findPeak([-1,1,3,7,-1])
print findPeak([-1,1,3,7,8,-1])