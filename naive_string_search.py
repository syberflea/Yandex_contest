def sub_str_search(sub_string, string):
    n = len(string)
    m = len(sub_string)
    if m == 0:
        return True
    pos = -1
    for char in sub_string:
        pos = string.find(char, pos + 1)
        if pos < 0:
            return False
    return True



def main():
    sub_string = input()
    string = input()
    print(sub_str_search(sub_string, string))


if __name__ == "__main__":
    main()