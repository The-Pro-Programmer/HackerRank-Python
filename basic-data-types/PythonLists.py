if __name__ == '__main__':
    N = int(input())
    numbers = list()
    for i in range(N):

        inputs = input().split()
        operation = inputs[0]

        if operation == 'insert':
            index = int(inputs[1])
            num = int(inputs[2])
            numbers.insert(index, num)

        elif operation == 'print':
            print(numbers)

        elif operation == 'remove':
            num = int(inputs[1])
            numbers.remove(num)

        elif operation == 'append':
            num = int(inputs[1])
            numbers.append(num)

        elif operation == 'sort':
            numbers.sort() 

        elif operation == 'pop':
            del numbers[-1]

        elif operation == 'reverse':
            numbers.reverse()

