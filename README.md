### 📋 Güncelleme: [19 Nisan 2026/12.53] - Altyapı Hazırlandı
- AWS IoT Core üzerinde "Simulated_IoT_Device" oluşturuldu ve sertifikalar alındı.
- Python tabanlı IoT Simulator yazıldı ve bağlantı testi başarıyla tamamlandı.
- Verilerin depolanacağı DynamoDB tablosu (`IoT_Sensor_Data`) yapılandırıldı.
- **Partition Key:** device_id (String)
- **Sort Key:** timestamp (Number)


### 📋 Güncelleme: [19 Nisan 2026/17.53] - Geliştirme ve Hata Düzeltimi
Projenin canlıya alınması ve veri akışının stabilize edilmesi sürecinde karşılaşılan teknik engeller ve uygulanan çözümler aşağıda detaylandırılmıştır:
# 1. Veri Tipi Uyumsuzluğu
IoT simülatöründen gelen veriler Lambda fonksiyonu aracılığıyla DynamoDB'ye yazılırken veri tipi uyumsuzluğu hatasıyla karşılaşılmıştır.
- **Çözüm:**Lambda fonksiyonuna Decimal modülü eklenerek ondalıklı verilerin dönüştürülmesiyle çözülmüştür.
- **Teknik Uygulama:** Kod bloğuna `json.loads(json.dumps(event), parse_float=Decimal)` mantığı eklenerek veri bütünlüğü korunmuş ve yazma hatası giderilmiştir.

# 2. AWS CloudWatch ile Hata Ayıklama (Debugging)
Sistem mimarisindeki veri akışını izlemek ve görünmez hataları tespit etmek için **AWS CloudWatch Logs** kullanılmıştır.
- **Tespit:** Verilerin IoT Core'dan başarıyla çıktığı ancak DynamoDB'ye yazılmadan hemen önce Lambda katmanında hata aldığı CloudWatch log akışları (Log Streams) sayesinde hızlıca teşhis edilmiştir.

# 3. Veri Doğrulama ve Canlı Test
Simülatörden gönderilen verilerin veritabanına ulaşıp ulaşmadığı başlangıçta belirsiz kalmıştır. DynamoDB üzerinde yapılan Scan sorguları ile verilerin tabloya başarılı bir şekilde kaydedildiği kanıtlanarak sistemin çalışırlığı teyit edilmiştir.