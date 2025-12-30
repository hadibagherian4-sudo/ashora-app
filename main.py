import streamlit as st
import base64
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ۱. تنظیمات پهنای صفحه (Wide Mode)
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

# ۳. طراحی هنری و اختصاصی با CSS (سفید کردن فیلدها و نوشته‌های تیره)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(255,255,255,0.88), rgba(255,255,255,0.88)), url("data:image/png;base64,{img_bg}");
        background-size: cover; background-position: center; background-attachment: fixed;
        direction: rtl; text-align: right; font-family: 'Vazirmatn', sans-serif !important;
    }}

    /* لوگو اختصاصی در بالاترین نقطه سمت راست */
    .corner-logo {{
        position: fixed; top: 12px; right: 25px; z-index: 2000;
        width: 105px; filter: drop-shadow(2px 2px 5px rgba(0,0,0,0.3));
    }}

    /* هدر سرمه ای رنگ برند سازمان */
    .header-bar {{
        position: fixed; top: 0; left: 0; right: 0; height: 80px;
        background: #0d47a1; display: flex; align-items: center; justify-content: center; z-index: 1000;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }}
    .header-bar h2 {{ color: #ffc107 !important; margin: 0; font-weight: 900; font-size: 26px; text-shadow: none; }}

    .main .block-container {{ padding-top: 110px !important; }}

    /* --- سفید کردن اجباری فیلدهای ورودی --- */
    div[data-baseweb="input"] input, div[data-baseweb="textarea"] textarea, div[data-baseweb="select"] {{
        background-color: white !important;
        color: #1a237e !important;
        border: 2px solid #0d47a1 !important;
        border-radius: 12px !important;
        font-weight: bold !important;
    }}
    
    /* تنظیم رنگ متن ها به تیره برای خوانایی */
    label, p, h1, h2, h3, h4 {{
        color: #1a237e !important;
        font-weight: 800 !important;
    }}

    /* دکمه ارسال طلایی بزرگ */
    .stButton>button {{
        background-color: #ffc107 !important;
        color: #0d47a1 !important;
        font-weight: 900 !important;
        border: 2px solid #0d47a1 !important;
        height: 60px; font-size: 20px !important; width: 100%; border-radius: 15px !important;
    }}

    /* استایل کارت‌های آرشیو بخش یادگیری */
    .content-card {{
        background: white; border: 1px solid #ddd; border-right: 10px solid #ffc107;
        padding: 25px; border-radius: 15px; margin-bottom: 20px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.1);
    }}
</style>

<div class="logo-fixed"><img src="data:image/png;base64,{img_logo}" class="corner-logo"></div>
<div class="header-bar"><h2>سامانه مدیریت محتوا و آموزش تخصصی موسسه عاشورا</h2></div>
""", unsafe_allow_html=True)

# ۴. تابع ارسال ایمیل
def send_email_v2(u_name, u_phone, u_unit, u_topic, u_script):
    RECIPIENT = "hadibagherian4@gmail.com"
    try:
        PASS = st.secrets["GMAIL_PASS"]
        msg = MIMEMultipart()
        msg['From'] = RECIPIENT
        msg['To'] = RECIPIENT
        msg['Subject'] = f"New Request: {u_topic}"
        body = f"نام: {u_name}\nهمراه: {u_phone}\nواحد: {u_unit}\nموضوع: {u_topic}\n\nسناریو:\n{u_script}"
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(RECIPIENT, PASS.replace(" ", ""))
        server.send_msg(msg)
        server.quit()
        return True
    except Exception as e: return str(e)

# ۵. منوی کناری شیک و روشن
with st.sidebar:
    st.image(f"data:image/png;base64,{img_logo}" if img_logo else None, width=150)
    st.markdown("### 🧭 میز عملیاتی")
    app_mode = st.radio("بخش های سامانه را انتخاب کنید:", ["📂 ویترین یادگیری و آرشیو دانش", "🖋️ ثبت درخواست تولید محتوا"])
    st.divider()
    st.info("هدف: دسترسی آسان پرسنل و جامعه به آموزش‌های تخصصی مهندسی")

# ---------------------------------------------------
# اجرای بخش ۱: آرشیو (پروپیمون)
# ---------------------------------------------------
if app_mode == "📂 ویترین یادگیری و آرشیو دانش":
    st.title("📚 کتابخانه محتواهای تولید شده")
    st.write("در این بخش می‌توانید محتواهای تولید شده در موسسه را مشاهده نموده و یادگیری را آغاز کنید.")
    
    # تَب‌های دسته‌بندی موضوعی
    t1, t2, t3, t4, t5 = st.tabs(["🏗️ فنی و مهندسی", "🦺 HSSE و ایمنی", "💻 IT و هوشمندسازی", "💰 اداری و مالی", "🧠 مدیریتی"])
    
    with t1:
        st.markdown('<div class="content-card"><h3>🎬 فیلم آموزشی روسازی راه (نشریه ۱۰۱)</h3><p>محتوای تخصصی ویژه مهندسین عمران در خصوص اجرای آسفالت پلیمری.</p><button>مشاهده فیلم</button></div>', unsafe_allow_html=True)
    with t2:
        st.markdown('<div class="content-card"><h3>📽️ سناریوی ایمنی کار در ارتفاع</h3><p>آموزش اصول ایمنی نصب داربست و کار در ارتفاع با رعایت پروتکل‌های سپاه.</p></div>', unsafe_allow_html=True)
    with t3:
        st.info("محتواهای حوزه IT به زودی در اینجا لیست می‌شوند...")

# ---------------------------------------------------
# اجرای بخش ۲: فرم درخواست (طبق متن درخواستی شما)
# ---------------------------------------------------
else:
    # تیتر جدید و درشت مطابق درخواست
    st.markdown("<h1 style='text-align: center;'>لطفاً مشخصات آموزشی درخواستی را تکمیل فرمایید. ثبت سناریو تولید محتوا</h1>", unsafe_allow_html=True)
    
    with st.container():
        with st.form("pro_request_form"):
            st.markdown("#### 📝 اطلاعات مورد نیاز :")
            col_a, col_b = st.columns(2)
            u_name = col_a.text_input("👤 نام و نام خانوادگی درخواست دهنده:")
            u_phone = col_b.text_input("📞 شماره تماس همراه:")
            
            u_unit = st.selectbox("🎯 انتخاب واحد مربوطه:", ["واحد فنی", "بخش HSSE", "امور مالی", "نیروی انسانی", "مدیریت پروژه"])
            u_topic = st.text_input("📌 عنوان موضوع آموزشی مد نظر:")
            
            u_script = st.text_area("📄 سناریوی پیشنهادی یا شرح کامل واقعه فنی را اینجا بنویسید:", height=250, placeholder="لطفاً تمام جزئیاتی که نیاز دارید در کلیپ یا پادکست باشد را اینجا قید کنید...")
            
            st.write("")
            submit_form = st.form_submit_button("🚀 تایید و ارسال نهایی برای مدیریت تولید محتوا")

    if submit_form:
        if u_name and u_phone and u_script:
            with st.spinner('در حال برقراری ارتباط با ایمیل hadibagherian4@gmail.com...'):
                res = send_email_v2(u_name, u_phone, u_unit, u_topic, u_script)
                if res is True:
                    st.success("✅ سناریو با موفقیت ثبت شد و اطلاعات برای مدیریت ارسال گردید.")
                    st.balloons()
                else:
                    st.error(f"❌ خطا در ارسال! متن خطا: {res}")
        else:
            st.warning("⚠️ لطفاً نام، تلفن و شرح موضوع را وارد کن.")

# ۶. فوتر سازمانی شیک
st.markdown("<br><hr><div style='text-align:center; padding:15px; background:#0d47a1; color:#ffc107; border-radius:15px; font-weight:bold;'>واحد تحقیق و توسعه موسسه عاشورا - مرکز تولید محتوای تخصصی</div>", unsafe_allow_html=True)
