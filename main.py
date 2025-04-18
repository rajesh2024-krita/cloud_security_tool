
import json
import time
from datetime import datetime

USER_DB_FILE = "user_db.json"
LOG_FILE = "logs/activity_log.txt"

# Log activity
def log_activity(module, message):
    with open(LOG_FILE, 'a') as log:
        log.write(f"{datetime.now()} - [{module}] - {message}\n")

# IAM: Identity Access Management
def simulate_iam_login(username, password):
    users = load_users()
    user_data = users.get(username)

    if not user_data:
        log_activity("IAM", f"Login failed - User {username} not found.")
        return False

    if user_data["locked"]:
        log_activity("IAM", f"Login failed - User {username} is locked.")
        return False

    if password == user_data["password"]:
        users[username]["failed_attempts"] = 0
        log_activity("IAM", f"Login successful - User {username}")
    else:
        users[username]["failed_attempts"] += 1
        log_activity("IAM", f"Login failed - Incorrect password for user {username}")
        if users[username]["failed_attempts"] >= 3:
            users[username]["locked"] = True
            log_activity("IAM", f"User {username} locked due to multiple failed attempts")

    with open(USER_DB_FILE, 'w') as file:
        json.dump(users, file, indent=4)

    return password == user_data["password"]

# EDR: Endpoint Detection Simulation
def simulate_edr_detection():
    log_activity("EDR", "Malware signature matched on endpoint-PC1. Threat quarantined.")

# SIEM: Security Incident Event Management Logging
def simulate_siem_alert():
    log_activity("SIEM", "Anomalous login attempt detected from IP 192.168.1.105.")

def load_users():
    with open(USER_DB_FILE, 'r') as file:
        return json.load(file)

def run_simulation():
    print("=== Cloud-Based Cyber Security Simulation ===")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if simulate_iam_login(username, password):
        print("Access Granted ✅")
        simulate_edr_detection()
        simulate_siem_alert()
    else:
        print("Access Denied ❌")

if __name__ == "__main__":
    run_simulation()
