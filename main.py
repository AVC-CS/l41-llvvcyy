def main():

    N = int(input('Enter the number N: '))
    result = []

    result.extend(2 ** i for i in range(N + 1))
    print(" ".join(map(str, result)))

    return result


if __name__ == '__main__':
    main()
