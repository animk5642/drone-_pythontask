sensor_stream = [
    {"sensor": "Main_IMU", "status": "Active", "temperature": 42},
    {"sensor": "Front_LiDAR", "status": "Error", "temperature": 55},
    {"sensor": "Optical_Flow", "status": "Active", "temperature": 38},
    {"sensor": "GPS_Module", "status": "Error", "temperature": 72},
    {"sensor": "Alt_Telemetry", "status": "Active", "temperature": 40}
]


for item in sensor_stream:
  if(item["status"]=="Error"):
    print(f"print: 🛑 ALERT: {item['sensor']} has FAILED!")
  if(item["temperature"]>60):
      print(f"⚠️ CRITICAL: {item['sensor']} is OVERHEATING at {item['temperature']}°C!")
  