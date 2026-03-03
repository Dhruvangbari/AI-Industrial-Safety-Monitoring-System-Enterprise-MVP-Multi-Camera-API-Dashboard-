import os
import pandas as pd
import time
import cv2
from config import VIOLATION_COOLDOWN

os.makedirs("../logs/images", exist_ok=True)
last_logged = {}

def log_violation(person, frame):
    pid = person["id"]
    current = time.time()

    if pid in last_logged and current - last_logged[pid] < VIOLATION_COOLDOWN:
        return

    last_logged[pid] = current

    filename = f"../logs/images/{pid}_{int(current)}.jpg"
    cv2.imwrite(filename, frame)

    df = pd.DataFrame([[pid, current]], columns=["person_id", "timestamp"])
    df.to_csv("../logs/violations.csv",
              mode='a',
              header=not os.path.exists("../logs/violations.csv"),
              index=False)
