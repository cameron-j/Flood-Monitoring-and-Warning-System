class MonitoringStation:
    def __init__(self, stationID: str, measurementID: str, name: str, loc: tuple[float, float],
                 typical: tuple[float, float], river: str, town: str):
        self.stationID = stationID
        self.measurementID = measurementID
        self.name = name
        self.loc = loc
        self.typical = typical
        self.river = river
        self.town = town
    
    def __repr__(self):
        print(f"""
        Station name:   {self.name}
            id:             {self.stationID}
            measure id:     {self.measurementID}
            coordinate:     {self.loc}
            town:           {self.town}
            river:          {self.river}
            typical range:  {self.typical}
        """)


def build_station_list(use_cache=True):
    pass