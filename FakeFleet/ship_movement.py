import time
import random
import json
from ais_ship import generate_ship_data

def update_position(ship):
    ship["lat"] += round(random.uniform(-0.01, 0.01), 6)
    ship["lon"] += round(random.uniform(-0.01, 0.01), 6)
    ship["speed"] = round(random.uniform(5, 20), 2)
    ship["course"] = random.randint(0, 359)
    ship["last_position_epoch"] = int(time.time())
    ship["last_position_UTC"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    return ship

if __name__ == "__main__":
    ship = generate_ship_data()
    while True:
        ship = update_position(ship)
        print(json.dumps(ship, indent=4))
        time.sleep(5)
