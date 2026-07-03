from colors import interpolate

day = (255,120,175)
night = (145,22,40)

for i in range(11):

    t = i / 10

    print(interpolate(day, night, t))
