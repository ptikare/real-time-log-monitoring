import time
from prometheus_client import start_http_server, Counter

ERROR_THRESHOLD = 5
alert_triggered = False
error_count = 0

# Prometheus metrics
error_counter = Counter('error_count', 'Total number of error logs')
log_counter = Counter('log_count', 'Total number of logs processed')

def monitor(file_path):
    global error_count, alert_triggered
    
    print("Monitoring with alert thresholds...")

    # Start Prometheus metrics server
    start_http_server(8000, addr="0.0.0.0")

    with open(file_path, "r") as file:
        file.seek(0, 2)

        while True:
            line = file.readline()

            if not line:
                time.sleep(0.5)
                continue

            log_counter.inc()

            if "ERROR" in line:
                error_count += 1
                error_counter.inc()

            if error_count >= ERROR_THRESHOLD and not alert_triggered:
                print(f"🚨 ALERT: High error count ({error_count})")
                alert_triggered = True

            if error_count < ERROR_THRESHOLD:
                alert_triggered = False


if __name__ == "__main__":
    monitor("app.log")
