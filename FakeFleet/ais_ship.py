import random
import datetime


class AISShip:
    """Simulates a moving ship for an AIS system with realistic attributes and movement."""

    def __init__(self):
        self.vessel_types = {
            "Cargo": {"size_range": (50, 400), "speed_range": (10, 25),
                      "cargo_types": ["Containers", "Bulk Goods", "Vehicles"]},
            "Fishing": {"size_range": (10, 50), "speed_range": (5, 15), "cargo_types": ["Fish"]},
            "Military": {"size_range": (50, 300), "speed_range": (25, 40),
                         "cargo_types": ["Classified", "Weapons", "Troops"]},
            "Passenger": {"size_range": (50, 350), "speed_range": (15, 30), "cargo_types": ["People"]},
            "Pleasure Craft": {"size_range": (5, 30), "speed_range": (10, 30), "cargo_types": ["Personal Use"]},
            "Tanker": {"size_range": (100, 400), "speed_range": (8, 20),
                       "cargo_types": ["Crude Oil", "LNG", "Chemicals"]},
            "Tug/Tow": {"size_range": (20, 80), "speed_range": (10, 18), "cargo_types": ["Towing"]},
            "Other": {"size_range": (20, 300), "speed_range": (5, 25),
                      "cargo_types": ["Research Equipment", "Special Ops"]},
        }

        self.countries = {
            "USA": "366",
            "UK": "235",
            "Japan": "431",
            "Germany": "211",
            "France": "227",
            "China": "412",
            "Norway": "257",
            "Panama": "352",
            "Singapore": "563",
            "Liberia": "636",
            "Bahamas": "311",
            "Greece": "237",
        }

        self.ship_names = [
            "Ocean Voyager", "Sea Pearl", "Poseidon's Call", "Neptune Spirit", "Atlantic Titan",
            "Pacific Breeze", "Arctic Explorer", "Starlight Mariner", "Blue Horizon", "Thunder Wave"
        ]

        self.assign_ship_attributes()

    def assign_ship_attributes(self):
        """Assigns initial attributes to the ship instance."""
        self.vessel_type = random.choice(list(self.vessel_types.keys()))
        details = self.vessel_types[self.vessel_type]

        self.name = random.choice(self.ship_names)
        self.imo_number = f"IMO {random.randint(1000000, 9999999)}"
        self.country, self.country_code = random.choice(list(self.countries.items()))
        self.mmsi = f"{self.country_code}{random.randint(1000000, 9999999)}"
        self.call_sign = self.generate_call_sign()
        self.size = random.randint(*details["size_range"])
        self.speed = random.randint(*details["speed_range"])
        self.cargo_type = random.choice(details["cargo_types"])
        self.latitude, self.longitude = self.generate_position()
        self.heading = random.randint(0, 359)  # Random initial heading (0-359 degrees)

    def generate_call_sign(self):
        """Generates a realistic maritime call sign."""
        prefix = random.choice(["3F", "5R", "9H", "D5", "EK", "V7", "XU"])
        suffix = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=4))
        return f"{prefix}{suffix}"

    def generate_position(self):
        """Generates a random initial AIS position (latitude, longitude)."""
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        return latitude, longitude

    def update_position(self):
        """Simulates ship movement by updating latitude and longitude based on heading & speed."""
        # Convert speed from knots to degrees of movement
        movement_factor = self.speed * 0.01  # Arbitrary movement conversion

        # Basic lat/lon movement simulation (ignoring real-world complexities like currents)
        self.latitude += round(movement_factor * random.uniform(-0.5, 0.5), 6)
        self.longitude += round(movement_factor * random.uniform(-0.5, 0.5), 6)

        # Keep within valid coordinate ranges
        self.latitude = max(-90, min(90, self.latitude))
        self.longitude = max(-180, min(180, self.longitude))

    def get_ais_data(self):
        """Returns a dictionary representing the current AIS data of the ship."""
        return {
            "Name": self.name,
            "Vessel Type": self.vessel_type,
            "IMO Number": self.imo_number,
            "MMSI": self.mmsi,
            "Call Sign": self.call_sign,
            "Flag": self.country,
            "Size (meters)": self.size,
            "Speed (knots)": self.speed,
            "Cargo Type": self.cargo_type,
            "Latitude": self.latitude,
            "Longitude": self.longitude,
            "Heading": self.heading,
            "Date_Time_UTC": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        }


# Example Usage
ships = [AISShip() for _ in range(3)]  # Create 3 moving ships

# Simulate movement updates
for ship in ships:
    ship.update_position()  # Move each ship
