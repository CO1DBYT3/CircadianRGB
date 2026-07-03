import yaml

class Config:

    def __init__(self, filename="config.yaml"):

        with open(filename, "r") as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, key):
        return self.data[key]
