import streamlit as st
import base64
import os

# ۱. تنظیمات اولیه صفحه
st.set_page_config(page_title="پورتال مهندسی محتوا عاشورا", layout="wide")

# ۲. تابع تبدیل عکس به فرمت CSS (Base64)
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

# نام فایل‌های تو (اگر نام فایل لوگو را عوض کردی اینجا هم اصلاح کن)
img_banner = "Picture1.tif"  # پیشنهاد: تبدیل به PNG برای کیفیت بهتر
img_logo = "official_logo.png"

bin_str_logo = get_base64(img_logo)
bin_str_banner = get_base64(img_banner)

# ۳. تزریق کدهای CSS برای استایل‌دهی نهایی
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {{
        background-color: #f0f2f5;
        direction: rtl;
        text-align: right;
        font-family: 'Vazirmatn', sans-serif;
    }}

    /* نوار هدر اصلی */
    .header-banner {{
        background-color: #5c85c1; /* رنگ آبی ملایم بر اساس اسکرین شات */
        background-image: linear-gradient(rgba(0,0,0,0.1), rgba(0,0,0,0.1)), url("data:image/tif;base64,{bin_str_banner}");
        background-size: cover;
        background-position: center;
        height: 200px;
        border-radius: 0 0 50px 50px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        color: white;
        margin-top: -65px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }}

    .logo-img {{
        width: 100px;
        margin-bottom: 10px;
    }}

    /* تنظیمات متون روی عکس */
    .header-banner h1 {{
        font-size: 40px;
        font-weight: bold;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
        margin: 0;
    }}

    /* تنظیمات سایدبار */
    [data-testid="stSidebar"] {{
        background-color: #0d47a1;
        color: white;
    }}

    /* دکمه استخراج */
    .stButton>button {{
        background-color: #ffc107 !important;
        color: #0d47a1 !important;
        font-weight: bold;
        border-radius: 12px;
        height: 45px;
        width: 100%;
        border: none;
    }}

    /* فوتر نواری پایین */
    .footer-strip {{
        background-color: #0d47a1;
        color: #ffc107;
        padding: 15px;
        text-align: center;
        font-weight: bold;
        border-radius: 10px;
        margin-top: 50px;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
    }}
    
    /* اصلاح رنگ برچسب‌های متنی */
    h3, label, p {{
        color: #1a237e !important;
    }}
    </style>
    
    <div class="header-banner">
        <img src="data:image/png;base64,{bin_str_logo}" class="logo-img">
        <h1>سامانه مهندسی محتوا</h1>
    </div>
    <br>
""", unsafe_allow_html=True)

# ۴. بخش منوی کناری (سایدبار)
with st.sidebar:
    st.markdown("### 🛠️ ابزارهای مدیریتی")
    unit = st.selectbox("واحد انتخابی:", ["فنی و مهندسی", "HSSE", "مالی و اداری", "ماشین‌آلات"])
    st.divider()
    st.write("پورتال مرکزی مدیریت دانش")

# ۵. محتوای میانی سایت
c1, c2 = st.columns(2)

with c1:
    st.markdown("### 🖋️ ثبت چالش یا تجربه")
    issue = st.text_area("شرح واقعه یا موضوع تخصصی:", height=200, placeholder="جزئیات را اینجا وارد کنید...")
    submit = st.button("🚀 استخراج سناریو و تحلیل")

with c2:
    st.markdown("### 📋 خروجی و سناریوی پیشنهادی")
    if submit:
        if issue:
            st.info(f"واحد {unit}: تحلیل داده‌ها بر اساس نشریات آغاز شد...")
            st.success(f"پیشنهاد نهایی: محتوا در قالب 'ویدیو کوتاه آموزشی' با تکیه بر تجربه چالش {issue[:20]}... تولید گردد.")
            st.balloons()
        else:
            st.error("لطفاً شرح واقعه را وارد نمایید.")

# ۶. فوتر اصلاح شده طبق درخواست شما
st.markdown("""
    <div class="footer-strip">
        مرکز تحقیق و توسعه موسسه عاشورا - مدیریت تولید محتوا
    </div>
""", unsafe_allow_html=True)
