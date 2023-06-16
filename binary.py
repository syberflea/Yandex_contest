def to_binary(number: int) -> str:
    bin_str = ''

    while number:
        bin_str = str(number % 2) + bin_str
        number //= 2
    return bin_str or '0'

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))