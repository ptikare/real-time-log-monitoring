import time

def monitor(file_path):
    print("Starting real-time monitoring...")

    with open(file_path, "r") as file:
        file.seek(0, 2)

        while True:
            line = file.readline()

            if not line:
                time.sleep(0.5)
                continue

            if "ERROR" in line:
                print(f"ERROR detected: {line.strip()}")


if __name__ == "__main__":
    monitor("app.log")
