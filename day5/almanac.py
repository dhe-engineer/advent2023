class seed_almanac ():
    SEED = 0
    SOIL = 0
    FERTILIZER = 0
    WATER = 0
    LIGHT = 0
    TEMPERATURE = 0
    HUMIDITY = 0
    LOCATION = 0

    def __init__(self, seed):
        self.SEED = seed

    def get_params(self):
        params = []
        params.append(self.SEED)
        params.append(self.SOIL)
        params.append(self.FERTILIZER)
        params.append(self.WATER)
        params.append(self.LIGHT)
        params.append(self.TEMPERATURE)
        params.append(self.HUMIDITY)
        params.append(self.LOCATION)
        return params
