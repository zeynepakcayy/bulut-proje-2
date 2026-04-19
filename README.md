### 📋 Güncelleme: [19 Nisan 2026/12.53] - Altyapı Hazırlandı
- AWS IoT Core üzerinde "Simulated_IoT_Device" oluşturuldu ve sertifikalar alındı.
- Python tabanlı IoT Simulator yazıldı ve bağlantı testi başarıyla tamamlandı.
- Verilerin depolanacağı DynamoDB tablosu (`IoT_Sensor_Data`) yapılandırıldı.
- **Partition Key:** device_id (String)
- **Sort Key:** timestamp (Number)