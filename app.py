import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Başlık
st.title("📊 Kişisel Kredi Başvuru Tahmin Uygulaması")

# Veriyi yükle
data = pd.read_excel("Bank_Personal_Loan_Modelling.xlsx", sheet_name="Data")

# Girdi / Çıktı ayrımı
X = data.drop('Personal Loan', axis=1)
y = data['Personal Loan']

# Eğitim / Test bölmesi
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli eğit
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Kullanıcıdan veriler al
st.sidebar.header("Müşteri Bilgileri")

age = st.sidebar.slider("Yaş", 18, 75, 35)
experience = st.sidebar.slider("İş Tecrübesi (yıl)", -5, 40, 5)
income = st.sidebar.slider("Gelir (bin $)", 10, 200, 50)
family = st.sidebar.selectbox("Aile Büyüklüğü", [1, 2, 3, 4])
ccavg = st.sidebar.slider("Aylık Kredi Kartı Harcaması (bin $)", 0.0, 10.0, 1.0)
education = st.sidebar.selectbox("Eğitim Seviyesi", [1, 2, 3])
mortgage = st.sidebar.slider("Mortgage (bin $)", 0, 500, 0)
securities = st.sidebar.selectbox("Menkul Hesabı Var mı?", [0, 1])
cd = st.sidebar.selectbox("CD Hesabı Var mı?", [0, 1])
online = st.sidebar.selectbox("Online Bankacılık Kullanıyor mu?", [0, 1])
creditcard = st.sidebar.selectbox("Kredi Kartı Var mı?", [0, 1])
# Sabitlenen (örnek) bilgiler
zipcode = 91107
customer_id = 99999

# Tahmin için giriş verisi (tüm sütunlara karşılık gelen sırayla)
input_data = pd.DataFrame([[age, experience, income, family, ccavg, education, mortgage,
                            securities, cd, online, creditcard, zipcode, customer_id]],
                          columns=X.columns)

# Tahmin
prediction = model.predict(input_data)[0]

# Sonucu göster
st.subheader("🧠 Tahmin Sonucu")
if prediction == 1:
    st.success("✅ Bu müşteri büyük ihtimalle kredi alacak.")
else:
    st.warning("⚠️ Bu müşteri kredi almayabilir.")