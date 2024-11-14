# draw line horizontal on scree

def draw_line(screen, width, x1, x2, y):

    bytes_per_row = width // 8

    row_start = y * bytes_per_row

    start_byte = row_start + x1 // 8
    end_byte = row_start + x2 // 8

    if start_byte == end_byte:
        screen[start_byte] |= ((1 << (x2 - x1 + 1)) - 1) << (7 - (x2 % 8))
    else:
        screen[start_byte] |= (0xFF >> (x1 % 8))

        screen[end_byte] |= (0xFF << (7 - x2 % 8)) & 0xFF

        for i in range(start_byte + 1, end_byte):
            screen[i] = 0xFF

    return screen