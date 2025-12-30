import streamlit as st
import base64
import os

# ۱. تنظیمات صفحه
st.set_page_config(
    page_title="سامانه مهندسی محتوا | موسسه عاشورا",
    layout="wide"
)

# ۲. ابزار تبدیل عکس به base64 (با قابلیت هندل کردن خطای نبود عکس)
def img_to_base64(path):
    try:
        if os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    except Exception as e:
        return ""
    return ""

bg_img = img_to_base64("Picture1.png")
logo_img = img_to_base64("official_logo.png")

# ۳. CSS (بهینه‌سازی شده)
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');

html, body, [data-testid="stAppViewContainer"] {{
    font-family: 'Vazirmatn', sans-serif;
    direction: rtl;
    text-align: right;
}}

/* بک‌گراند */
[data-testid="stAppViewContainer"] {{
    background-image: linear-gradient(rgba(255,255,255,0.92), rgba(255,255,255,0.92)), url("data:image/png;base64,{bg_img}");
    background-size: cover;
    background-attachment: fixed;
}}

/* هدر ثابت */
.header {{
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 70px;
    background: #0d47a1;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 999;
}}

.header h2 {{ color: #ffc107; margin: 0; }}

/* لوگو سمت راست بالا */
.logo {{ position: fixed; top: 10px; right: 20px; z-index: 1000; }}

.main .block-container {{ padding-top: 100px; }}

/* دکمه‌های ابزارها */
.ai-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
    margin-top: 20px;
}}

.ai-btn {{
    background: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    text-decoration: none !important;
    color: #0d47a1 !important;
    font-weight: bold;
    border-right: 8px solid #ffc107;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}}
.ai-btn:hover {{ background: #ffc107; transform: translateY(-3px); transition: 0.3s; }}
</style>

<div class="header">
    <h2>سامانه مهندسی محتوا</h2>
</div>

<div class="logo">
    <img src="data:image/png;base64,{logo_img}" width="90">
</div>
""", unsafe_allow_html=True)

# ۴. بخش ورودی و تولید سناریو (در مرکز)
col_r, col_c, col_l = st.columns([1, 2, 1])

with col_c:
    st.markdown("### ✏️ گام اول: تدوین سناریو آموزشی")
    
    # دریافت تنظیمات از سایدبار
    with st.sidebar:
        st.header("⚙️ تنظیمات داشبورد")
        unit = st.selectbox("بخش اجرایی:", ["واحد فنی و مهندسی", "HSSE و ایمنی", "امور مالی", "ماشین‌آلات"])
        c_type = st.selectbox("نوع محتوا:", ["کلیپ آموزشی", "پادکست صوتی", "بروشور", "موشن گرافیک"])
        st.divider()

    topic = st.text_area(
        "چالش مهندسی یا حادثه ایمنی را اینجا شرح دهید:",
        height=150,
        placeholder="جزئیات فنی را اینجا بنویسید..."
    )

    if st.button("🚀 تولید پرامپت و نهایی‌سازی"):
        if topic:
            st.success("پرامپت برای ابزارهای هوش مصنوعی آماده شد!")
            st.code(f"تو یک مهندس ارشد موسسه عاشورا هستی. سناریوی {c_type} برای واحد {unit} در مورد '{topic}' طراحی کن.", language="markdown")
            st.balloons()
        else:
            st.warning("لطفاً ابتدا موضوع را شرح دهید.")

# ۵. ابزارهای هوش مصنوعی
st.write("---")
st.markdown("### 🤖 گام دوم: تبدیل به رسانه (هوش مصنوعی)")
st.markdown("""
<div class="ai-grid">
    <a class="ai-btn" href="https://chatgpt.com/" target="_blank">💬 ویرایش متن (ChatGPT)</a>
    <a class="ai-btn" href="https://aistudio.google.com/" target="_blank">🧠 تحلیل اسناد (Gemini)</a>
    <a class="ai-btn" href="https://hailuoai.video/" target="_blank">🎬 تولید ویدیو (Hailuo)</a>
    <a class="ai-btn" href="https://app.heygen.com/" target="_blank">🎭 ساخت آواتار (HeyGen)</a>
    <a class="ai-btn" href="https://elevenlabs.io/" target="_blank">🎙️ تولید صدا (ElevenLabs)</a>
    <a class="ai-btn" href="https://www.canva.com/" target="_blank">🎨 گرافیک (Canva)</a>
</div>
""", unsafe_allow_html=True)

# ۶. فوتر
st.markdown(f"""
<br><br>
<div style="background:#0d47a1; color:#ffc107; padding:15px; text-align:center; border-radius:10px; font-weight:bold;">
مرکز تحقیق و توسعه موسسه عاشورا - مدیریت تولید محتوا
</div>
""", unsafe_allow_html=True)
