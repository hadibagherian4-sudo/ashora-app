import streamlit as st
import base64
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ۱. تنظیمات پهنای صفحه
st.set_page_config(page_title="ثبت سناریو محتوا | موسسه عاشورا", layout="wide")

# ۲. تابع تبدیل تصاویر به کد جهت استفاده در دیزاین
def get_base64(path):
    try:
        if os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    except: return ""
    return ""

img_bg = get_base64("Picture1.png")
img_logo = get_base64("official_logo.png")

# ۳. طراحی شیک، روشن و هنری (CSS سفارشی)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(255,255,255,0.92), rgba(255,255,255,0.92)), url("data:image/png;base64,{img_bg}");
        background-size: cover; background-position: center; background-attachment: fixed;
        direction: rtl; text-align: right; font-family: 'Vazirmatn', sans-serif !important;
    }}

    /* هدر آبی بالا */
    .header-nav {{
        position: fixed; top: 0; left: 0; right: 0; height: 80px;
        background: #0d47a1; display: flex; align-items: center; justify-content: center; z-index: 1000;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }}
    .header-nav h2 {{ color: #ffc107 !important; margin: 0; font-weight: 900; font-size: 26px; }}

    /* لوگو ثابت گوشه راست */
    .logo-fixed {{ position: fixed; top: 12px; right: 30px; z-index: 1001; width: 110px; }}

    .main .block-container {{ padding-top: 110px !important; }}

    /* --- سفید کردن اجباری فیلدها و رنگ تیره متن --- */
    input, textarea, [data-baseweb="select"] div {{
        background-color: white !important;
        color: #0d47a1 !important; /* متن سرمه‌ای تیره */
        border: 2px solid #0d47a1 !important;
        border-radius: 12px !important;
        font-weight: bold !important;
    }}
    
    /* متون برچسب و عناوین */
    h1, h2, h3, h4, p, span, label {{
        color: #1a237e !important;
        font-weight: 900 !important;
        text-shadow: none !important;
    }}

    /* دکمه ارسال طلایی */
    .stButton>button {{
        background-color: #ffc107 !important;
        color: #0d47a1 !important;
        font-weight: 900 !important;
        border: 2px solid #0d47a1 !important;
        border-radius: 12px !important;
        height: 55px;
    }}
    
    /* مخفی سازی المان‌های اضافی استریم‌لیت */
    #MainMenu, footer {{visibility: hidden;}}
</style>

<div class="logo-fixed"><img src="data:image/png;base64,{img_logo}" width="105"></div>
<div class="header-nav"><h2>سامانه مدیریت و تولید محتوا</h2></div>
""", unsafe_allow_html=True)

# ۴. تابع ارسال جیمیل (با رمز عبور از Secrets)
def perform_send_mail(n, p, u, t, s):
    MY_GMAIL = "hadibagherian4@gmail.com"
    try:
        # حاجی رمز رو توی پنل Settings -> Secrets استریم‌لیت با اسم GMAIL_PASS بذار
        PASS = st.secrets["GMAIL_PASS"]
        
        msg = MIMEMultipart()
        msg['From'] = MY_GMAIL
        msg['To'] = MY_GMAIL
        msg['Subject'] = f"New Scenario: {t}"
        
        body = f"فرستنده: {n}\nتلفن: {p}\nواحد: {u}\nعنوان: {t}\n\nشرح سناریو:\n{s}"
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(MY_GMAIL, PASS.replace(" ", "")) # حذف فواصل احتمالی
        server.send_msg(msg)
        server.quit()
        return True
    except Exception as e:
        return str(e)

# ۵. طراحی سایدبار
with st.sidebar:
    st.image(f"data:image/png;base64,{img_logo}" if img_logo else None, width=150)
    st.divider()
    app_page = st.radio("بخش های عملیاتی:", ["🖋️ ثبت سناریو آموزشی جدید", "📂 آرشیو دانش عمومی"])

# ۶. بخش اصلی - فرم درخواست محتوا
if app_page == "🖋️ ثبت سناریو آموزشی جدید":
    # تیتر جدید مطابق درخواست شما
    st.markdown("<h2 style='text-align: center; border-bottom: 2px dashed #ffc107; padding-bottom: 10px;'>لطفاً مشخصات آموزشی را تکمیل فرمایید. ثبت سناریو تولید محتوا</h2>", unsafe_allow_html=True)
    
    with st.form("professional_ashora_form"):
        st.write("")
        c1, c2 = st.columns(2)
        u_name = c1.text_input("👤 نام و نام خانوادگی:")
        u_phone = c2.text_input("📞 شماره تماس همراه:")
        
        u_dept = st.selectbox("🎯 مربوط به واحد اجرایی:", ["واحد فنی و مهندسی", "بخش HSSE و ایمنی", "امور مالی و قراردادها", "مدیریت ماشین‌آلات"])
        u_title = st.text_input("📌 عنوان موضوع پیشنهادی:")
        u_script = st.text_area("📄 متن سناریو یا شرح کامل چالش فنی (آموزشی):", height=200, placeholder="شرح واقعه را اینجا بنویسید...")
        
        st.write("")
        final_submit = st.form_submit_button("🚀 تایید نهایی و ارسال برای مدیریت تولید محتوا")

    if final_submit:
        if u_name and u_phone and u_script:
            with st.spinner('در حال برقراری ارتباط با ایمیل موسسه...'):
                email_status = perform_send_mail(u_name, u_phone, u_dept, u_title, u_script)
                if email_status is True:
                    st.success("✅ عالی شد! سناریوی شما ثبت و برای بررسی علمی ارسال گردید.")
                    st.balloons()
                else:
                    st.error(f"❌ خطا در اتصال به ایمیل. (علت احتمالی: اشتباه بودن رمز ۱۶ رقمی گوگل در Secrets سایت). متن خطا: {email_status}")
        else:
            st.warning("⚠️ حاجی، لطفاً نام، شماره تماس و متن سناریو رو حتماً وارد کن.")

else:
    st.title("📂 ویترین دانش و آرشیو محتوا")
    st.info("فایل‌های آموزشی و ویدیوهای تخصصی موسسه به زودی در این بخش فعال می‌شوند.")

# فوتر (پاورقی)
st.markdown("<br><div style='text-align:center; padding:20px; background:#0d47a1; color:white; border-radius:15px; font-weight:bold;'>واحد تحقیق و توسعه موسسه عاشورا - سامانه بازآفرینی دانش تخصصی</div>", unsafe_allow_html=True)
