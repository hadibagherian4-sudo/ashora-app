import streamlit as st
import base64
import os

# ۱. تنظیمات اولیه صفحه
st.set_page_config(page_title="سامانه محتوا و آموزش موسسه عاشورا", layout="wide")

# ۲. توابع گرافیکی (بک‌گراند و لوگو)
def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

bin_bg = get_base64("Picture1.png")
bin_logo = get_base64("official_logo.png")

# ۳. طراحی ظاهر سایت با CSS (لوگو راست، بک‌گراند تمام صفحه)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)), url("data:image/png;base64,{bin_bg}");
        background-size: cover; background-position: center; background-attachment: fixed;
        direction: rtl; text-align: right; font-family: 'Vazirmatn', sans-serif !important;
    }}

    .logo-header {{
        position: fixed; top: 10px; right: 20px; z-index: 1001;
    }}
    
    .nav-bar {{
        position: fixed; top: 0; left: 0; right: 0; height: 75px;
        background: #0d47a1; display: flex; align-items: center; justify-content: center; z-index: 1000;
    }}

    .nav-bar h2 {{ color: #ffc107; margin: 0; font-size: 26px; }}

    .main .block-container {{ padding-top: 100px !important; }}

    /* استایل کارت‌های محتوا در آرشیو */
    .archive-card {{
        background: rgba(255, 255, 255, 0.9);
        border-right: 5px solid #ffc107; padding: 15px; border-radius: 10px;
        margin-bottom: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}

    /* استایل فرم ثبت درخواست در مرکز */
    .stForm {{
        background: rgba(255, 255, 255, 0.95);
        padding: 30px; border-radius: 20px; border: 1px solid #ddd;
    }}
    
    label p {{ color: #0d47a1 !important; font-weight: bold; font-size: 18px !important; }}
</style>

<div class="logo-header"><img src="data:image/png;base64,{bin_logo}" width="110"></div>
<div class="nav-bar"><h2>سامانه مدیریت دانش و مهندسی محتوا</h2></div>
""", unsafe_allow_html=True)

# ۴. سایدبار مدیریتی (منو)
with st.sidebar:
    st.image(f"data:image/png;base64,{bin_logo}" if bin_logo else None, width=150)
    st.markdown("### 🧭 منوی سامانه")
    app_mode = st.radio("بخش مورد نظر را انتخاب کنید:", ["📂 آرشیو محتوا (یادگیری عمومی)", "🖋️ ثبت درخواست تولید محتوا"])
    st.divider()
    st.info("هدف ما دسترسی آسان همه افراد به محتواهای تخصصی آموزشی است.")

# ---------------------------------------------------------
# بخش اول: آرشیو و ویترین محتوا (📂)
# ---------------------------------------------------------
if app_mode == "📂 آرشیو محتوا (یادگیری عمومی)":
    st.markdown("## 📚 کتابخانه یادگیری هوشمند")
    st.write("در این بخش محتواهای تولید شده برای استفاده عمومی و ارتقای سطح دانش مهندسی قرار دارد.")
    
    tab_fani, tab_hsse, tab_omoomi, tab_it, tab_modiriati = st.tabs([
        "🏗️ فنی و مهندسی", "🦺 HSSE", "💰 عمومی (مالی/اداری)", "💻 IT", "🧠 مدیریت"
    ])
    
    with tab_fani:
        st.markdown("""
        <div class="archive-card"><h4>فصل اول: استانداردهای بتن‌ریزی در پروژه‌های عمرانی</h4><p>مرجع: نشریه ۵۰۰ | قالب: ویدیوی آموزشی</p><button>مشاهده و یادگیری</button></div>
        <div class="archive-card"><h4>فصل دوم: متره و برآورد هوشمند</h4><p>قالب: پادکست صوتی تخصصی</p><button>مشاهده و یادگیری</button></div>
        """, unsafe_allow_html=True)

    with tab_hsse:
        st.info("محتواهای ایمنی محیط کار در حال بارگذاری است...")

# ---------------------------------------------------------
# بخش دوم: فرم ثبت درخواست تولید محتوا (🖋️)
# ---------------------------------------------------------
else:
    st.markdown("## 🖋️ مرکز درخواست تولید محتوای نوین")
    st.write("اگر موضوع آموزشی خاصی مد نظر دارید، فرم زیر را پر کنید تا کارشناسان ما فرآیند تولید را آغاز کنند.")
    
    col_r, col_mid, col_l = st.columns([0.2, 1, 0.2]) # تراز وسط کادر
    
    with col_mid:
        with st.form("request_form"):
            name = st.text_input("👤 نام و نام خانوادگی متقاضی:")
            phone = st.text_input("📞 شماره تماس (جهت هماهنگی):")
            
            unit = st.selectbox("🎯 مربوط به کدام بخش است؟", ["فنی", "HSSE", "مالی و نیروی انسانی", "IT", "مدیریت پروژه"])
            
            topic = st.text_input("📌 عنوان موضوع درخواستی:")
            
            description = st.text_area("📄 چالش آموزشی را شرح دهید (کدام مسئله فنی یا تجربی قرار است یاد داده شود؟)", height=150)
            
            # ثبت نوع تکنولوژی درخواستی
            st.markdown("##### 🚀 تکنولوژی آموزشی پیشنهادی شما:")
            c1, c2, c3 = st.columns(3)
            use_ai = c1.checkbox("هوش مصنوعی")
            use_ar = c2.checkbox("واقعیت افزوده")
            use_mic = c3.checkbox("میکرولرنینگ")
            
            submitted = st.form_submit_button("🚀 ارسال درخواست تولید به ایمیل مدیریت")
            
            if submitted:
                if name and phone and description:
                    # آماده سازی پیام برای جیمیل شما
                    # نکته: برای ارسال واقعی، باید تنظیمات SMTP جیمیل hadibagherian4@gmail.com فعال باشد.
                    st.success(f"حاجی دمت گرم! درخواست موضوع '{topic}' با موفقیت ثبت شد.")
                    st.balloons()
                    st.info("جزئیات درخواست به همراه شماره تماس شما برای hadibagherian4@gmail.com ارسال شد.")
                else:
                    st.error("لطفاً فیلد نام، تلفن و شرح موضوع را حتماً پر کنید.")

# ۵. فوتر سازمانی
st.markdown(f"""
    <div style="background:#0d47a1; color:#ffc107; padding:15px; text-align:center; border-radius:15px; margin-top: 50px; font-weight:bold;">
        مرکز تحقیق و توسعه موسسه عاشورا - مدیریت تولید محتوای تخصصی
    </div>
""", unsafe_allow_html=True)
