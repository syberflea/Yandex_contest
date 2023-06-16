def is_palindrome(line: str) -> bool:
    table = line.maketrans(",.:", "   ")
    line = line.translate(table)
    clean_str = ''.join(line.split(' ')).casefold()
    rev_clean_str = reversed(clean_str)
    return list(clean_str) == list(rev_clean_str)


print(is_palindrome(input().strip()))