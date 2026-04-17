import time
import random
from datetime import datetime

LOG_FILE = "app.log"

levels = ["INFO", "INFO", "INFO", "WARN", "ERROR"]  
# More INFO to simulate real systems

messages = {
    "INFO": [
        "Request successful",
        "User login successful",
        "Data fetched successfully"
    ],
    "WARN": [
        "High memory usage",
        "Slow response detected"
    ],
    "ERROR": [
        "Database connection failed",
        "Timeout occurred",
        "Service unavailable"
    ]
}


def generate_log():
    level = random.choice(levels)
    message = random.choice(messages[level])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"{timestamp} {level} {message}"


def start_logging():
    print("🚀 Generating logs... Press Ctrl+C to stop.\n")

    with open(LOG_FILE, "a") as file:
        while True:
            log = generate_log()
            file.write(log + "\n")
            file.flush()  # ensure immediate write

            print(log)  # optional: see logs in terminal

            # Random delay to simulate traffic
            time.sleep(random.uniform(0.2, 1.5))


if __name__ == "__main__":
    start_logging()
