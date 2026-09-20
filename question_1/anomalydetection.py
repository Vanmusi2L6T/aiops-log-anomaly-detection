import matplotlib.pyplot as plt
from statistics import mean

time = [
    "10:00", "10:01", "10:02", "10:03", "10:04",
    "10:05", "10:06", "10:07", "10:08", "10:09",
    "10:10", "10:11", "10:12", "10:13", "10:14",
    "10:15", "10:16", "10:17", "10:18", "10:19"
]

cpu = [
    45, 52, 48, 55, 60,
    95, 57, 50, 62, 58,
    54, 63, 97, 59, 56,
    61, 53, 64, 92, 58
]

memory = [
    58, 61, 59, 63, 65,
    68, 64, 62, 67, 66,
    60, 69, 71, 65, 63,
    68, 60, 70, 73, 64
]

response_time = [
    210, 225, 218, 230, 245,
    260, 235, 220, 250, 240,
    215, 255, 275, 238, 228,
    248, 218, 265, 285, 232
]

# Find CPU values above 90%
anomaly_positions = []

for i in range(len(cpu)):
    if cpu[i] > 90:
        anomaly_positions.append(i)

print("Total records:", len(time))
print("Anomalies detected:", len(anomaly_positions))

print("\nTimestamp       CPU       Status")

for position in anomaly_positions:
    print(time[position], "       ", str(cpu[position]) + "%", "    ANOMALY")

print("\nBasic statistics:")
print("Average CPU:", round(mean(cpu), 2), "%")
print("Average memory:", round(mean(memory), 2), "%")
print("Average response time:", round(mean(response_time), 2), "ms")

# Create graph
plt.plot(time, cpu, marker="o", label="CPU usage")

for position in anomaly_positions:
    plt.scatter(
        time[position],
        cpu[position],
        color="red",
        s=150,
        label="Anomaly" if position == anomaly_positions[0] else ""
    )

plt.title("CPU Usage and Anomalies")
plt.xlabel("Time")
plt.ylabel("CPU usage (%)")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()

plt.savefig("anomalies.png")
print("\nGraph saved as anomalies.png")