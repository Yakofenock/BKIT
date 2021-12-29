data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    # result = ...
    # print(result)
    print(sorted(data, key=abs, reverse=True))

    # result_with_lambda = ...
    # print(result_with_lambda)
    print(sorted(data, key=lambda x: abs(x), reverse=True))