a = input()

def convert_to_decimal(binary):
    decimal_val = 0
    
    for i in range(len(binary)):
        decimal_val += 2 ** i * int(binary[len(binary) - i - 1])        

    return decimal_val

has_zero = False
for i in range(1, len(a)):
    if a[i] == '0':
        has_zero = True
        list_a = list(a)
        list_a[i] = '1'
        print(convert_to_decimal(''.join(list_a)))
        break

if not has_zero:
    list_a = list(a)
    list_a[-1] = '0'
    print(convert_to_decimal(''.join(list_a)))