import socket
import json
import random
import time

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

reader = client.makefile("r")
writer = client.makefile("w")

print("Connected to server")
print("Sending traffic continuously. Press Ctrl+C to stop.")

try:
    for i in range(500):
        data = {
            "source_ip": "192.168.1." + str(random.randint(1, 10)),
            "destination_ip": "192.168.1." + str(random.randint(11, 20)),
            "protocol": random.choice(["TCP", "UDP"]),
            "packet_size": random.randint(100, 1500),
            "packets_per_second": random.randint(10, 100)
        }

        if random.random() < 0.2:
            data["packets_per_second"] = random.randint(200, 500)

        writer.write(json.dumps(data) + "\n")
        writer.flush()

        response = json.loads(reader.readline())
        print(data["source_ip"], "->", response)

        time.sleep(1)

except KeyboardInterrupt:
    print("\nTraffic transmission stopped.")

finally:
    reader.close()
    writer.close()
    client.close()