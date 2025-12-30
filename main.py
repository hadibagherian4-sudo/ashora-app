import streamlit as st
import base64
import os

# ۱. تنظیمات اولیه صفحه
st.set_page_config(page_title="پورتال هوشمند عاشورا", layout="wide")

# ۲. تابع تبدیل عکس محلی به فرمت قابل نمایش در CSS (Base64)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# نام فایل‌های تو در گیت‌هاب (اگر تغییر دادی اینجا هم اصلاح کن)
img_banner_top = "Picture1.tif" 
img_logo_side = "ChatGPT Image Dec 27, 2025, 03_01_00 PM.png"

# ۳. تزریق کدهای CSS برای بنرها و پس‌زمینه
def set_style():
    # بنر بالایی به صورت نواری
    bin_str_top = ""
    if os.path.exists(img_banner_top):
        bin_str_top = get_base64_of_bin_file(img_banner_top)

    st.markdown(f"""
    <style>
    /* فونت فارسی و استایل کلی */
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn&display=swap');
    
    .stApp {{
        background-color: #f4f7f9;
        direction: rtl;
        text-align: right;
    }}
    
    /* بنر بالایی - نواری */
    .header-banner {{
        background-image: linear-gradient(rgba(13, 71, 161, 0.6), rgba(13, 71, 161, 0.6)), url("data:image/tif;base64,{bin_str_top}");
        background-size: cover;
        background-position: center;
        height: 180px;
        border-radius: 0 0 50px 50px;
        margin-top: -60px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }}
    
    .header-banner h1 {{
        font-size: 35px;
        font-family: 'Vazirmatn', sans-serif;
    }}

    /* شخصی‌سازی سایدبار */
    [data-testid="stSidebar"] {{
        background-color: #0d47a1;
        color: white;
        direction: rtl;
    }}
    
    .stButton>button {{
        background-color: #ffc107;
        color: #0d47a1;
        font-weight: bold;
        border-radius: 8px;
    }}
    </style>
    <div class="header-banner">
        <h1>سامانه مهندسی محتوا و مدیریت دانش</h1>
    </div>
    <br>
    """, unsafe_allow_html=True)

set_style()

# ۴. سایدبار (منوی کناری)
with st.sidebar:
    if os.path.exists(img_logo_side):
        st.image(img_logo_side, width=220)
    st.divider()
    st.markdown("### ⚙️ داشبورد مدیریت")
    unit = st.selectbox("واحد مورد نظر:", ["فنی و مهندسی", "HSSE و ایمنی", "مالی", "ماشین‌آلات"])
    st.write("خوش آمدید")

# ۵. بدنه اصلی سایت
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 🖋️ ثبت چالش یا تجربه")
    issue = st.text_area("جزئیات اتفاق را بنویسید:", height=200)
    btn = st.button("🚀 استخراج سناریو")

with col2:
    st.markdown("### 📋 خروجی سیستم")
    if btn:
        if issue:
            st.success(f"واحد {unit}: تحلیل در حال انجام...")
            st.markdown(f"**چالش فنی:** {issue}\n\n**سناریوی ویدیویی پیشنهادی:** ۱. مستندسازی هوایی ۲. تحلیل خطای آیین نامه ۳. پاداش مولف")
        else:
            st.warning("لطفا متن را وارد کنید.")

# ۶. بنر نواری پایینی (فوتر)
st.markdown("""
    <style>
    .footer-strip {
        background-color: #0d47a1;
        color: #ffc107;
        padding: 10px;
        text-align: center;
        border-radius: 10px;
        margin-top: 50px;
        font-weight: bold;
    }
    </style>
    <div class="footer-strip">
        مرکز تحقیق و توسعه موسسه عاشورا - مدیریت دانش سازمانی
    </div>
""", unsafe_allow_html=True)
