import streamlit as st
import base64
import os
import smtplib
from email.message import EmailMessage

# ۱. تنظیمات اولیه صفحه
st.set_page_config(page_title="مدیریت دانش - موسسه عاشورا", layout="wide")

# ۲. تابع تبدیل تصاویر به کد جهت استفاده در پس‌زمینه و لوگو
def get_base64(path):
    try:
        if os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    except: return ""
    return ""

img_bg = get_base64("Picture1.png")
img_logo = get_base64("official_logo.png")

# ۳. طراحی شیک و روشن (کادرهای سفید + متن سرمه‌ای تیره)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(255,255,255,0.92), rgba(255,255,255,0.92)), url("data:image/png;base64,{img_bg}");
        background-size: cover; background-position: center; background-attachment: fixed;
        direction: rtl; text-align: right; font-family: 'Vazirmatn', sans-serif !important;
    }}

    /* لوگو ثابت گوشه راست بالا */
    .corner-logo {{ position: fixed; top: 12px; right: 30px; z-index: 1001; width: 105px; filter: drop-shadow(2px 2px 5px rgba(0,0,0,0.2)); }}
    
    /* هدر آبی رنگ سازمان */
    .header-top {{ position: fixed; top: 0; left: 0; right: 0; height: 75px; background: #0d47a1; z-index: 1000; display: flex; align-items: center; justify-content: center; }}
    .header-top h2 {{ color: #ffc107 !important; margin: 0; font-weight: 900; font-size: 26px; }}

    .main .block-container {{ padding-top: 110px !important; }}

    /* --- استایل اجباری فیلدهای روشن و متن تیره --- */
    input, textarea, [data-baseweb="select"] div, .stTextInput div, .stTextArea div {{
        background-color: white !important;
        color: #1a237e !important;
        border: 2px solid #0d47a1 !important;
        border-radius: 12px !important;
        font-weight: bold !important;
    }}
    
    p, span, label, h1, h2, h3, h4 {{ color: #1a237e !important; font-weight: 800 !important; }}

    /* سایدبار روشن */
    [data-testid="stSidebar"] {{ background-color: #fdfdfd !important; border-left: 1px solid #ddd; }}
    [data-testid="stSidebar"] * {{ color: #0d47a1 !important; font-weight: bold !important; }}

    /* کارت های هنری بخش یادگیری */
    .archive-card {{
        background: white; border: 1px solid #e0e0e0; border-right: 12px solid #ffc107;
        padding: 30px; border-radius: 20px; margin-bottom: 25px;
        box-shadow: 0 12px 25px rgba(0,0,0,0.06); transition: 0.3s;
    }}
    .archive-card:hover {{ transform: scale(1.01); box-shadow: 0 15px 35px rgba(0,0,0,0.1); }}
    
    /* پلیرها */
    .stVideo, .stAudio {{ border-radius: 15px; border: 1px solid #0d47a1; overflow: hidden; }}
</style>

<div class="corner-logo"><img src="data:image/png;base64,{img_logo}"></div>
<div class="header-top"><h2>سامانه مدیریت دانش و تولید محتوا</h2></div>
""", unsafe_allow_html=True)

# ۴. تابع فنی ارسال جیمیل
def send_professional_email(name, phone, unit, topic, desc):
    sender_mail = "hadibagherian4@gmail.com"
    app_password = "fekcxbaflmjwmiwl" # رمز ۱۶ رقمی که فعال کردی

    msg = EmailMessage()
    msg['Subject'] = f"🚀 درخواست محتوا: {topic}"
    msg['From'] = sender_mail
    msg['To'] = sender_mail
    msg.set_content(f"اطلاعات فرستنده:\nنام: {name}\nتلفن: {phone}\nواحد: {unit}\n\nشرح سناریو:\n{desc}")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_mail, app_password)
            smtp.send_message(msg)
            return True
    except Exception as e: return str(e)

# ۵. طراحی سایدبار روشن و گویا
with st.sidebar:
    st.image(f"data:image/png;base64,{img_logo}" if img_logo else None, width=160)
    st.markdown("### 🧭 میز عملیاتی")
    app_mode = st.radio("بخش مورد نظر:", ["📂 ویترین یادگیری و آرشیو دانش", "🖋️ ثبت سناریو محتوا"])
    st.divider()
    st.write("موسسه عاشورا - واحد R&D")

# ۶. بخش عملیاتی ۱: آرشیو یادگیری
if app_mode == "📂 ویترین یادگیری و آرشیو دانش":
    st.markdown("<h2 style='text-align: center;'>📚 کتابخانه جامع آموزش‌های تولید شده</h2>", unsafe_allow_html=True)
    st.write("دسته بندی مورد نظر را انتخاب کنید:")

    tabs = st.tabs(["🏗️ فنی و مهندسی", "🦺 HSSE", "💻 IT", "💰 مالی", "🧠 مدیریت"])
    
    with tabs[0]: # بخش فنی
        st.markdown("""
        <div class="archive-card">
            <h3>🎬 ضوابط اجرایی آسفالت و بتن در مناطق سردسیر</h3>
            <p>آموزش تخصصی بر اساس نشریات ۵۰۰ و تجربیات کارگاهی در خصوص نحوه دم‌کردن بتن و افزودنی‌های ضدیخ.</p>
            <p><b>زمان آموزش:</b> 1 دقیقه | <b>موضوع:</b> راهسازی تخصصی</p>
        </div>
        """, unsafe_allow_html=True)
        
        # --- نمایش فیلم rosazi.mp4 ---
        with st.expander("🎞️ برای پخش و مشاهده آنلاین فیلم کلیک کنید"):
            # اگر فایل کنار همین کد در گیت هاب باشد، نامش را مینویسیم:
            if os.path.exists("rosazi.mp4"):
                st.video("rosazi.mp4")
                st.caption("محتوای بازآفرینی شده در مدیریت دانش موسسه")
            else:
                st.error("⚠️ حاجی فیلم rosazi.mp4 توی فایل‌ها پیدا نشد! آپلودش کن توی گیت‌هاب.")

    with tabs[1]:
        st.info("محتواهای ایمنی در مرحله تولید است...")

# ۷. بخش عملیاتی ۲: ثبت درخواست محتوا
else:
    st.markdown("<h2 style='text-align: center;'>لطفاً محتوا آموزشی درخواستی خود را تکمیل فرمایید. ثبت سناریو تولید محتوا</h2>", unsafe_allow_html=True)
    with st.form("pro_form"):
        col_r, col_l = st.columns(2)
        n = col_r.text_input("👤 نام و نام خانوادگی:")
        p = col_l.text_input("📞 شماره تماس مستقیم:")
        u = st.selectbox("🎯 مربوط به کدام بخش است؟", ["واحد فنی", "بخش HSSE", "امور مالی", "نیروی انسانی"])
        t = st.text_input("📌 عنوان موضوع آموزشی:")
        s = st.text_area("📄 سناریوی پیشنهادی یا چالش فنی:", height=200)
        submit_btn = st.form_submit_button("🚀 تایید نهایی و ارسال به ایمیل مدیریت")

    if submit_btn:
        if n and p and s:
            with st.spinner('در حال ثبت و ارسال برای مدیریت...'):
                result = send_professional_email(n, p, u, t, s)
                if result is True:
                    st.success(f"✅ جناب {n}، درخواست شما با موفقیت برای مدیریت ارسال گردید.")
                    st.balloons()
                else: st.error(f"خطا در ارسال: {result}")
        else: st.warning("همه فیلدها را پر کن حاجی!")

# ۸. فوتر
st.markdown("<br><hr><div style='text-align:center; padding:20px; background:#0d47a1; color:white; border-radius:15px; font-weight:bold;'>مرکز تحقیق و توسعه موسسه عاشورا - سامانه بازآفرینی محتوای تخصصی</div>", unsafe_allow_html=True)
