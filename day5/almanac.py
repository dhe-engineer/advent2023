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

    def get_all_properties(self):
        properties = []
        properties.append(self.SEED)
        properties.append(self.SOIL)
        properties.append(self.FERTILIZER)
        properties.append(self.WATER)
        properties.append(self.LIGHT)
        properties.append(self.TEMPERATURE)
        properties.append(self.HUMIDITY)
        properties.append(self.LOCATION)
        return properties

    def get_property(self, name):
        match name:
            case "SEED":
                return self.SEED
            case "SOIL":
                return self.SOIL
            case "FERTILIZER":
                return self.FERTILIZER
            case "WATER":
                return self.WATER
            case "LIGHT":
                return self.LIGHT
            case "TEMPERATURE":
                return self.TEMPERATURE
            case "HUMIDITY":
                return self.HUMIDITY
            case "LOCATION":
                return self.LOCATION

    def set_property(self, value, name):
        match name:
            case "SEED":
                self.SEED = value
            case "SOIL":
                self.SOIL = value
            case "FERTILIZER":
                self.FERTILIZER = value
            case "WATER":
                self.WATER = value
            case "LIGHT":
                self.LIGHT = value
            case "TEMPERATURE":
                self.TEMPERATURE = value
            case "HUMIDITY":
                self.HUMIDITY = value
            case "LOCATION":
                self.LOCATION = value
