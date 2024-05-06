from parameters import MONITOR_RESOLUTION, USE_PRIZE_COUPON, USE_PRODUCTION_COUPON, LOWER_REACTION_TIME, \
    UPPER_REACTION_TIME


class Configuration:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Configuration, cls).__new__(cls, *args, **kwargs)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        # Initialize configuration with default values
        self.settings = {
            MONITOR_RESOLUTION: "1920:1080",
            USE_PRIZE_COUPON: True,
            USE_PRODUCTION_COUPON: False,
            LOWER_REACTION_TIME: 1,
            UPPER_REACTION_TIME: 5
        }

    def get_setting(self, key):
        return self.settings.get(key)

    def set_setting(self, key, value):
        self.settings[key] = value

    def generate_configuration_string(self):
        return "\n".join([f"{key}: {value}" for key, value in self.settings.items()])
