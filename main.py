import streamlit as st
import base64
import os

# ۱. تنظیمات اولیه صفحه
st.set_page_config(page_title="داشبورد تولید محتوا - موسسه عاشورا", layout="wide")

# ۲. توابع تبدیل تصاویر (لوگو و بک‌گراند)
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

img_bg = "Picture1.png"
img_logo = "official_logo.png"

bin_bg = get_base64(img_bg)
bin_logo = get_base64(img_logo)

# ۳. تزریق CSS اختصاصی (ترازبندی وسط و ابعاد باکس)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
    
    /* تصویر پس‌زمینه Picture1 */
    [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)), url("data:image/png;base64,{bin_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* لوگو گوشه سمت راست بالا */
    .top-logo-fixed {{
        position: fixed;
        top: 10px;
        right: 20px;
        z-index: 1001;
    }}
    .official-logo {{
        width: 100px;
        filter: drop-shadow(2px 2px 8px rgba(0,0,0,0.2));
    }}

    /* هدر آبی بالا */
    .blue-strip {{
        position: fixed;
        top: 0;
        right: 0;
        left: 0;
        height: 70px;
        background: rgba(13, 71, 161, 0.95);
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }}
    .blue-strip h2 {{
        color: #ffc107 !important;
        font-family: 'Vazirmatn' !important;
        font-size: 26px;
        margin: 0;
    }}

    /* فاصله دادن محتوا از هدر */
    .main .block-container {{
        padding-top: 100px !important;
        direction: rtl;
        text-align: right;
    }}

    /* فونت و رنگ متن ها */
    html, body, p, div, label, span, h3 {{
        font-family: 'Vazirmatn', sans-serif !important;
        color: #0d47a1 !important;
        font-weight: bold;
        text-align: center !important;
    }}

    /* دکمه‌های سایت‌های هوش مصنوعی (ردیفی در مرکز) */
    .ai-tool-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
        margin-top: 20px;
    }}
    
    .ai-btn {{
        padding: 15px;
        background: #ffffff;
        color: #0d47a1 !important;
        text-align: center;
        text-decoration: none !important;
        border-radius: 12px;
        border-right: 6px solid #ffc107;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        font-size: 14px;
        transition: 0.3s;
    }}
    .ai-btn:hover {{
        background: #ffc107;
        transform: translateY(-3px);
    }}
    </style>
    
    <div class="top-logo-fixed">
        <img src="data:image/png;base64,{bin_logo}" class="official-logo">
    </div>
    
    <div class="blue-strip">
        <h2>سامانه مهندسی محتوا</h2>
    </div>
""", unsafe_allow_html=True)

# ۴. پنل سایدبار (بخش اجرایی و خروجی)
with st.sidebar:
    st.markdown("### ⚙️ تنظیمات داشبورد")
    unit = st.selectbox("بخش اجرایی را انتخاب کنید:", 
                        ["واحد فنی و مهندسی", "واحد HSSE و ایمنی", "امور مالی", "ماشین‌آلات"])
    
    output = st.selectbox("نوع خروجی تولیدی:", 
                        ["کلیپ (Clip)", "پادکست (Podcast)", "بروشور", "موشن گراف"])
    st.divider()
    st.info(f"آماده‌سازی سناریوی {output} برای {unit}")

# ۵. چیدمان مرکزی کادر سناریو
st.write("### 🖋️ مرحله اول: تدوین سناریو و شرح واقعه")

# ایجاد ۳ ستون برای انداختن کادر در وسط صفحه
col_side1, col_center, col_side2 = st.columns([1, 2, 1])

with col_center:
    # کوچکتر کردن کادر سیاه با تنظیم height روی ۱۵۰ (قابل تغییر به ۱۰۰ برای کوچکتر شدن)
    scenario_text = st.text_area("چالش مهندسی یا حادثه ایمنی را اینجا شرح دهید:", 
                                 height=150, 
                                 placeholder="شرح جزئیات فنی واقعه...")
    
    confirm_btn = st.button("🚀 تایید و آماده‌سازی نهایی")
    
    if confirm_btn and scenario_text:
        st.success("تحلیل آیین‌نامه‌ای سناریو آماده است. یکی از ابزارهای AI را انتخاب کنید.")

# ۶. بخش ابزارهای هوش مصنوعی (متمرکز در پایین کادر سناریو)
st.write("---")
st.markdown("### 🤖 مرحله دوم: اتصال به موتورهای تولید هوش مصنوعی")

# نمایش دکمه ها در مرکز
c_l, c_m, c_r = st.columns([0.2, 1, 0.2])
with c_m:
    st.markdown(f"""
        <div class="ai-tool-grid">
            <a href="https://chatgpt.com/" target="_blank" class="ai-btn">💬 اصلاح متن (ChatGPT)</a>
            <a href="https://aistudio.google.com/" target="_blank" class="ai-btn">🧠 تحلیل اسناد (Gemini)</a>
            <a href="https://hailuoai.video/" target="_blank" class="ai-btn">🎞️ تولید کلیپ (Hailuo)</a>
            <a href="https://app.heygen.com/" target="_blank" class="ai-btn">🎭 ساخت آواتار (HeyGen)</a>
            <a href="https://elevenlabs.io/" target="_blank" class="ai-btn">🎙️ صداگذاری (ElevenLabs)</a>
            <a href="https://www.canva.com/" target="_blank" class="ai-btn">🎨 گرافیک و بروشور (Canva)</a>
        </div>
    """, unsafe_allow_html=True)

# ۷. نوار پاورقی (فوتر)
st.markdown(f"""
    <div style="background-color: #0d47a1; color: #ffc107; padding: 15px; text-align: center; font-weight: bold; border-radius: 12px; margin-top: 50px;">
        مرکز تحقیق و توسعه موسسه عاشورا - مدیریت تولید محتوا
    </div>
""", unsafe_allow_html=True)
