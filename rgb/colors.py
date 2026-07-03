import colorsys

def ease(t):
    """Smooth ease-in/ease-out"""
    return t * t * (3 - 2 * t)


def rgb_to_hsv(rgb):
    r, g, b = [x / 255 for x in rgb]
    return colorsys.rgb_to_hsv(r, g, b)


def hsv_to_rgb(hsv):
    r, g, b = colorsys.hsv_to_rgb(*hsv)
    return (
        int(r * 255),
        int(g * 255),
        int(b * 255),
    )


def lerp(a, b, t):
    return a + (b - a) * t


def interpolate(start_rgb, end_rgb, t):
    t = ease(t)

    h1, s1, v1 = rgb_to_hsv(start_rgb)
    h2, s2, v2 = rgb_to_hsv(end_rgb)

    # shortest hue path
    dh = h2 - h1
    if abs(dh) > 0.5:
        if dh > 0:
            h1 += 1
        else:
            h2 += 1

    h = (lerp(h1, h2, t)) % 1
    s = lerp(s1, s2, t)
    v = lerp(v1, v2, t)

    return hsv_to_rgb((h, s, v))
