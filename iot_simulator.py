import time
import json
import random
from awscrt import mqtt
from awsiot import mqtt_connection_builder

# --- AYARLAR ---
ENDPOINT = "a2mzrnb96fxzyy-ats.iot.eu-central-1.amazonaws.com" # Burayı değiştir!
CERT_FILE = "certs/5a6457f79110e9cbf0216280e050b50e3cbc0966b777608a65177efaf727d7dc-certificate.pem.crt" # Dosya adını kontrol et
KEY_FILE = "certs/5a6457f79110e9cbf0216280e050b50e3cbc0966b777608a65177efaf727d7dc-private.pem.key"      # Dosya adını kontrol et
ROOT_CA = "certs/AmazonRootCA1.pem"
TOPIC = "iot/sensor_data"
CLIENT_ID = "Simulated_IoT_Device"

# --- BAĞLANTI KURULUMU ---
mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=ENDPOINT,
    cert_filepath=CERT_FILE,
    pri_key_filepath=KEY_FILE,
    ca_filepath=ROOT_CA,
    client_id=CLIENT_ID,
    clean_session=False,
    keep_alive_secs=30
)

print(f"AWS IoT Core'a bağlanılıyor: {ENDPOINT}...")
connect_future = mqtt_connection.connect()
connect_future.result()
print("Bağlantı Başarılı!")

# --- VERİ GÖNDERİMİ (SİMÜLASYON) ---
try:
    while True:
        # Rastgele sıcaklık ve nem verisi üret
        data = {
            "device_id": CLIENT_ID,
            "timestamp": int(time.time()),
            "temperature": round(random.uniform(20.0, 30.0), 2),
            "humidity": round(random.uniform(40.0, 60.0), 2)
        }
        
        message = json.dumps(data)
        mqtt_connection.publish(topic=TOPIC, payload=message, qos=mqtt.QoS.AT_LEAST_ONCE)
        print(f"Veri Gönderildi: {message}")
        time.sleep(5) # 5 saniyede bir gönder
except KeyboardInterrupt:
    print("Simülasyon durduruldu.")
    mqtt_connection.disconnect().result()