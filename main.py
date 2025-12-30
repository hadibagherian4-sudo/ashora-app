import streamlit as st
import base64
import os

# ۱. تنظیمات اولیه صفحه
st.set_page_config(page_title="سامانه مهندسی محتوا عاشورا", layout="wide")

# ۲. تابع تبدیل عکس به فرمت CSS (Base64)
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

# نام فایل‌هایی که در گیت‌هاب داری (حتما مطمئن شو اسم فایل ها دقیقا همین باشد)
img_background = "Picture1.png" # عکس کارگاهی که الان فرستادی (با فرمت png ذخیره کن)
img_logo = "official_logo.png"   # لوگویی که در مرحله قبل فرستادی

bin_str_logo = get_base64(img_logo)
bin_str_bg = get_base64(img_background)

# ۳. تزریق کدهای CSS برای دیزاین اختصاصی
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {{
        background-color: #ffffff;
        direction: rtl;
        text-align: right;
        font-family: 'Vazirmatn', sans-serif;
    }}

    /* نوار هدر پهن با تصویر پس زمینه ای که فرستادی */
    .header-banner {{
        position: relative;
        background-image: linear-gradient(rgba(13, 71, 161, 0.4), rgba(13, 71, 161, 0.4)), url("data:image/png;base64,{bin_str_bg}");
        background-size: cover;
        background-position: center;
        height: 250px;
        width: 100%;
        margin-top: -85px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 0 0 40px 40px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }}

    /* لوگو در گوشه سمت راست بنر */
    .corner-logo {{
        position: absolute;
        top: 20px;
        right: 30px;
        width: 110px;
        filter: drop-shadow(2px 2px 5px rgba(0,0,0,0.4));
    }}

    .header-banner h1 {{
        color: white;
        font-size: 45px;
        font-weight: bold;
        text-shadow: 3px 3px 15px rgba(0,0,0,0.7);
        margin: 0;
    }}

    /* نوار فوتر سفارشی شما */
    .footer-strip {{
        background-color: #0d47a1;
        color: #ffc107;
        padding: 18px;
        text-align: center;
        font-weight: bold;
        border-radius: 12px;
        margin-top: 60px;
        font-size: 16px;
        box-shadow: 0 -4px 10px rgba(0,0,0,0.1);
    }}

    /* اصلاح استایل دکمه و باکس متن */
    .stButton>button {{
        background-color: #ffc107 !important;
        color: #0d47a1 !important;
        border-radius: 10px;
        font-weight: bold;
        border: none;
        height: 50px;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        background-color: #ffd54f !important;
        transform: scale(1.02);
    }}
    
    h3, label, .stMarkdown p {{
        color: #0d47a1 !important;
        font-weight: bold;
    }}
    </style>
    
    <div class="header-banner">
        <img src="data:image/png;base64,{bin_str_logo}" class="corner-logo">
        <h1>سامانه مهندسی محتوا</h1>
    </div>
    <br>
""", unsafe_allow_html=True)

# ۴. سایدبار مدیریتی (سمت چپ ظاهر می شود)
with st.sidebar:
    st.markdown("### 📋 میز کار هوشمند")
    st.info("کاربر گرامی خوش آمدید.")
    unit = st.selectbox("بخش اجرایی را انتخاب کنید:", ["فنی و مهندسی", "امور مالی", "HSSE", "ماشین‌آلات"])
    st.divider()

# ۵. فضای اصلی عملیات
col_a, col_b = st.columns([1, 1])

with col_a:
    st.markdown("### 🖋️ ثبت جزئیات واقعه")
    desc = st.text_area("چالش مهندسی یا حادثه ایمنی را اینجا شرح دهید:", height=200, 
                      placeholder="مثلاً: نحوه مقابله با خاک سست در تونل سازی...")
    action = st.button("🚀 پردازش و مهندسی محتوا")

with col_b:
    st.markdown("### 🎬 سناریوی پیشنهادی سیستم")
    if action:
        if desc:
            with st.status("در حال تطبیق با استانداردهای نظام فنی...", expanded=True):
                st.write("استخراج متن نشریات مرتبط...")
                st.write("تحلیل تجربه عملیاتی ثبت شده...")
                st.success("تجزیه و تحلیل با موفقیت انجام شد.")
            
            st.markdown(f"""
            #### 📦 پکیج آموزشی واحد {unit}:
            ۱. **سناریو:** آموزش تصویری مدیریت `{desc[:25]}...`  
            ۲. **متدولوژی:** میکرولرنینگ تعاملی ۳ دقیقه‌ای  
            ۳. **خروجی جانبی:** بروشور فنی جهت نصب در محل کارگاه  
            """)
            st.balloons()
        else:
            st.error("لطفاً فیلد گزارش را پر کنید.")

# ۶. نوار پایین دقیقاً با متنی که خواستید
st.markdown("""
    <div class="footer-strip">
        مرکز تحقیق و توسعه موسسه عاشورا - مدیریت تولید محتوا
    </div>
""", unsafe_allow_html=True)
