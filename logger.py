import datetime

LOG_FILE = "logs.txt"

def log_action(message):
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{time_now}] {message}\n"

    with open(LOG_FILE, "a") as f:
        f.write(line)