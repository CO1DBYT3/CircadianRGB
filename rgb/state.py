from dataclasses import dataclass

@dataclass
class RGBState:

    gpu: tuple[int, int, int]

    fans: tuple[int, int, int]

    brightness: int

    theme: str
