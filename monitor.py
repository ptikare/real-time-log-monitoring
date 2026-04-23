import time

ERROR_THRESHOLD = 5
error_count = 0

def monitor(file_path):
    global error_count
    
    print("Monitoring with alert thresholds...")

    with open(file_path, "r") as file:
        file.seek(0, 2)

        while True:
            line = file.readline()

            if not line:
                time.sleep(0.5)
                continue

            if "ERROR" in line:
                error_count += 1

            if error_count >= ERROR_THRESHOLD:
                print(f"🚨 ALERT: High error count ({error_count})")
                error_count = 0


if __name__ == "__main__":
    monitor("app.log")
