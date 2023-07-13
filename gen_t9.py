KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def generator(*sentence):
    result = []
    if not sentence:
        return [[]]
    else:
        for elem in sentence[0]:
            for each in generator(*sentence[1:]):
                result.append([elem] + each)
        return result


def main():
    keys = input().strip()
    sentence = [KEYBOARD[key] for key in keys]
    print(" ".join("".join(each) for each in generator(*sentence)))


if __name__ == "__main__":
    main()
