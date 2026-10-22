import socket
import json

HOST = "127.0.0.1"
PORT = 5000

server = None

try:
    print("Network Traffic Server", flush=True)
    print("Setting up server...", flush=True)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print("Binding to port", PORT, flush=True)
    server.bind((HOST, PORT))

    server.listen()
    print("Server is running on port", PORT, flush=True)
    print("Waiting for client...", flush=True)

    while True:
        conn, addr = server.accept()
        print("Client connected:", addr, flush=True)

        with conn:
            reader = conn.makefile("r")
            writer = conn.makefile("w")

            try:
                for line in reader:
                    try:
                        data = json.loads(line)

                        if data["packets_per_second"] > 150:
                            data["status"] = "Anomaly"
                            print("Anomaly detected:", data["source_ip"], flush=True)
                        else:
                            data["status"] = "Normal"

                        with open("traffic_log.jsonl", "a") as file:
                            file.write(json.dumps(data) + "\n")

                        response = {
                            "message": "Traffic received",
                            "status": data["status"]
                        }

                    except (ValueError, KeyError, TypeError):
                        response = {
                            "message": "Invalid traffic record"
                        }

                    writer.write(json.dumps(response) + "\n")
                    writer.flush()

            finally:
                reader.close()
                writer.close()

        print("Client disconnected", flush=True)

except OSError as e:
    print("Server error:", e, flush=True)

finally:
    if server is not None:
        server.close()