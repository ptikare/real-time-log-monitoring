# Real-Time Log Monitoring & Alerting System (SRE Project)
This project is a real-time log monitoring system built using Python, designed to simulate core Site Reliability Engineering (SRE) practices.
It continuously reads application logs, detects anomalies such as error spikes and high traffic, and triggers alerts using threshold-based logic.


# Features
- Real-time log monitoring (tail -f behavior)
- Log parsing with timestamp and severity levels
- Error spike detection using sliding window algorithm
- Configurable alert thresholds
- Lightweight and extensible design


# Tech Stack
- Python
- Regex for parsing
- Deque (sliding window logic)


# Log Generator
To simulate real-time logs:
python log_generator.py


# How it works
1. The system continuously reads incoming logs.
2. Extracts timestamp and log level.
3. Maintains a rolling time window (e.g., last 10 seconds).
4. Triggers alerts when:
   - Error count exceeds threshold
   - Request rate spikes


# How to Run
python monitor.py


# Sample log Format
2026-04-09 12:00:01 INFO Request successful
2026-04-09 12:00:02 ERROR Database connection failed


# Future Improvements
- Slack/Email alert integration
- Prometheus metrics endpoint
- Docker containerization
- CI/CD pipeline (Jenkins)
- Deployment on AWS
