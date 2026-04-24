import streamlit as st
import pandas as pd
from datetime import date

# صفحہ کی سیٹنگ
st.set_page_config(page_title="Digital Khata Book", layout="wide")

st.title("📔 ڈیجیٹل کھاتہ بک - اکاؤنٹ مینجمنٹ سسٹم")

# سائیڈ بار مینو
menu = ["نئی انٹری", "ریکارڈ دیکھیں", "جی میل بیک اپ"]
choice = st.sidebar.selectbox("مینو منتخب کریں", menu)

if choice == "نئی انٹری":
    st.subheader("نیا کھاتہ اندراج فارم")
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("گاہک کا نام")
        phone = st.text_input("فون نمبر")
        khat_type = st.radio("کھاتہ کی قسم", ["جمع (+)", "بقایا (-)"])
        
    with col2:
        today = st.date_input("تاریخ", date.today())
        amount = st.number_input("رقم", min_value=0)
        detail = st.text_area("تفصیل / بابت")
        wada = st.text_input("وعدہ (دن)")

    if st.button("محفوظ کریں"):
        st.success(f"{name} کا کھاتہ محفوظ ہو گیا ہے!")

elif choice == "ریکارڈ دیکھیں":
    st.subheader("گاہک کا ریکارڈ تلاش کریں")
    search = st.text_input("نام یا فون نمبر لکھیں")
    if st.button("تلاش کریں"):
        st.info("سرچ فنکشن ابھی سیٹ ہو رہا ہے...")

elif choice == "جی میل بیک اپ":
    st.subheader("ڈیٹا بیک اپ (Gmail)")
    st.write("آپ کا ڈیٹا جی میل پر بھیجنے کے لیے تیار ہے۔")
    if st.button("بیک اپ بھیجیں"):
        st.warning("جی میل سیٹنگ ابھی باقی ہے۔")
