from openrgb import OpenRGBClient
from openrgb.utils import RGBColor

class RGBController:

    def __init__(self):

        self.client = OpenRGBClient()

        self.device = self.client.devices[0]

        self.zone_lookup = {
            zone.name: zone
            for zone in self.device.zones
        }

        self.last_colors = {}

    def set_zone(self, zone_name, rgb):

        if self.last_colors.get(zone_name) == rgb:
            return

        self.last_colors[zone_name] = rgb

        zone = self.zone_lookup[zone_name]

        zone.set_color(RGBColor(*rgb))
