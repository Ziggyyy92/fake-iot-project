import pandas as pd
import matplotlib.pyplot as plt

def plot_temperature_data(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data["timestamp"], data["temperature"], label="Temperature")
    plt.xticks(rotation=45)
    plt.xlabel("Timestamp")
    plt.ylabel("Temperature (Celsius)")
    plt.title("Temperature Data")
    plt.legend()
    plt.tight_layout()
    plt.show()