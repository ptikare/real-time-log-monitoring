import re
from datetime import datetime

def parse_log(line):
  pattern = r"^(.*?)\s+(INFO|ERROR|WARN)"
  match = re.match(pattern, line)

  if match:
    timestamp_str, level = match.groups()
    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    return timestamp, level
  return None, None


def analyze_logs(file_path):
  error_count = 0

  with open(file_path, "r") as file:
    for line in file:
      _, level = parse_log(line)
      if level == "ERROR":
        error_count += 1

  print(f"Total ERROR logs: {error_count}")


if __name__ == "__main__":
  analyze_logs("app.log")
