# Gerekli kütüphaneleri içe aktar
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, roc_auc_score, accuracy_score
import matplotlib.pyplot as plt
from sklearn import tree

# Excel dosyasını oku, 'Data' adlı sayfayı kullan
data = pd.read_excel('Bank_Personal_Loan_Modelling.xlsx', sheet_name='Data')

data.shape
data.value_counts()
#Eksik veriler
data.isnull().sum()
# 2. Gereksiz sütunları at (ID ve ZIP Code)
data.drop(columns=['ID','ZIP Code'],inplace=True)
#Eksik verileri yeniden kontrol
data.isnull().sum()
#Kategorik verileri one-hot-encoding ile dondurme
data=pd.get_dummies(data,columns=['Education','Family'],drop_first=True)
# İlk 5 satırı görüntüle (kontrol amaçlı)
data.head(5)

# Bağımsız değişkenleri (özellikler) ve hedef değişkeni ayır
X = data.drop('Personal Loan', axis=1)  # Hedef sütunu dışarıda bırak
y = data['Personal Loan']               # Hedef sütunu seç

# Veriyi eğitim ve test olarak ayır (80% eğitim, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Karar ağacı sınıflandırıcısı oluştur
dt_model = DecisionTreeClassifier()

# Modeli eğitim verisiyle eğit
dt_model.fit(X_train, y_train)

# Test verisi ile tahmin yap
y_pred = dt_model.predict(X_test)

# Karışıklık matrisi hesapla ve yazdır
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Sınıflandırma raporunu yazdır (doğruluk, kesinlik, F1 skoru vs.)
class_report = classification_report(y_test, y_pred)
print("\nClassification Report:")
print(class_report)

# ROC eğrisi ve AUC skoru hesapla
y_prob = dt_model.predict_proba(X_test)[:, 1]  # Pozitif sınıfın olasılığı
fpr, tpr, thresholds = roc_curve(y_test, y_prob)  # ROC eğrisi için değerler
auc_score = roc_auc_score(y_test, y_prob)        # AUC skoru

# ROC eğrisini çiz
plt.figure()
plt.plot(fpr, tpr, color='blue', label='ROC curve (area = %0.2f)' % auc_score)
plt.plot([0, 1], [0, 1], color='red', linestyle='--')  # Y = X doğrusu
plt.xlabel('False Positive Rate')  # X ekseni etiketi
plt.ylabel('True Positive Rate')   # Y ekseni etiketi
plt.title('ROC Curve')             # Grafik başlığı
plt.legend(loc="lower right")      # Lejant konumu
plt.show()

# Farklı eğitim-test oranları ile modelin doğruluğunu test et
split_ratios = [(0.6, 0.4), (0.5, 0.5), (0.7, 0.3), (0.8, 0.2), (0.9, 0.1), (0.95, 0.05)]

# Her bir oran için eğitim ve test doğruluklarını karşılaştır
for train_ratio, test_ratio in split_ratios:
    # Veriyi belirlenen oranlarda ayır
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_ratio, test_size=test_ratio, random_state=42)
    
    # Modeli yeniden eğit
    dt_model.fit(X_train, y_train)
    
    # Eğitim ve test seti tahminleri
    y_train_pred = dt_model.predict(X_train)
    y_test_pred = dt_model.predict(X_test)
    
    # Doğruluk skorlarını hesapla
    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    
    # Sonuçları yazdır
    print(f"Train-Test Split: {train_ratio}-{test_ratio}")
    print(f"Training Accuracy: {train_accuracy}")
    print(f"Testing Accuracy: {test_accuracy}")
    print("\n")
    import pickle

# Modeli kaydet
with open("model.pkl", "wb") as file:
    pickle.dump(dt_model, file)
# Save model_columns
with open("model_columns.pkl", "wb") as file:
    pickle.dump(model_columns, file)
