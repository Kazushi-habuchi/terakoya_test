def is_anagram(arg1, arg2):
    if type(arg1) != str or type(arg2) != str:
        raise ValueError

    arg1 = list(arg1)
    arg2 = list(arg2)

    arg1.sort()
    arg2.sort()

    arg1 = ''.join(arg1)
    arg2 = ''.join(arg2)
    count = 0

    if (len(arg1) != len(arg2)):
        return (False)
    else:
        for i in range(0, len(arg1)):
            for j in range(0, len(arg2)):
                if (arg1[i] == arg2[j]):
                    count += 1
        if (count == len(arg1)):
            return (True)
        else:
            return (False)