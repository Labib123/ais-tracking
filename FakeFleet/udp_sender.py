import socket
import json
import time
from ais_ship import AISShip  # Import the AISShip class

# UDP Configuration
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create multiple ships (e.g., 3 ships)
ships = [AISShip() for _ in range(3)]

if __name__ == "__main__":
    while True:
        for ship in ships:
            ship.update_position()  # Move the ship
            ais_data = ship.get_ais_data()  # Get updated AIS data
            message = json.dumps(ais_data).encode()

            sock.sendto(message, (UDP_IP, UDP_PORT))
            print(f"Sent AIS data: {message}")

            # Determine sleep time based on vessel movement
            if ship.is_moving():
                time.sleep(2)  # Fast update for moving ships (every 2 sec)
            else:
                time.sleep(180)  # Slow update for stationary ships (every 3 min)
