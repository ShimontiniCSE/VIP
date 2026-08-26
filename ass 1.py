import colorsys
import math

def rgb_to_hsv(r, g, b):
    return colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

def hsv_to_rgb(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return round(r * 255), round(g * 255), round(b * 255)

def rgb_to_hsl(r, g, b):
    return colorsys.rgb_to_hls(r / 255, g / 255, b / 255)

def hsl_to_rgb(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return round(r * 255), round(g * 255), round(b * 255)

def rgb_to_cmyk(r, g, b):
    r, g, b = r / 255, g / 255, b / 255
    k = 1 - max(r, g, b)
    if k == 1:
        return 0, 0, 0, 100
    c = (1 - r - k) / (1 - k)
    m = (1 - g - k) / (1 - k)
    y = (1 - b - k) / (1 - k)
    return round(c * 100, 2), round(m * 100, 2), round(y * 100, 2), round(k * 100, 2)

def cmyk_to_rgb(c, m, y, k):
    c, m, y, k = c / 100, m / 100, y / 100, k / 100
    r = 255 * (1 - c) * (1 - k)
    g = 255 * (1 - m) * (1 - k)
    b = 255 * (1 - y) * (1 - k)
    return round(r), round(g), round(b)

def rgb_to_ycbcr(r, g, b):
    y = 0.299 * r + 0.587 * g + 0.114 * b
    cb = 128 - 0.168736 * r - 0.331264 * g + 0.5 * b
    cr = 128 + 0.5 * r - 0.418688 * g - 0.081312 * b
    return round(y, 2), round(cb, 2), round(cr, 2)

def ycbcr_to_rgb(y, cb, cr):
    r = y + 1.402 * (cr - 128)
    g = y - 0.344136 * (cb - 128) - 0.714136 * (cr - 128)
    b = y + 1.772 * (cb - 128)
    return tuple(round(max(0, min(255, x))) for x in (r, g, b))

def rgb_to_xyz(r, g, b):
    r, g, b = r / 255, g / 255, b / 255

    r = ((r + 0.055) / 1.055) ** 2.4 if r > 0.04045 else r / 12.92
    g = ((g + 0.055) / 1.055) ** 2.4 if g > 0.04045 else g / 12.92
    b = ((b + 0.055) / 1.055) ** 2.4 if b > 0.04045 else b / 12.92

    x = (r * 0.4124564 + g * 0.3575761 + b * 0.1804375) * 100
    y = (r * 0.2126729 + g * 0.7151522 + b * 0.0721750) * 100
    z = (r * 0.0193339 + g * 0.1191920 + b * 0.9503041) * 100

    return round(x, 2), round(y, 2), round(z, 2)

def xyz_to_rgb(x, y, z):
    x, y, z = x / 100, y / 100, z / 100

    r = x * 3.2404542 + y * -1.5371385 + z * -0.4985314
    g = x * -0.9692660 + y * 1.8760108 + z * 0.0415560
    b = x * 0.0556434 + y * -0.2040259 + z * 1.0572252

    r = 1.055 * (max(0, min(1, r)) ** (1 / 2.4)) - 0.055 if r > 0.0031308 else 12.92 * r
    g = 1.055 * (max(0, min(1, g)) ** (1 / 2.4)) - 0.055 if g > 0.0031308 else 12.92 * g
    b = 1.055 * (max(0, min(1, b)) ** (1 / 2.4)) - 0.055 if b > 0.0031308 else 12.92 * b

    return round(r * 255), round(g * 255), round(b * 255)

def main():
    r, g, b = map(int, input("Enter RGB values: ").split())

    print("RGB:", r, g, b)

    h, s, v = rgb_to_hsv(r, g, b)
    print("HSV:", round(h * 360, 2), round(s * 100, 2), round(v * 100, 2))

    h, l, s = rgb_to_hsl(r, g, b)
    print("HSL:", round(h * 360, 2), round(s * 100, 2), round(l * 100, 2))

    print("CMYK:", rgb_to_cmyk(r, g, b))
    print("YCbCr:", rgb_to_ycbcr(r, g, b))
    print("XYZ:", rgb_to_xyz(r, g, b))

if __name__ == "__main__":
    main()
