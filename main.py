import streamlit as st
import base64
import os
import smtplib
from email.message import EmailMessage

# ۱. تنظیمات پهنای صفحه
st.set_page_config(page_title="مدیریت دانش - موسسه عاشورا", layout="wide")

# ۲. تابع تبدیل تصاویر
def get_base64(path):
    try:
        if os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    except: return ""
    return ""

img_bg = get_base64("Picture1.png")
img_logo = get_base64("official_logo.png")

# ۳. استایل CSS (جراحی رنگ ها - کادر سفید، متن تیره، منوی روشن)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;900&display=swap');
    
    /* کل بدنه سایت و بک گراند */
    [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(255,255,255,0.92), rgba(255,255,255,0.92)), url("data:image/png;base64,{img_bg}");
        background-size: cover; background-attachment: fixed;
        direction: rtl; text-align: right; font-family: 'Vazirmatn', sans-serif !important;
    }}

    /* لوگو گوشه راست بالا */
    .corner-logo {{ position: fixed; top: 12px; right: 30px; z-index: 1001; width: 100px; }}
    
    /* هدر آبی بالا */
    .header-top {{ position: fixed; top: 0; left: 0; right: 0; height: 75px; background: #0d47a1; z-index: 1000; display: flex; align-items: center; justify-content: center; }}
    .header-top h2 {{ color: #ffc107 !important; margin: 0; font-size: 26px; }}

    .main .block-container {{ padding-top: 110px !important; }}

    /* --- سفید کردن کادرهای ورودی و انتخابی (اجباری) --- */
    input, textarea, select, [data-baseweb="select"] div, [data-baseweb="select"] span {{
        background-color: white !important;
        color: #1a237e !important;
        border: 2px solid #0d47a1 !important;
        font-weight: bold !important;
        border-radius: 8px !important;
    }}
    
    /* متون لیبل و عنوان ها */
    p, span, label, h1, h2, h3, h4 {{
        color: #1a237e !important;
        font-weight: 800 !important;
        text-align: right !important;
    }}

    /* --- روشن کردن کامل منوی سایدبار (بخش قرمز شده) --- */
    [data-testid="stSidebar"] {{
        background-color: #f8f9fa !important;
        border-left: 1px solid #ddd;
    }}
    [data-testid="stSidebar"] * {{
        color: #0d47a1 !important; /* تبدیل نوشته های ناخوانا به آبی تیره */
    }}

    /* دکمه ارسال طلایی */
    .stButton>button {{
        background-color: #ffc107 !important;
        color: #0d47a1 !important;
        font-weight: 900 !important;
        border: 2px solid #0d47a1 !important;
        height: 50px; border-radius: 12px !important;
    }}
</style>

<div class="logo-fixed"><img src="data:image/png;base64,{img_logo}" class="corner-logo"></div>
<div class="header-top"><h2>سامانه مدیریت هوشمند محتوا</h2></div>
""", unsafe_allow_html=True)

# ۴. تابع اصلاح شده ارسال ایمیل (صد در صد عملیاتی)
def send_professional_email(name, phone, unit, topic, desc):
    sender_mail = "hadibagherian4@gmail.com"
    app_password = "fekcxbaflmjwmiwl" # کد 16 رقمی تایید شده شما

    msg = EmailMessage()
    msg['Subject'] = f"🚀 درخواست تولید محتوا: {topic}"
    msg['From'] = sender_mail
    msg['To'] = sender_mail
    msg.set_content(f"درخواست جدید ثبت شد:\n\nنام متقاضی: {name}\nشماره تماس: {phone}\nواحد مربوطه: {unit}\nعنوان: {topic}\n\nشرح سناریو:\n{desc}")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_mail, app_password)
            smtp.send_message(msg)
            return True
    except Exception as e:
        return str(e)

# ۵. طراحی سایدبار روشن
with st.sidebar:
    st.image(f"data:image/png;base64,{img_logo}" if img_logo else None, width=150)
    st.markdown("### 🧭 میز عملیاتی")
    app_mode = st.radio("بخش عملیاتی را انتخاب کنید:", ["📂 آرشیو محتوا", "🖋️ ثبت سناریو محتوا"])
    st.divider()
    st.markdown("<p style='text-align: center;'>مدیریت تولید محتوای تخصصی</p>", unsafe_allow_html=True)

# ۶. بخش اصلی ثبت درخواست
if app_mode == "🖋️ ثبت سناریو محتوا":
    st.markdown("<h2 style='text-align: center;'>لطفاً مشخصات آموزشی درخواستی را تکمیل فرمایید. ثبت سناریو تولید محتوا</h2>", unsafe_allow_html=True)
    
    with st.form("main_form"):
        c1, c2 = st.columns(2)
        n = c1.text_input("👤 نام و نام خانوادگی درخواست دهنده:")
        p = c2.text_input("📞 شماره تماس همراه:")
        
        # کادر انتخابی اصلاح شده
        u = st.selectbox("🎯 انتخاب واحد مربوطه (فنی، مالی، ...):", ["فنی و مهندسی", "HSSE", "مالی و انسانی", "ماشین‌آلات"])
        t = st.text_input("📌 عنوان موضوع آموزشی:")
        d = st.text_area("📄 سناریوی پیشنهادی یا شرح کامل چالش فنی:", height=180)
        
        st.write("")
        submit = st.form_submit_button("🚀 تایید و ارسال نهایی به ایمیل مدیریت")

    if submit:
        if n and p and d:
            with st.spinner('در حال ارسال سناریو به جیمیل مدیریت...'):
                result = send_professional_email(n, p, u, t, d)
                if result is True:
                    st.success("✅ حاجی عالی شد! سناریو با موفقیت ثبت و به ایمیل شما ارسال شد.")
                    st.balloons()
                else:
                    st.error(f"❌ خطا در ارسال! متن خطا: {result}")
        else:
            st.warning("⚠️ کادرها خالیه حاجی! لطفا پرشون کن.")

else:
    st.markdown("### 📚 آرشیو و یادگیری")
    st.info("فایل‌های آموزشی قبلی به زودی در اینجا فعال می‌شوند.")

# ۷. فوتر
st.markdown("<div style='background:#0d47a1; color:#ffc107; padding:15px; text-align:center; border-radius:10px; margin-top:50px; font-weight:bold;'>مرکز تحقیق و توسعه موسسه عاشورا</div>", unsafe_allow_html=True)
