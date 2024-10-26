import time
from collections import defaultdict
import logging
import random

# Configure logging
logging.basicConfig(filename='firewall.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

class Firewall:
    def __init__(self, request_limit=100, time_window=60, block_duration=300):
        self.request_limit = request_limit
        self.time_window = time_window
        self.block_duration = block_duration
        self.ip_requests = defaultdict(list)
        self.blocked_ips = {}

    def check_request(self, ip_address):
        current_time = time.time()
        
        # Check if IP is blocked
        if ip_address in self.blocked_ips:
            if current_time - self.blocked_ips[ip_address] < self.block_duration:
                logging.info(f"Blocked request from {ip_address} (IP is blocked)")
                return False
            else:
                del self.blocked_ips[ip_address]

        # Remove old requests
        self.ip_requests[ip_address] = [t for t in self.ip_requests[ip_address] if current_time - t < self.time_window]
        
        # Add new request
        self.ip_requests[ip_address].append(current_time)
        
        # Check if request limit is exceeded
        if len(self.ip_requests[ip_address]) > self.request_limit:
            self.blocked_ips[ip_address] = current_time
            logging.warning(f"DoS attack detected from {ip_address}. IP blocked for {self.block_duration} seconds.")
            return False
        
        return True

def simulate_math_bc_server(firewall):
    def handle_request(ip_address):
        if firewall.check_request(ip_address):
            print(f"Request from {ip_address} allowed - Processing math operation")
            # Simulate processing a math operation
            result = random.randint(1, 100)
            print(f"Math result for {ip_address}: {result}")
        else:
            print(f"Request from {ip_address} blocked - Potential DoS attack")

    # List of IP addresses to simulate traffic from
    ip_addresses = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4"]

    print("Starting Math Bc Server simulation with DoS protection...")
    print(f"Firewall settings: limit {firewall.request_limit} requests per {firewall.time_window} seconds, block duration {firewall.block_duration} seconds")
    
    # Simulate traffic for 2 minutes
    end_time = time.time() + 120
    while time.time() < end_time:
        # Randomly select an IP address
        ip = random.choice(ip_addresses)
        
        # Simulate a request
        handle_request(ip)
        
        # Wait for a short random interval before the next request
        time.sleep(random.uniform(0.1, 0.5))

    print("\nSimulation complete. Check firewall.log for detailed logs.")

if __name__ == "__main__":
    # Initialize the firewall
    firewall = Firewall(request_limit=50, time_window=10, block_duration=30)

    # Run the simulation
    simulate_math_bc_server(firewall)

