import streamlit as st
import base64
import os

# ۱. تنظیمات اولیه صفحه
st.set_page_config(page_title="مرکز فرماندهی تولید محتوای هوشمند", layout="wide")

# ۲. تبدیل تصاویر به فرمت Base64 برای استفاده در پس‌زمینه و لوگو
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

# ۳. تزریق CSS برای بک‌گراند کل صفحه، لوگو و استایل‌های مدرن
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
    
    /* پس‌زمینه کل سایت */
    [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)), url("data:image/png;base64,{bin_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* هدر شفاف و لوگو در سمت راست بالا */
    .custom-header {{
        position: fixed;
        top: 0;
        right: 0;
        left: 0;
        height: 100px;
        background: rgba(13, 71, 161, 0.9);
        display: flex;
        justify-content: flex-end;
        align-items: center;
        padding-right: 30px;
        z-index: 1000;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }}
    .header-logo {{
        height: 80px;
        filter: drop-shadow(2px 2px 5px rgba(0,0,0,0.3));
    }}

    /* حذف فاصله بالای سایت به خاطر هدر جدید */
    .block-container {{
        padding-top: 120px !important;
        direction: rtl;
        text-align: right;
    }}

    html, body, p, div, label {{
        font-family: 'Vazirmatn', sans-serif !important;
        color: #0d47a1 !important;
        font-weight: bold;
    }}

    /* استایل دکمه‌های سایت‌های هوش مصنوعی */
    .ai-button {{
        display: block;
        padding: 15px;
        margin: 10px 0;
        background: #ffc107;
        color: #0d47a1 !important;
        text-align: center;
        text-decoration: none;
        border-radius: 15px;
        font-weight: bold;
        transition: 0.3s;
        border: 2px solid #0d47a1;
    }}
    .ai-button:hover {{
        background: #0d47a1;
        color: #ffc107 !important;
        transform: translateY(-3px);
    }}

    .stButton>button {{
        background-color: #2e7d32 !important;
        color: white !important;
        width: 100%;
        border-radius: 12px;
    }}

    </style>
    
    <div class="custom-header">
        <img src="data:image/png;base64,{bin_logo}" class="header-logo">
    </div>
""", unsafe_allow_html=True)

# ۴. سایدبار مدیریتی
with st.sidebar:
    st.markdown("### ⚙️ کنترل پنل واحدها")
    unit = st.selectbox("بخش اجرایی:", ["فنی و مهندسی", "امور مالی", "HSSE", "ماشین‌آلات"])
    st.divider()
    st.write("درگاه تولید دانش سازمانی")

# ۵. محتوای میانی و مرکز فرماندهی
st.title("🛡️ سامانه مهندسی محتوای تخصصی")
st.write("استراتژی تولید دانش بر پایه هوش مصنوعی مولد")

col_main, col_tools = st.columns([1.5, 1])

with col_main:
    st.markdown("### 📝 گام اول: نگارش سناریو")
    # اضافه کردن فیلد انتخاب نوع تولید محتوا
    content_type = st.selectbox("نوع تولید محتوا را انتخاب کنید:", 
                                ["پادکست صوتی (Audio)", "کلیپ ویدیویی (Short Film)", "موشن گرافیک (Motion Graphic)", "کارت پستال / اینفوگرافیک (Card)"])
    
    script_area = st.text_area("سناریو یا متن خام محتوا را وارد کنید:", height=250, 
                              placeholder="مثال: آموزش نکات ایمنی کار در ارتفاع بر اساس نشریات...")

with col_tools:
    st.markdown("### 🤖 گام دوم: تبدیل به رسانه (AI)")
    st.write("با استفاده از لینک‌های زیر، سناریوی خود را به محتوا تبدیل کنید:")
    
    # دکمه‌های متصل به سایت‌های هوش مصنوعی
    st.markdown(f"""
        <a href="https://chatgpt.com/" target="_blank" class="ai-button">💬 ویرایش سناریو (ChatGPT)</a>
        <a href="https://aistudio.google.com/" target="_blank" class="ai-button">✨ تحلیل حرفه‌ای اسناد (Google Studio)</a>
        <a href="https://hailuoai.video/" target="_blank" class="ai-button">🎥 تولید کلیپ حرفه‌ای (Hailuo AI)</a>
        <a href="https://app.heygen.com/" target="_blank" class="ai-button">🗣️ ساخت آواتار سخنگو (HeyGen)</a>
        <a href="https://elevenlabs.io/" target="_blank" class="ai-button">🎙️ تولید پادکست (ElevenLabs)</a>
        <a href="https://www.canva.com/" target="_blank" class="ai-button">🖼️ طراحی کارت پستال (Canva)</a>
    """, unsafe_allow_html=True)

# ۶. نوار پایین (فوتر)
st.markdown("""
    <div style="background-color: #0d47a1; color: #ffc107; padding: 15px; text-align: center; font-weight: bold; border-radius: 15px; margin-top: 50px;">
        مرکز تحقیق و توسعه موسسه عاشورا - مدیریت تولید محتوا
    </div>
""", unsafe_allow_html=True)
