"""Quadratic evaluation"""

def eval_quadratic(a_, b_, c_, x_):
    """quadratic"""
    result_ = a_ * (x_ * x_) + b_ * x_ + c_
    return result_

def main():
    """quadratic"""
    data = input()
    data = data.split(' ')
    data = list(map(int, data))
    print(data)
    for x in range(len(data)):
        temp = str(data[x]).split('.')
        # if temp[1] == '0':
        #     data[x] = int(float(str(data[x])))
        # else:
        #     data[x] = data[x]
    print(eval_quadratic(data[0], data[1], data[2], data[3]))

if __name__ == "__main__":
    main()
