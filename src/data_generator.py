import pandas as pd
import random
from datetime import datetime, timedelta

def generate_fake_temperature_data(num_samples):
    data = []
    for i in range(num_samples):
        # Povremeno ubaci anomaliju
        temp = random.uniform(50.0, 80.0) if i % 20 == 0 else random.uniform(15.0, 30.0)
        entry = {
            "device_id": f"sensor_{random.randint(1, 10)}",
            "timestamp": (datetime.now() +  timedelta(seconds=i)).isoformat(),
            "temperature": round(temp, 2),
            "humidity": round(random.uniform(30.0, 60.0), 2)
        }
        data.append(entry)
    return pd.DataFrame(data)