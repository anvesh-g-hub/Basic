import numpy as np
class NaturalNumbers:

    def __init__(self):
        print("constructor")

    def naturalNumbers(self,boundry):
        for x in range(boundry):
            print(x)

if __name__ == '__main__':
    naturalNumbers = NaturalNumbers()
    print('Printing Natural Numbers 1-100')
    print(np.array([1, 2, 3, 4, 5]))
    naturalNumbers.naturalNumbers(100)

