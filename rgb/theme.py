from pathlib import Path
import yaml
from rgb.state import RGBState

class ThemeLoader:

    def __init__(self):

        self.cache = {}

    def load(self, filename):

        if filename in self.cache:
            return self.cache[filename]

        BASE_DIR = Path(__file__).resolve().parent.parent

        path = BASE_DIR / "themes" / f"{filename}.yaml"

        with open(path) as f:
            data = yaml.safe_load(f)

        state = RGBState(

            gpu=tuple(data["gpu"]["color"]),

            fans=tuple(data["fans"]["color"]),

            brightness=data["brightness"],

            theme=data["name"]

        )

        self.cache[filename] = state

        return state
