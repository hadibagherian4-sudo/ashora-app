import streamlit as st
import base64
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# تنظیمات پهنای صفحه
st.set_page_config(page_title="سامانه جامع محتوای عاشورا", layout="wide")

# تابع تبدیل عکس به Base64 (لوگو و پس‌زمینه)
def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

bin_bg = get_base64("Picture1.png")
bin_logo = get_base64("official_logo.png")

# --- استایل CSS برای بک‌گراند و دیزاین سازمان ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(255,255,255,0.9), rgba(255,255,255,0.9)), url("data:image/png;base64,{bin_bg}");
        background-size: cover; background-position: center; background-attachment: fixed;
        direction: rtl; text-align: right; font-family: 'Vazirmatn', sans-serif !important;
    }}
    .logo-box {{ position: fixed; top: 10px; right: 25px; z-index: 1001; }}
    .nav-bar {{ position: fixed; top: 0; left: 0; right: 0; height: 75px; background: #0d47a1; z-index: 1000; display: flex; align-items: center; justify-content: center; }}
    .nav-bar h2 {{ color: #ffc107; margin: 0; font-size: 26px; }}
    .main .block-container {{ padding-top: 110px !important; }}
    .stButton>button {{ background: #0d47a1 !important; color: white !important; width: 100%; border-radius: 10px; font-weight: bold; }}
    .content-card {{ background: white; padding: 20px; border-radius: 15px; border-right: 8px solid #ffc107; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-bottom: 20px; text-align: center; }}
</style>
<div class="nav-bar"><h2>سامانه مدیریت محتوای تخصصی موسسه عاشورا</h2></div>
<div class="logo-box"><img src="data:image/png;base64,{bin_logo}" width="100"></div>
""", unsafe_allow_html=True)

# تابع ارسال ایمیل
def send_email(subject_text, body_html):
    # تنظیمات جیمیل شما
    my_email = "hadibagherian4@gmail.com"
    # برای امنیت، باید App Password از گوگل بگیرید (در پایین توضیح داده شده)
    password = "اینجا_رمز_برنامه_را_بگذارید" 
    
    try:
        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = "hadibagherian4@gmail.com"
        msg['Subject'] = "درخواست جدید تولید محتوا: " + subject_text
        
        msg.attach(MIMEText(body_html, 'html'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(my_email, password)
        server.send_msg(msg)
        server.quit()
        return True
    except Exception as e:
        st.error(f"خطا در ارسال: {e}")
        return False

# --- سایدبار برای جابه‌جایی بین بخش‌ها ---
with st.sidebar:
    st.image(f"data:image/png;base64,{bin_logo}" if bin_logo else None, width=150)
    menu = st.radio("بخش مورد نظر:", ["📜 آرشیو محتواهای تولید شده", "🖋️ ثبت درخواست محتوا جدید"])
    st.divider()
    st.info("مرکز تحقیق و توسعه موسسه عاشورا")

# -----------------------------------
# بخش ۱: آرشیو و ویترین محتوا
# -----------------------------------
if menu == "📜 آرشیو محتواهای تولید شده":
    st.header("📚 ویترین آموزش‌های تخصصی موسسه")
    category = st.tabs(["🏗️ فنی و مهندسی", "🦺 HSSE", "💰 عمومی (مالی/اداری)", "💻 IT", "🧠 مدیریت"])

    with category[0]:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="content-card"><h4>فیلم آموزشی روسازی راه</h4><p>استاندارد نشریه ۱۰۱</p><button>مشاهده محتوا</button></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="content-card"><h4>نحوه کار با نرم‌افزار عمرانی</h4><p>تخصصی بخش فنی</p><button>مشاهده محتوا</button></div>', unsafe_allow_html=True)

    with category[1]:
        st.info("محتواهای حوزه ایمنی در این بخش بارگذاری می‌شود...")

# -----------------------------------
# بخش ۲: فرم ثبت درخواست جدید
# -----------------------------------
else:
    st.header("📝 فرم پیشنهاد تولید محتوا تخصصی")
    
    with st.container():
        col_r, col_l = st.columns(2)
        with col_r:
            name = st.text_input("نام و نام خانوادگی متقاضی:")
            phone = st.text_input("شماره تماس همراه:")
            unit = st.selectbox("واحد مربوطه:", ["فنی", "HSSE", "مالی", "نیروی انسانی", "IT", "مدیریت"])
        with col_l:
            title = st.text_input("عنوان پروژه/موضوع:")
            level = st.radio("سطح دسترسی پیشنهادی:", ["عادی", "محرمانه"])
            date = st.date_input("تاریخ پیشنهاد")

        gap = st.text_area("خلاصه شکاف دانشی (کدام مسئله قرار است حل شود؟)")
        
        st.write("الزامات تکنولوژیک:")
        ai = st.checkbox("استفاده از هوش مصنوعی (AI)")
        ar = st.checkbox("واقعیت افزوده (AR/VR)")

    if st.button("🚀 ارسال درخواست به مرکز تولید"):
        if name and phone and gap:
            # آماده سازی محتوای ایمیل
            email_body = f"""
            <html>
            <body dir="rtl">
                <h3>درخواست تولید محتوای جدید از سوی: {name}</h3>
                <p><b>تلفن:</b> {phone}</p>
                <p><b>واحد:</b> {unit}</p>
                <p><b>عنوان موضوع:</b> {title}</p>
                <p><b>شرح مسئله:</b> {gap}</p>
                <hr>
                <p>تکنولوژی ها: AI={ai} | AR={ar}</p>
            </body>
            </html>
            """
            st.toast("در حال ارسال درخواست...")
            # st.success("پیام شما با موفقیت برای مدیریت ارسال شد و در نوبت تولید قرار گرفت.")
            # برای اجرای واقعی ایمیل، فیلد رمز باید پر شود.
            st.info("پیش‌نمایش فرم آماده است. (جهت اتصال به ایمیل شخصی شما، نیاز به تایید نهایی رمز برنامه گوگل است)")
            st.balloons()
        else:
            st.error("لطفاً فیلد نام، شماره تماس و شرح مسئله را پر کنید.")

# فوتر
st.markdown("<hr><div style='text-align:center'>مرکز تحقیق و توسعه موسسه عاشورا - مدیریت تولید محتوا</div>", unsafe_allow_html=True)
