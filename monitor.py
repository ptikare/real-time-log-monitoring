def analyze_logs(file_path):
  error_count = 0

  with open(file_path, "r") as file:
    for line in file:
      if "ERROR" in line:
        error_count += 1

  print(f"Total ERROR logs: {error_count}")


if __name__ == "__main__":
  analyze_logs("app.log")
  
