import time

from controller import RGBController
from colors import interpolate

rgb = RGBController()

day_gpu = (255,120,175)
night_gpu = (145,22,40)

day_fans = (255,190,225)
night_fans = (110,8,18)

duration = 10          # seconds for testing
fps = 60

frames = duration * fps

for i in range(frames + 1):

    t = i / frames

    gpu = interpolate(day_gpu, night_gpu, t)
    fans = interpolate(day_fans, night_fans, t)

    rgb.set_zone("JRAINBOW1", gpu)
    rgb.set_zone("JRAINBOW2", fans)

    time.sleep(1 / fps)
