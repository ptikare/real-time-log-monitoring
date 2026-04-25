import time

ERROR_THRESHOLD = 5
alert_triggered = False
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

            if error_count >= ERROR_THRESHOLD and not alert_triggered:
                print(f"🚨 ALERT: High error count ({error_count})")
                alert_triggered = True

            if error_count < ERROR_THRESHOLD:
                alert_triggered = False


if __name__ == "__main__":
    monitor("app.log")
