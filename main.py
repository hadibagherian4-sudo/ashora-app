import streamlit as st
import base64
import os
import smtplib
from email.message import EmailMessage

# ۱. تنظیمات اولیه صفحه
st.set_page_config(page_title="مدیریت محتوا - موسسه عاشورا", layout="wide")

# ۲. تابع تبدیل فایل ها به Base64
def get_base64(path):
    try:
        if os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    except: return ""
    return ""

img_bg = get_base64("Picture1.png")
img_logo = get_base64("official_logo.png")

# ۳. طراحی هنری (فونت B Nazanin، کادر روشن، ویدیو سایز استاندارد)
st.markdown(f"""
<style>
    @font-face {{
        font-family: 'B Nazanin';
        src: local('B Nazanin');
    }}
    
    html, body, [data-testid="stAppViewContainer"], p, span, label, h1, h2, h3, h4 {{
        font-family: 'B Nazanin', 'Tahoma', sans-serif !important;
        direction: rtl; text-align: right;
        color: #1a237e !important;
    }}

    /* تصویر پس‌زمینه کارگاهی */
    [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(255,255,255,0.92), rgba(255,255,255,0.92)), url("data:image/png;base64,{img_bg}");
        background-size: cover; background-position: center; background-attachment: fixed;
    }}

    /* هدر آبی رنگ */
    .header-nav {{
        position: fixed; top: 0; left: 0; right: 0; height: 80px;
        background: #0d47a1; display: flex; align-items: center; justify-content: center; z-index: 1000;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }}
    .header-nav h2 {{ color: #ffc107 !important; margin: 0; font-size: 32px; }}
    
    .logo-top {{ position: fixed; top: 12px; right: 25px; z-index: 1001; width: 100px; }}

    .main .block-container {{ padding-top: 110px !important; }}

    /* سایدبار با تم روشن و فونت خوانا */
    [data-testid="stSidebar"] {{
        background-color: #fcfdfd !important;
        border-left: 2px solid #ddd;
    }}
    [data-testid="stSidebar"] * {{
        color: #0d47a1 !important;
        font-weight: bold !important;
    }}

    /* کارت یادگیری با کلیک - حالت نمایشی */
    .stExpander {{
        border: none !important;
        background: white !important;
        border-radius: 20px !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.07) !important;
        border-right: 12px solid #ffc107 !important;
        margin-bottom: 15px;
    }}
    
    /* سفید کردن کادرهای ورودی ثبت نام */
    input, textarea, select {{
        background-color: white !important;
        color: #1a237e !important;
        border: 2px solid #0d47a1 !important;
        border-radius: 10px !important;
    }}

</style>

<div class="logo-top"><img src="data:image/png;base64,{img_logo}" width="100"></div>
<div class="header-nav"><h2>سامانه مهندسی محتوا و بازآفرینی دانش</h2></div>
""", unsafe_allow_html=True)

# ۴. تابع فنی ارسال جیمیل
def send_professional_email(name, phone, dept, title, script):
    manager_mail = "hadibagherian4@gmail.com"
    app_key = "fekcxbaflmjwmiwl"
    msg = EmailMessage()
    msg['Subject'] = f"🚀 پیشنهاد جدید: {title}"
    msg['From'] = manager_mail
    msg['To'] = manager_mail
    msg.set_content(f"اطلاعات ارسالی:\nنام: {name}\nتلفن: {phone}\nواحد: {dept}\nعنوان: {title}\n\nسناریو:\n{script}")
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(manager_mail, app_key)
            smtp.send_message(msg)
            return True
    except Exception as e: return str(e)

# ۵. طراحی سایدبار روشن
with st.sidebar:
    st.image(f"data:image/png;base64,{img_logo}" if img_logo else None, width=150)
    st.markdown("### 🧭 میز مدیریت محتوا")
    app_mode = st.radio("بخش عملیاتی:", ["📂 ویترین دانش و آرشیو یادگیری", "🖋️ ثبت سناریو جدید"])
    st.divider()

