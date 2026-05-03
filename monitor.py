import time
from prometheus_client import start_http_server, Counter, Gauge

ERROR_THRESHOLD = 5
alert_triggered = False
error_count = 0
total_count_local = 0
start_time = time.time()

# Prometheus metrics
error_counter = Counter('error_count', 'Total number of error logs')
log_lines_total = Counter('log_lines_total', 'Total log lines processed')
error_rate = Gauge('error_rate', 'Error rate (errors per second)')

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

            log_lines_total.inc()
            total_count_local += 1

            if "ERROR" in line:
                error_counter.inc()
                error_count_local += 1

            if error_count >= ERROR_THRESHOLD and not alert_triggered:
                print(f"🚨 ALERT: High error count ({error_count})")
                alert_triggered = True

            if error_count < ERROR_THRESHOLD:
                alert_triggered = False


if __name__ == "__main__":
    monitor("app.log")
