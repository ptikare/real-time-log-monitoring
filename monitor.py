from prometheus_client import start_http_server, Counter, Gauge
import time
import os

error_counter = Counter('error_count', 'Total number of error logs')
log_lines_total = Counter('log_lines_total', 'Total log lines processed')
log_levels = Counter('log_levels_total', 'Log levels count', ['level'])
error_rate = Gauge('error_rate', 'Error rate (errors per second)')


def monitor(file_path):
    while not os.path.exists(file_path):
        print("Waiting for log file...")
        time.sleep(1)

    error_count_local = 0
    total_count_local = 0
    start_time = time.time()

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
                log_levels.labels(level="error").inc()
                error_count_local += 1

            elif "INFO" in line:
                log_levels.labels(level="info").inc()

            elif "WARNING" in line:
                log_levels.labels(level="warning").inc()

            elapsed_time = time.time() - start_time
            if elapsed_time > 0:
                error_rate.set(error_count_local / elapsed_time)


if __name__ == "__main__":
    start_http_server(8000, addr="0.0.0.0")
    monitor("app.log")
