import streamlit as st
from streamlit_gsheets import GSheetsConnection
from datetime import date
import pandas as pd

# صفحہ کی سیٹنگ
st.set_page_config(page_title="Digital Khata Book", layout="wide")

st.title("📔 ڈیجیٹل کھاتہ بک - اکاؤنٹ مینجمنٹ سسٹم")

# گوگل شیٹ کے ساتھ کنکشن
conn = st.connection("gsheets", type=GSheetsConnection)

# ڈیٹا پڑھنا (تاکہ ہیڈنگز کا پتہ چل سکے)
existing_data = conn.read(worksheet="Sheet1", usecols=[0,1,2,3,4,5], ttl=5)
existing_data = existing_data.dropna(how="all")

menu = ["نئی انٹری", "ریکارڈ دیکھیں"]
choice = st.sidebar.selectbox("مینو منتخب کریں", menu)

if choice == "نئی انٹری":
    st.subheader("نیا کھاتہ اندراج فارم")
    with st.form("khata_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("گاہک کا نام")
            phone = st.text_input("فون نمبر")
            khat_type = st.radio("کھاتہ کی قسم", ["جمع (+)", "بقایا (-)"])
        with col2:
            today = st.date_input("تاریخ", date.today())
            amount = st.number_input("رقم", min_value=0)
            detail = st.text_area("تفصیل / بابت")
        
        submit = st.form_submit_button("محفوظ کریں")
        
        if submit:
            if name and amount > 0:
                # نیا ڈیٹا تیار کرنا
                new_entry = pd.DataFrame([{
                    "Name": name,
                    "Phone": phone,
                    "Type": khat_type,
                    "Amount": amount,
                    "Detail": detail,
                    "Date": str(today)
                }])
                
                # پرانے ڈیٹا میں نیا ڈیٹا شامل کرنا
                updated_df = pd.concat([existing_data, new_entry], ignore_index=True)
                
                # گوگل شیٹ میں اپ ڈیٹ کرنا
                conn.update(worksheet="Sheet1", data=updated_df)
                st.success(f"شکریہ! {name} کا اندراج شیٹ میں محفوظ ہو گیا ہے۔")
            else:
                st.error("براہ کرم نام اور رقم درست درج کریں۔")

elif choice == "ریکارڈ دیکھیں":
    st.subheader("تمام ریکارڈ")
    st.dataframe(existing_data)
