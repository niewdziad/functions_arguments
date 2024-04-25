def gen_mul_table(width=10, height=10, *, sep_width=3, print_header=False, print_footer=True):
    if print_header:
        header = f"Multiplication Table {width} x {height}\n"
    else:
        header = ""

    table = header

    for i in range(1, height + 1):
        row = ""
        for j in range(1, width + 1):
            product = i * j
            row += f"{product:>{sep_width}}"
        table += row.strip() + "\n"

    if print_footer:
        footer = "-" * (width * (sep_width + 1))
        table += footer

    return table

# Testowanie funkcji
print(gen_mul_table(width=5, height=5, sep_width=3, print_footer=False))
