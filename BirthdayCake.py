#Solution to Birthday Cake Problem
#

def compute(ar):
    return sum([1 for i in ar if i == max(ar)])

def test():
    L = [[1,4,5,7,8,6,5,5,6,7],
         [1,1,1,1,1,1,1,1,1,1],
         [43,50,50,50,23,1,4,5,6,7,23,34,45,50,8]]
    #first answer is correct answer and second is the answer returned by function compute
    for i in L:
        print "List: ",i," Correct: ",i.count(max(i)),"Output: ",compute(i)
