from math import sqrt as sqrt
def Standard_Deviation(input):
    mean = sum(input)/len(input)
    difference = []
    for i in input:
        d = (i - mean)**2
        difference.append(d)
    sum_difference = sum(difference)
    variance = sum_difference/len(input)
    st_deviation = sqrt(variance)
    print st_deviation

Standard_Deviation([5, 6, 11, 13, 19, 20, 25, 26, 28, 37])