# --- بخش ۱: آرشیو محتوا با سیستم "کلیک و نمایش" ---
if app_mode == "📂 ویترین دانش و آرشیو یادگیری":
    st.markdown("<h2 style='text-align: center;'>📚 کتابخانه چندرسانه‌ای یادگیری هوشمند</h2>", unsafe_allow_html=True)
    st.write("لطفاً بر روی تیتـر آموزش مورد نظر کلیک کنید تا محتوا و ویدیـو نمایش داده شود:")

    tabs = st.tabs(["🏗️ فنی و مهندسی", "🦺 HSSE", "💰 مالی", "🧠 مدیریت"])

    with tabs[0]: # بخش فنی
        # پیاده سازی کلیک روی متن برای نمایش ویدیو
        with st.expander("🎬 🎬 استاندارد روسازی راه (نشریه ۱۰۱) - مشاهده جزییات و فیلم"):
            st.markdown("""
                <h3 style='color:#0d47a1'>ضوابط اجرایی آسفالت و بتن در مناطق سردسیر</h3>
                <p>این ویدیو شامل نکات تخصصی در خصوص درجات حرارت بتن، مواد افزودنی ضدیخ و روش‌های حفاظتی در دماهای بحرانی طبق نشریات مصوب است.</p>
                <hr>
            """, unsafe_allow_html=True)
            
            # کنترل سایز ویدیو با استفاده از ستون ها (ایجاد ستون خالی در کناره ها)
            v_col1, v_col2, v_col3 = st.columns([1, 4, 1])
            with v_col2:
                if os.path.exists("rosazi.mp4"):
                    st.video("rosazi.mp4")
                else:
                    st.error("فایل rosazi.mp4 در گیت‌هاب یافت نشد.")
            st.markdown("<p style='text-align:center;'>تاریخ تولید: ۱۴۰۳/۰۹/۱۵ | زمان: ۱ دقیقه</p>", unsafe_allow_html=True)

    with tabs[1]:
        st.info("محتواهای حوزه ایمنی در ارتفاع در حال تولید نهایی است...")

# --- بخش ۲: ثبت سناریو جدید (مبتنی بر عکس فرم شما) ---
else:
    st.markdown("<h2 style='text-align: center;'>لطفاً محتوا آموزشی درخواستی خود را تکمیل فرمایید. ثبت سناریو تولید محتوا</h2>", unsafe_allow_html=True)
    
    with st.form("professional_request"):
        r1c1, r1c2 = st.columns(2)
        n = r1c1.text_input("👤 نام و نام خانوادگی:")
        p = r1c2.text_input("📞 شماره تماس مستقیم:")
        
        dept = st.selectbox("🎯 واحد سازمانی:", ["فنی و مهندسی", "HSSE", "مالی و منابع انسانی", "ماشین‌آلات"])
        topic = st.text_input("📌 عنوان موضوع آموزشی:")
        script = st.text_area("📄 سناریو پیشنهادی یا شرح کامل چالش (آموزشی):", height=200)
        
        if st.form_submit_button("🚀 تایید نهایی و ارسال به مدیریت تولید محتوا"):
            if n and p and script:
                with st.spinner('در حال برقراری ارتباط با ایمیل...'):
                    res = send_professional_email(n, p, dept, topic, script)
                    if res is True:
                        st.success(f"جناب {n} عزیز، درخواست شما ثبت شد و به زودی بررسی می‌گردد.")
                        st.balloons()
                    else: st.error(f"خطا در ارسال ایمیل: {res}")
            else: st.warning("فیلدهای ضروری را تکمیل کن !")

# ۷. فوتر
st.markdown("<br><hr><div style='text-align:center; padding:15px; background:#0d47a1; color:white; border-radius:15px; font-weight:bold;'>مرکز برنامه ریزی و توسعه موسسه عاشورا - سامانه مدیریت محتوا</div>", unsafe_allow_html=True)
