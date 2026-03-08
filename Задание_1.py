class Glass:
    def __init__(self, capacity_volume: int, occupied_volume: int):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass = Glass(200, 0)
    print(dir(glass))
    glass.__class__
    print(glass.__class__)
    glass.__dict__
    print( glass.__dict__)