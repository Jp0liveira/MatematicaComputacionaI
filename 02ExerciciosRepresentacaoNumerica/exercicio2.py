def machine_precision(ref_value=1):
    A = 1.0
    s = 2.0
    while s > 1.0:
        A = A / 2.0
        s = 1.0 + A
    prec = 2.0 * A / ref_value
    return prec

print(machine_precision())
print(machine_precision(10))

references = [10, 17, 100, 184, 1000, 1575, 10000, 17893]
for ref in references:
    precision = machine_precision(ref)
    print(f"Para a referência {ref}, a precisão da máquina é {precision}")