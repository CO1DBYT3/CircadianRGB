import time
from rgb.state import RGBState
from rgb.colors import interpolate


class Animator:

    def __init__(self):

        self.running = False

        self.duration = 1.0

        self.start_time = None

        self.start_state = None

        self.target_state = None


    def start(self, start_state: RGBState,
                    target_state: RGBState,
                    duration: float):

        self.start_time = time.perf_counter()

        self.start_state = start_state

        self.target_state = target_state

        self.duration = duration

        self.running = True

    def update(self):

        if not self.running:
            return self.target_state

        elapsed = time.perf_counter() - self.start_time

        t = min(elapsed / self.duration, 1.0)

        gpu = interpolate(
            self.start_state.gpu,
            self.target_state.gpu,
            t
        )

        fans = interpolate(
            self.start_state.fans,
            self.target_state.fans,
            t
        )

        brightness = round(

            self.start_state.brightness +

            (self.target_state.brightness -
            self.start_state.brightness) * t

        )

        state = RGBState(

            gpu=gpu,

            fans=fans,

            brightness=brightness,

            theme=self.target_state.theme

        )

    if t >= 1.0:

        self.running = False

        return self.target_state

    return state
