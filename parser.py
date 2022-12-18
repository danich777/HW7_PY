def parser(string):
    exp_list = string.split()
    print(exp_list)
    for i in range(len(exp_list)):
            if exp_list[i].isdigit():
                exp_list[i] = int(exp_list[i])
    result = 0
    while len(exp_list) != 1:
        i = 0
        while ('*' in exp_list or '/' in exp_list) and i < len(exp_list):
            if exp_list[i] == '*':
                result = exp_list[i - 1] * exp_list[i + 1]
                exp_list.pop(i)
                exp_list.pop(i)
                exp_list[i - 1] = result
            elif exp_list[i] == '/':
                result = exp_list[i - 1] / exp_list[i + 1]
                exp_list.pop(i)
                exp_list.pop(i)
                exp_list[i - 1] = result
            else:
                i += 1

        while ('+' in exp_list or '-' in exp_list) and i < len(exp_list):
            if exp_list[i] == '+':
                result = exp_list[i - 1] + exp_list[i + 1]
                exp_list.pop(i)
                exp_list.pop(i)
                exp_list[i - 1] = result
                i -= 1
            elif exp_list[i] == '-':
                result = exp_list[i - 1] - exp_list[i + 1]
                exp_list.pop(i)
                exp_list.pop(i)
                exp_list[i - 1] = result
                i -= 1
            else:
                i += 1
    print(f'Результат: {result}')
