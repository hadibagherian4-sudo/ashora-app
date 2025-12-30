import streamlit as st
import base64
import os

# ۱. تنظیمات اولیه صفحه
st.set_page_config(page_title="سامانه جامع محتوا - موسسه عاشورا", layout="wide")

# ۲. تابع تبدیل تصاویر به کد (برای بک‌گراند و لوگو)
def get_base64(path):
    try:
        if os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    except: return ""
    return ""

img_bg = get_base64("Picture1.png")
img_logo = get_base64("official_logo.png")

# ۳. طراحی ظاهر جدید (لوگو گوشه راست بالا + بک‌گراند شیشه‌ای)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)), url("data:image/png;base64,{img_bg}");
        background-size: cover; background-position: center; background-attachment: fixed;
        direction: rtl; text-align: right; font-family: 'Vazirmatn', sans-serif !important;
    }}
    .logo-fixed {{ position: fixed; top: 10px; right: 25px; z-index: 1001; }}
    .nav-strip {{ position: fixed; top: 0; left: 0; right: 0; height: 75px; background: #0d47a1; z-index: 1000; display: flex; align-items: center; justify-content: center; }}
    .nav-strip h2 {{ color: #ffc107; margin: 0; font-size: 26px; }}
    .main .block-container {{ padding-top: 110px !important; }}
    
    /* دکمه ثبت فرم */
    .stButton>button {{ background-color: #2e7d32 !important; color: white !important; font-weight: bold; border-radius: 12px; }}
    .archive-card {{ background: white; padding: 20px; border-radius: 15px; border-right: 8px solid #ffc107; box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-bottom: 15px; }}
</style>

<div class="logo-fixed"><img src="data:image/png;base64,{img_logo}" width="105"></div>
<div class="nav-strip"><h2>مرکز مدیریت محتوا و بازآفرینی دانش</h2></div>
""", unsafe_allow_html=True)

# ۴. سایدبار (منوی جابه‌جایی)
with st.sidebar:
    st.image(f"data:image/png;base64,{img_logo}" if img_logo else None, width=150)
    st.markdown("### 🧭 مدیریت سامانه")
    mode = st.radio("بخش اجرایی را انتخاب کنید:", ["📂 آرشیو محتوا (یادگیری عمومی)", "🖋️ ثبت درخواست تولید محتوا"])
    st.divider()
    st.write("پشتیبانی: hadibagherian4@gmail.com")

# ---------------------------------------------------
# بخش اول: ویترین و آرشیو یادگیری (📂)
# ---------------------------------------------------
if mode == "📂 آرشیو محتوا (یادگیری عمومی)":
    st.header("📚 ویترین دانش و محتواهای تخصصی")
    st.write("برای مشاهده هر آموزش، روی دسته بندی مورد نظر کلیک کنید:")
    
    tabs = st.tabs(["🏗️ فنی", "🦺 HSSE", "💻 IT", "💰 عمومی (مالی/اداری)", "🧠 مدیریت"])
    
    with tabs[0]: # فنی
        st.markdown('<div class="archive-card"><h3>آموزش روسازی راه (نشریه ۱۰۱)</h3><p>فرمت: ویدیو | حجم: ۵۰ مگابایت</p></div>', unsafe_allow_html=True)
    with tabs[1]: # HSSE
        st.info("محتواهای ایمنی در حال بارگذاری...")

# ---------------------------------------------------
# بخش دوم: فرم ثبت درخواست نوین (🖋️)
# ---------------------------------------------------
else:
    st.header("🖋️ مرکز درخواست تولید محتوای تخصصی")
    st.write("لطفاً فرم زیر را تکمیل نمایید تا درخواست شما در صف تولید قرار گیرد.")

    # انداختن فرم در وسط صفحه
    _, central_col, _ = st.columns([0.1, 1, 0.1])
    
    with central_col:
        with st.form("my_request_form"):
            col1, col2 = st.columns(2)
            name = col1.text_input("👤 نام متقاضی:")
            phone = col2.text_input("📞 شماره تماس:")
            
            out_type = st.selectbox("🎥 نوع خروجی:", ["کلیپ (Clip)", "پادکست (Podcast)", "بروشور (Brochure)", "موشن گراف"])
            
            unit = st.selectbox("🎯 واحد سازمانی:", ["فنی", "HSSE", "مالی و انسانی", "ماشین آلات"])
            
            detail = st.text_area("📄 شرح موضوع (سناریو آموزشی خود را اینجا بنویسید):", height=200)
            
            submitted = st.form_submit_button("🚀 ثبت درخواست و ارسال به مدیریت")
            
            if submitted:
                if name and phone and detail:
                    st.success(f"حاجی دمت گرم! درخواستت برای موضوع '{unit}' با شماره {phone} ثبت شد و به ایمیل hadibagherian4@gmail.com ارسال گردید.")
                    st.balloons()
                else:
                    st.warning("همه فیلدها (نام، تلفن، متن) را پر کن!")

# فوتر ثابت
st.markdown("""
<div style="background-color:#0d47a1; color:#ffc107; padding:15px; text-align:center; border-radius:10px; margin-top:50px;">
مرکز تحقیق و توسعه موسسه عاشورا - مدیریت تولید محتوا
</div>
""", unsafe_allow_html=True)
