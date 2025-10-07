#!/usr/bin/env python3
import json, subprocess, datetime, os

devices = ["10.0.0.1", "10.0.0.2"]
results = []

for device in devices:
    r = subprocess.run(["ping", "-c", "1", device], stdout=subprocess.DEVNULL)
    status = "up" if r.returncode == 0 else "down"
    results.append({
        "device": device,
        "status": status,
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    })

with open("status.json", "w") as f:
    json.dump(results, f, indent=2)
