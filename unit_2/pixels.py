class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._green + self._blue) // 3
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        info = "X: {}, Y: {}, Color: {}".format(self._x, self._y, (self._red, self._green, self._blue))
        info += " Red" if self._red > 50 and self._green == 0 and self._blue == 0 else ""
        info += " Green" if self._red == 0 and self._green > 50 and self._blue == 0 else ""
        info += " Blue" if self._red == 0 and self._green == 0 and self._blue > 50 else ""
        print(info)


def main():
    pixel = Pixel(5, 6, 250)
    pixel.print_pixel_info()
    pixel.set_grayscale()
    pixel.print_pixel_info()


main()
