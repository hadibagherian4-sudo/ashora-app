import streamlit as st
import base64
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ۱. تنظیمات صفحه
st.set_page_config(page_title="سامانه هوشمند محتوا | عاشورا", layout="wide")

# ۲. تبدیل تصاویر به Base64 (بسیار مهم برای بک‌گراند و لوگو)
def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

img_bg = get_base64("Picture1.png")
img_logo = get_base64("official_logo.png")

# ۳. طراحی شیک و هنری با متون تیره و پس‌زمینه کارگاهی
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;900&display=swap');
    
    /* تصویر پس‌زمینه کارگاه */
    [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(255,255,255,0.92), rgba(255,255,255,0.92)), url("data:image/png;base64,{img_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        direction: rtl;
        text-align: right;
        font-family: 'Vazirmatn', sans-serif !important;
    }}
    
    /* هدر سفید با مرز سرمه‌ای */
    .nav-strip {{
        position: fixed; top: 0; left: 0; right: 0; height: 80px;
        background: white; border-bottom: 4px solid #0d47a1;
        z-index: 1000; display: flex; align-items: center; justify-content: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }}
    .nav-strip h2 {{ color: #0d47a1 !important; margin: 0; font-weight: 900; }}

    /* لوگو اختصاصی گوشه سمت راست بالا */
    .corner-logo {{
        position: fixed; top: 12px; right: 30px;
        z-index: 1001;
        width: 105px;
        filter: drop-shadow(2px 2px 5px rgba(0,0,0,0.2));
    }}

    .main .block-container {{ padding-top: 110px !important; }}

    /* تنظیم رنگ متون (تیره برای خوانایی روی پس‌زمینه روشن) */
    h1, h2, h3, h4, p, span, label {{ color: #0d47a1 !important; font-weight: bold; }}
    
    /* کارت‌های آرشیو */
    .archive-card {{
        background: #ffffff; border-right: 8px solid #ffc107;
        padding: 20px; border-radius: 15px; margin-bottom: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
    }}
</style>

<div class="logo-fixed"><img src="data:image/png;base64,{img_logo}" class="corner-logo"></div>
<div class="nav-strip"><h2>سامانه مدیریت محتوا و آموزش تخصصی</h2></div>
""", unsafe_allow_html=True)

# ۴. تابع فنی ارسال ایمیل به جیمیل شما
def send_email_to_manager(u_name, u_phone, u_unit, u_topic, u_desc):
    RECIPIENT = "hadibagherian4@gmail.com"
    # برادرم دقت کن رمز ۱۶ رقمی باید در بخش Secrets سایت ذخیره شده باشد
    try:
        PASSWORD = st.secrets["GMAIL_PASS"] 
    except:
        return "ERROR_SECRETS_NOT_SET"

    subject = f"درخواست تولید محتوا: {u_topic}"
    body = f"فرستنده: {u_name}\nتلفن: {u_phone}\nواحد: {u_unit}\nشرح موضوع:\n{u_desc}"

    msg = MIMEMultipart()
    msg['From'] = RECIPIENT
    msg['To'] = RECIPIENT
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(RECIPIENT, PASSWORD)
        server.send_msg(msg)
        server.quit()
        return True
    except Exception as e:
        return str(e)

# ۵. منوی کناری (Sidebar)
with st.sidebar:
    st.image(f"data:image/png;base64,{img_logo}" if img_logo else None, width=150)
    st.markdown("### 🧭 میز عملیاتی")
    mode = st.radio("بخش مورد نظر:", ["📜 ویترین دانش (آموزش عمومی)", "🖋️ درخواست تولید محتوا جدید"])
    st.divider()
    st.info("هدف: یادگیری آسان پرسنل در تمامی حوزه‌ها")

# ---------------------------------------------------
# اجرای بخش‌ها
# ---------------------------------------------------
if mode == "📜 ویترین دانش (آموزش عمومی)":
    st.title("📚 کتابخانه محتواهای تولید شده")
    tabs = st.tabs(["🏗️ فنی", "🦺 HSSE", "💰 عمومی (مالی/اداری)", "💻 IT", "🧠 مدیریت"])
    
    with tabs[0]:
        st.markdown('<div class="archive-card"><h3>🎬 استاندارد روسازی راه (نشریه ۱۰۱)</h3><p>شرح: ضوابط آسفالت در مناطق سردسیر.</p><button>مشاهده فیلم</button></div>', unsafe_allow_html=True)
    with tabs[2]:
        st.markdown('<div class="archive-card"><h3>🎙️ پادکست حسابداری پروژه‌های عمرانی</h3><p>شرح: نحوه ثبت هزینه های جاری کارگاه.</p></div>', unsafe_allow_html=True)
    # بقیه تَب‌ها مشابه پر شوند...

else:
    st.title("🖋️ مرکز ثبت درخواست نوین")
    with st.container():
        st.markdown("#### لطفا مشخصات آموزشی را تکمیل فرمایید:")
        col1, col2 = st.columns(2)
        sender_name = col1.text_input("👤 نام و نام خانوادگی:")
        sender_phone = col2.text_input("📞 شماره تماس:")
        sender_unit = st.selectbox("🎯 مربوط به واحد:", ["فنی", "HSSE", "مالی و اداری", "نیروی انسانی", "IT", "مدیریت"])
        sender_topic = st.text_input("📌 عنوان موضوع آموزشی مد نظر:")
        sender_desc = st.text_area("📄 سناریو یا شرح مسئله فنی:", height=180)
        
        if st.button("🚀 تایید و ارسال نهایی"):
            if sender_name and sender_phone and sender_desc:
                with st.spinner('در حال ارسال ایمیل به مدیریت...'):
                    res = send_email_to_manager(sender_name, sender_phone, sender_unit, sender_topic, sender_desc)
                    if res is True:
                        st.success("✅ حاجی دمت گرم! درخواستت با موفقیت ثبت و به ایمیل مدیریت ارسال شد.")
                        st.balloons()
                    elif res == "ERROR_SECRETS_NOT_SET":
                        st.error("خطا: رمز ۱۶ رقمی در تنظیمات Secrets سایت وارد نشده است.")
                    else:
                        st.error(f"خطا در ارسال: {res}")
            else:
                st.warning("همه فیلدها را پر کن.")

# ۶. نوار پایین
st.markdown("<div style='background:#0d47a1; color:#ffc107; padding:15px; text-align:center; border-radius:10px; margin-top:50px; font-weight:bold;'>مرکز تحقیق و توسعه موسسه عاشورا</div>", unsafe_allow_html=True)
