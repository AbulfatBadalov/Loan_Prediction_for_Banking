import streamlit as st
import pickle
import numpy as np

# Modeli yükle
with open('model.pkl','rb') as file:
  dt_model=pickle.load(file)

# Load model columns
with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)



st.title("Kişisel Kredi Başvuru Tahmini")

st.markdown("Aşağıdaki bilgileri doldurarak kredi başvurusunun onaylanıp onaylanmayacağını tahmin edebilirsiniz.")

# Form yapısı
with st.form("loan_form"):
    age = st.slider("Yaş", 18, 100, 30)
    experience = st.number_input("İş Deneyimi (Yıl)", -10, 50, 5)
    income = st.number_input("Yıllık Gelir (bin $)", 0, 500, 50)
    ccavg = st.number_input("Kredi Kartı Harcaması (bin $)", 0.0, 20.0, 1.5)
    mortgage = st.number_input("Mortgage Miktarı", 0, 1000, 0)
    
    securities_account = st.selectbox("Men. Kıymet Hesabı Var mı?", ['Hayır', 'Evet'])
    cd_account = st.selectbox("Vadeli Mevduat Hesabı Var mı?", ['Hayır', 'Evet'])
    online = st.selectbox("Online Bankacılık Kullanıyor mu?", ['Hayır', 'Evet'])
    credit_card = st.selectbox("Kredi Kartı Var mı?", ['Hayır', 'Evet'])

    education = st.selectbox("Eğitim Durumu", ['Undergrad', 'Graduate', 'Advanced/Professional'])
    family = st.selectbox("Aile Büyüklüğü", [1, 2, 3, 4])

    # Submit butonu
    submitted = st.form_submit_button("Submit")

if submitted:
    # Giriş verilerini hazırla
    input_dict = {
        'Age': age,
        'Experience': experience,
        'Income': income,
        'CCAvg': ccavg,
        'Mortgage': mortgage,
        'Securities Account': 1 if securities_account == 'Evet' else 0,
        'CD Account': 1 if cd_account == 'Evet' else 0,
        'Online': 1 if online == 'Evet' else 0,
        'CreditCard': 1 if credit_card == 'Evet' else 0,
        'Education_2': 1 if education == 'Graduate' else 0,
        'Education_3': 1 if education == 'Advanced/Professional' else 0,
        'Family_2': 1 if family == 2 else 0,
        'Family_3': 1 if family == 3 else 0,
        'Family_4': 1 if family == 4 else 0
    }

    # Eksik kolonları 0 ile doldur
    input_data = [input_dict.get(col, 0) for col in model_columns]

    # Tahmin
    prediction = dt_model.predict([input_data])[0]
    if prediction == 1:
        st.success("Tahmin: ✅ Kredi başvurusu ONAYLANIR.")
    else:
        st.warning("Tahmin: ❌ Kredi başvurusu REDDEDİLİR.")