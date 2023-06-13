with open("input.txt") as inp:
    num_a, num_b = inp.readline().split()
    sum_num = int(num_a) + int(num_b)
with open("output.txt", mode='w') as out:
    out.write(str(sum_num))
