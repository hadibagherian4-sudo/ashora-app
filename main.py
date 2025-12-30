import streamlit as st
import base64
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ۱. تنظیمات پهنای صفحه
st.set_page_config(page_title="سامانه جامع تولید محتوا - موسسه عاشورا", layout="wide")

# ۲. تابع تبدیل تصاویر به کد
def get_base64(path):
    try:
        if os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    except: return ""
    return ""

img_bg = get_base64("Picture1.png")
img_logo = get_base64("official_logo.png")

# ۳. طراحی شیک و هنری با فیلدهای سفید و متن تیره
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(255,255,255,0.88), rgba(255,255,255,0.88)), url("data:image/png;base64,{img_bg}");
        background-size: cover; background-position: center; background-attachment: fixed;
        direction: rtl; text-align: right; font-family: 'Vazirmatn', sans-serif !important;
    }}

    .corner-logo {{
        position: fixed; top: 12px; right: 25px; z-index: 2000;
        width: 105px; filter: drop-shadow(2px 2px 5px rgba(0,0,0,0.3));
    }}

    .header-bar {{
        position: fixed; top: 0; left: 0; right: 0; height: 80px;
        background: #0d47a1; display: flex; align-items: center; justify-content: center; z-index: 1000;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }}
    .header-bar h2 {{ color: #ffc107 !important; margin: 0; font-weight: 900; font-size: 26px; }}

    .main .block-container {{ padding-top: 110px !important; }}

    /* --- سفید کردن اجباری فیلدهای ورودی (رفع مشکل سیاهی کادر) --- */
    input, textarea, [data-baseweb="select"] div, .stTextInput div, .stTextArea div {{
        background-color: white !important;
        color: #1a237e !important;
        border: 2px solid #0d47a1 !important;
        border-radius: 12px !important;
        font-weight: bold !important;
    }}
    
    /* تیره کردن برچسب‌ها و متون برای خوانایی روی سفید */
    label, p, h1, h2, h3, h4, span {{
        color: #1a237e !important;
        font-weight: 800 !important;
    }}

    .stButton>button {{
        background-color: #ffc107 !important;
        color: #0d47a1 !important;
        font-weight: 900 !important;
        border: 2px solid #0d47a1 !important;
        height: 60px; width: 100%; border-radius: 15px !important;
    }}

    .content-card {{
        background: white; border-right: 10px solid #ffc107;
        padding: 25px; border-radius: 15px; margin-bottom: 20px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.1);
    }}
</style>

<div class="logo-fixed"><img src="data:image/png;base64,{img_logo}" class="corner-logo"></div>
<div class="header-bar"><h2>سامانه مدیریت محتوا و آموزش تخصصی موسسه عاشورا</h2></div>
""", unsafe_allow_html=True)

# ۴. تابع اصلاح شده ارسال ایمیل (تطبیق با Secrets گوگل)
def send_email_v2(u_name, u_phone, u_unit, u_topic, u_script):
    MANAGER_EMAIL = "hadibagherian4@gmail.com"
    try:
        # پاکسازی رمز از فاصله احتمالی
        actual_pass = st.secrets["GMAIL_PASS"].replace(" ", "").strip()
        
        # ساخت قالب ایمیل
        msg = MIMEMultipart()
        msg['From'] = MANAGER_EMAIL
        msg['To'] = MANAGER_EMAIL
        msg['Subject'] = f"New Content Request: {u_topic}"
        
        content = f"👤 نام: {u_name}\n📞 تلفن: {u_phone}\n🎯 واحد: {u_unit}\n📌 موضوع: {u_topic}\n\n📝 سناریو:\n{u_script}"
        msg.attach(MIMEText(content, 'plain', 'utf-8'))
        
        # اتصال به سرور (ترتیب صحیح)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(MANAGER_EMAIL, actual_pass) # ورود با رمز ۱۶ رقمی
        server.send_msg(msg)
        server.quit()
        return True
    except Exception as e:
        return str(e)

# ۵. منوی کناری (Sidebar)
with st.sidebar:
    st.image(f"data:image/png;base64,{img_logo}" if img_logo else None, width=150)
    st.markdown("### 🧭 میز عملیاتی")
    app_mode = st.radio("انتخاب بخش:", ["📂 ویترین یادگیری و آرشیو دانش", "🖋️ ثبت سناریو محتوا"])
    st.divider()

# --- بخش ۱: آرشیو محتوا ---
if app_mode == "📂 ویترین یادگیری و آرشیو دانش":
    st.title("📚 کتابخانه محتواهای تولید شده")
    t1, t2, t3, t4, t5 = st.tabs(["🏗️ فنی و مهندسی", "🦺 HSSE", "💻 IT", "💰 اداری و مالی", "🧠 مدیریتی"])
    with t1:
        st.markdown('<div class="content-card"><h3>🎬 استاندارد روسازی راه (نشریه ۱۰۱)</h3><p>محتوای آموزشی اجرای آسفالت و بتن.</p></div>', unsafe_allow_html=True)
    with t2:
        st.markdown('<div class="content-card"><h3>📽️ سناریوی ایمنی کار در ارتفاع</h3><p>ضوابط حفاظتی نصب داربست.</p></div>', unsafe_allow_html=True)

# --- بخش ۲: فرم ثبت سناریو (بخش اصلی شما) ---
else:
    st.markdown("<h1 style='text-align: center;'>لطفاً مشخصات آموزشی درخواستی را تکمیل فرمایید. ثبت سناریو تولید محتوا</h1>", unsafe_allow_html=True)
    
    with st.form("ashora_form"):
        col_a, col_b = st.columns(2)
        u_name = col_a.text_input("👤 نام و نام خانوادگی درخواست دهنده:")
        u_phone = col_b.text_input("📞 شماره تماس همراه:")
        
        u_unit = st.selectbox("🎯 انتخاب واحد مربوطه:", ["واحد فنی", "بخش HSSE", "امور مالی", "نیروی انسانی", "مدیریت پروژه"])
        u_topic = st.text_input("📌 عنوان موضوع آموزشی:")
        u_script = st.text_area("📄 سناریوی پیشنهادی یا شرح کامل چالش فنی:", height=250)
        
        submit_form = st.form_submit_button("🚀 تایید و ارسال نهایی به ایمیل مدیریت")

    if submit_form:
        if u_name and u_phone and u_script:
            with st.spinner('در حال ارسال ایمیل...'):
                res = send_email_v2(u_name, u_phone, u_unit, u_topic, u_script)
                if res is True:
                    st.success("✅  سناریو ثبت و ایمیل ارسال شد.")
                    st.balloons()
                else:
                    st.error(f"❌ خطا! احتمالا پسورد ۱۶ رقمی اشتباه است. متن خطا: {res}")
        else:
            st.warning("⚠️ لطفاً نام، شماره تماس و متن سناریو رو پر کن.")

# ۶. فوتر
st.markdown("<br><hr><div style='text-align:center; font-weight:bold; color:#0d47a1'>واحد تحقیق و توسعه موسسه عاشورا - سامانه مدیریت محتوا</div>", unsafe_allow_html=True)
