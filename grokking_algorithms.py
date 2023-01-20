# Suppose you’re a farmer with a plot of land. You want to divide this farm evenly into square plots. You want the plots
# to be as big as possible. So none of these will work. How do you figure out the largest square size you can use for a plot of land?

def find_biggest_square(width, height):
    if width % height == 0:
        return height
    return find_biggest_square(height, width % height)


print(find_biggest_square(1680, 640))  # 80
print(find_biggest_square(64, 168))  # 8   64 % 168 = 64 => find_biggest_square(168, 64) => It will swap the width and height
print(find_biggest_square(50, 25))  # 25



