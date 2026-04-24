import streamlit as st
import pandas as pd
from datetime import date
from shillelagh.backends.apsw.db import connect

# صفحہ کی سیٹنگ
st.set_page_config(page_title="Digital Khata Book", layout="wide")

# آپ کی گوگل شیٹ کا لنک
sheet_url = "https://docs.google.com/spreadsheets/d/1iev-e2cWP15HhNXxT1j-Zkg-By885HpmlC1IgvXtpSA/edit#gid=0"

st.title("📔 ڈیجیٹل کھاتہ بک - اکاؤنٹ مینجمنٹ سسٹم")

# سائیڈ بار مینو
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
                # یہاں ڈیٹا سیو کرنے کا لاجک آئے گا
                st.success(f"شکریہ! {name} کا {amount} روپے کا اندراج ہو گیا ہے۔")
                st.info("نوٹ: ڈیٹا ابھی شیٹ میں بھیجنے کے لیے کنکشن سیٹ ہو رہا ہے۔")
            else:
                st.error("براہ کرم نام اور رقم درست درج کریں۔")

elif choice == "ریکارڈ دیکھیں":
    st.subheader("تمام ریکارڈ")
    st.write("آپ کا ڈیٹا نیچے دی گئی گوگل شیٹ میں محفوظ ہو رہا ہے:")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # یہ عارضی ہے
    st.link_button("گوگل شیٹ کھولیں", sheet_url)
