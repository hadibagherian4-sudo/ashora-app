import streamlit as st
import base64
import os

# ۱. تنظیمات اولیه صفحه
st.set_page_config(page_title="سامانه مدیریت محتوای عاشورا", layout="wide")

# ۲. توابع تبدیل فایل به Base64
def get_base64(path):
    try:
        if os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    except: return ""
    return ""

img_bg = get_base64("Picture1.png")
img_logo = get_base64("official_logo.png")

# ۳. طراحی شیک و روشن (Light UI) با متون تیره
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;900&display=swap');
    
    /* پس‌زمینه اصلی با لایه بسیار روشن */
    [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(255,255,255,0.92), rgba(255,255,255,0.92)), url("data:image/png;base64,{img_bg}");
        background-size: cover; background-position: center; background-attachment: fixed;
        direction: rtl; text-align: right; font-family: 'Vazirmatn', sans-serif !important;
    }}
    
    /* لوگو ثابت در موقعیت طلایی */
    .logo-box {{ position: fixed; top: 12px; right: 25px; z-index: 1001; }}
    
    /* نوار هدر (روشن) */
    .header-nav {{
        position: fixed; top: 0; left: 0; right: 0; height: 75px;
        background: #ffffff; display: flex; align-items: center; justify-content: center; z-index: 1000;
        box-shadow: 0 2px 15px rgba(0,0,0,0.1);
        border-bottom: 3px solid #0d47a1;
    }}
    .header-nav h2 {{ color: #0d47a1 !important; margin: 0; font-weight: 900; font-size: 24px; }}

    .main .block-container {{ padding-top: 110px !important; }}

    /* --- استایل منوی کناری (روشن شد) --- */
    [data-testid="stSidebar"] {{
        background-color: #f8f9fa !important;
        border-left: 1px solid #e0e0e0;
    }}
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label {{
        color: #0d47a1 !important; /* متن های تیره در کادر روشن */
        font-weight: bold !important;
    }}

    /* --- رنگ متون کل سایت (تیره برای خوانایی عالی) --- */
    h1, h2, h3, h4, p, span, label {{
        color: #1a237e !important; 
    }}

    /* کارت‌های بخش آرشیو (سفید و هنری) */
    .archive-card {{
        background: #ffffff; 
        border: 1px solid #eee; 
        border-right: 10px solid #ffc107;
        padding: 30px; border-radius: 20px; margin-bottom: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05); 
        transition: 0.3s;
    }}
    .archive-card:hover {{ 
        transform: translateY(-5px); 
        box-shadow: 0 15px 30px rgba(0,0,0,0.1); 
    }}
    
    /* پلیرهای فیلم و صوت */
    .stVideo, .stAudio {{
        border-radius: 15px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }}
    
    /* استایل تَب ها (روشن) */
    .stTabs [data-baseweb="tab-list"] button {{
        background-color: transparent;
        color: #444 !important; border-radius: 10px; margin: 5px; font-weight: bold;
    }}
    .stTabs [aria-selected="true"] {{ 
        background-color: #0d47a1 !important; color: #fff !important; 
    }}
    
    /* فوتر نواری پایین */
    .footer-band {{
        background-color: #0d47a1; color: white !important; 
        padding: 15px; text-align: center; border-radius: 12px; margin-top: 60px;
        font-weight: bold; font-size: 15px;
    }}
</style>

<div class="logo-box"><img src="data:image/png;base64,{img_logo}" width="100"></div>
<div class="header-nav"><h2>سامانه مدیریت هوشمند محتوا</h2></div>
""", unsafe_allow_html=True)

# ۴. منوی کناری (روشن)
with st.sidebar:
    st.image(f"data:image/png;base64,{img_logo}" if img_logo else None, width=150)
    st.markdown("### 🧭 میز عملیاتی")
    app_mode = st.radio("بخش مورد نظر:", ["📜 آرشیو و یادگیری", "🖋️ ثبت درخواست جدید"])
    st.divider()
    st.markdown("<p style='font-size: 0.9em; opacity: 0.7;'>واحد مدیریت محتوای تخصصی</p>", unsafe_allow_html=True)

# ---------------------------------------------------
# بخش ۱: آرشیو محتوا (تَب های روشن)
# ---------------------------------------------------
if app_mode == "📜 آرشیو و یادگیری":
    st.markdown("<h1 style='text-align: center;'>📚 ویترین دانش و آموزش‌های موسسه</h1>", unsafe_allow_html=True)
    st.write("---")
    
    tabs = st.tabs(["🏗️ فنی", "🦺 HSSE", "💰 اداری/مالی", "💻 IT", "🧠 مدیریت"])
    
    with tabs[0]: # فنی
        # کارت فیلم آموزشی
        st.markdown("""
        <div class="archive-card">
            <h3>🎬 استاندارد روسازی راه (نشریه ۱۰۱)</h3>
            <p style='color: #555 !important;'>شرح: آموزش ضوابط آسفالت ریزی در مناطق سردسیر بر اساس استانداردهای بین‌المللی راهسازی.</p>
            <p><b>⏱️ مدت زمان:</b> 1 دقیقه | <b>تاریخ:</b> آذر ۱۴۰۳</p>
        </div>
        """, unsafe_allow_html=True)
        
        # پلیر ویدیو
        with st.expander("🎞️ مشاهده آنلاین ویدیو آموزشی"):
            st.video("https://www.w3schools.com/html/mov_bbb.mp4") # حاجی لینک فیلم خودت رو اینجا بذار

        st.write("---")
        
        # کارت پادکست
        st.markdown("""
        <div class="archive-card">
            <h3>🎙️ مدیریت خاک‌برداری در پروژه‌های کوهستانی</h3>
            <p style='color: #555 !important;'>نکات عملیاتی ویژه مدیران پروژه برای بهینه سازی عملیات خاکی در زمین های سخت.</p>
            <p><b>🎙️ مدرس:</b> مهندسی ارشد فنی | <b>قالب:</b> فایل صوتی</p>
        </div>
        """, unsafe_allow_html=True)
        
        # پلیر صوتی
        with st.expander("🎵 پخش پادکست صوتی"):
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

    with tabs[1]:
        st.info("محتواهای ایمنی در حال تدوین است...")

# ---------------------------------------------------
# بخش ۲: فرم درخواست (روشن)
# ---------------------------------------------------
else:
    st.markdown("<h1 style='text-align: center;'>🖋️ فرم ثبت درخواست تولید محتوا</h1>", unsafe_allow_html=True)
    
    with st.form("light_form"):
        st.markdown("<h4 style='color:#0d47a1;'>لطفاً اطلاعات زیر را تکمیل فرمایید:</h4>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        name = col1.text_input("👤 نام و نام خانوادگی:")
        phone = col2.text_input("📞 شماره تماس:")
        
        unit_type = st.selectbox("🎯 انتخاب واحد مربوطه:", ["فنی", "HSSE", "اداری و مالی", "مدیریت پروژه"])
        content_topic = st.text_input("📌 عنوان موضوع آموزشی مد نظر:")
        content_detail = st.text_area("📄 شرح چالش فنی یا سناریو پیشنهادی:", height=180)
        
        submitted = st.form_submit_button("🚀 ثبت درخواست و ارسال به مدیریت")
        
        if submitted:
            if name and phone and content_detail:
                st.success("درخواست شما با موفقیت ثبت شد و به زودی با شما تماس می‌گیریم.")
                st.balloons()
            else:
                st.error("لطفاً فیلد های ستاره‌دار را تکمیل کنید.")

# ۶. فوتر ثابت روشن-سرمه‌ای
st.markdown("""
    <div class="footer-band">
        مرکز تحقیق و توسعه موسسه عاشورا - واحد تولید محتوای تخصصی
    </div>
""", unsafe_allow_html=True)
