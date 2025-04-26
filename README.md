# 📊 Banka Kişisel Kredi Tahmin Modeli

Bu proje, bir bankanın müşterilerine kişisel kredi (Personal Loan) verip vermemesi gerektiğini makine öğrenmesi ile tahmin etmeyi amaçlamaktadır. Model olarak **Karar Ağacı (Decision Tree Classifier)** kullanılmıştır.

---

## 🔍 Proje Hakkında

- **Veri seti:** `Bank_Personal_Loan_Modelling.xlsx` dosyasının `Data` sayfası
- **Hedef:** Müşterinin kişisel kredi alıp almayacağını tahmin etmek (`Personal Loan` sütunu)
- **Yöntem:** Gözetimli öğrenme - Sınıflandırma
- **Model:** `DecisionTreeClassifier` (sklearn)

---

## 🛠️ Kullanılan Kütüphaneler

- pandas
- scikit-learn (sklearn)
- matplotlib
- openpyxl (Excel okuma için)

---

## 📁 Adım Adım İşleyiş

1. Excel dosyasından veri okundu
2. Özellikler (`X`) ve hedef değişken (`y`) ayrıldı
3. %80 eğitim - %20 test oranı ile veri bölündü
4. Karar ağacı modeli oluşturulup eğitildi
5. Test verisi üzerinde tahmin yapıldı
6. Aşağıdaki metriklerle model performansı değerlendirildi:
   - Karışıklık Matrisi (Confusion Matrix)
   - Sınıflandırma Raporu (Precision, Recall, F1-Score)
   - ROC Eğrisi & AUC Skoru
7. Farklı eğitim/test oranları denenerek modelin kararlılığı test edildi

---

## 📊 ROC Eğrisi

Modelin pozitif sınıfı tahmin etme başarısı **ROC Curve** ve **AUC Score** ile görselleştirilmiştir. AUC skoru 1'e ne kadar yakınsa, model o kadar iyi performans göstermektedir.

---

## ⚙️ Farklı Veri Bölme Denemeleri

Model aşağıdaki oranlarla yeniden eğitilmiş ve her durumda doğruluk skorları hesaplanmıştır:

- 60% eğitim / 40% test
- 50% eğitim / 50% test
- 70% eğitim / 30% test
- 80% eğitim / 20% test
- 90% eğitim / 10% test
- 95% eğitim / 5% test

Her oranda eğitim ve test doğrulukları karşılaştırılarak modelin genelleme yeteneği analiz edilmiştir.

---

## ✅ Sonuç

Karar ağacı modeli, kişisel kredi tahmini konusunda yüksek başarı göstermektedir. Modelin doğruluğu, kullanılan eğitim/test oranına ve veri dağılımına göre değişiklik gösterebilir. ROC eğrisi ve sınıflandırma metrikleri modelin performansını görsel ve sayısal olarak doğrulamaktadır.

---

## 📌 Notlar

- Hiperparametre ayarları yapılmadan temel model kullanılmıştır.
- Geliştirme için `max_depth`, `criterion`, `min_samples_split` gibi parametrelerle oynamak önerilir.
- Modelin görsel olarak karar ağacı şeklinde çizilmesiyle daha iyi yorumlama sağlanabilir.

---

🧠 **Makine Öğrenmesi ile Kredi Tahmini – Karar Ağacı Kullanımı**  
📂 Dosya: `Bank_Personal_Loan_Modelling.xlsx`  
📘 Model: `DecisionTreeClassifier` (scikit-learn)

************Abulfat Badalov*************
