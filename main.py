import streamlit as st
import base64
import os

# ۱. تنظیمات اولیه صفحه (تب بروزر و آیکون)
st.set_page_config(
    page_title="سامانه مهندسی محتوا | موسسه عاشورا",
    layout="wide"
)

# ۲. تابع تبدیل عکس به base64 (برای استفاده در استایل‌های CSS)
def img_to_base64(path):
    try:
        if os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    except:
        return ""
    return ""

bg_base64 = img_to_base64("Picture1.png")
logo_base64 = img_to_base64("official_logo.png")

# ۳. جراحی ظاهر سایت با CSS حرفه‌ای
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');

html, body, [data-testid="stAppViewContainer"] {{
    font-family: 'Vazirmatn', sans-serif !important;
    direction: rtl;
    text-align: right;
}}

/* بک‌گراند کل صفحه با لایه روشن برای خوانایی متن */
[data-testid="stAppViewContainer"] {{
    background-image: linear-gradient(
        rgba(255,255,255,0.85),
        rgba(255,255,255,0.85)
    ), url("data:image/png;base64,{bg_base64}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* نوار سرمه‌ای بالا (هدر ثابت) */
.nav-bar {{
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 75px;
    background-color: #0d47a1;
    z-index: 998;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}}
.nav-bar h2 {{ color: #ffc107; margin: 0; font-size: 28px; }}

/* لوگوی گوشه سمت راست بالا */
.logo-box {{
    position: fixed;
    top: 10px;
    right: 30px;
    z-index: 1001; /* باید بالاتر از هدر باشد */
}}

/* حاشیه کناری بدنه سایت */
.main .block-container {{ padding-top: 110px !important; }}

/* شبکه دکمه‌های هوش مصنوعی */
.ai-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
    margin-top: 30px;
}}

.ai-card {{
    background: #ffffff;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    text-decoration: none !important;
    color: #0d47a1 !important;
    font-weight: bold;
    border-right: 6px solid #ffc107;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transition: 0.3s ease-in-out;
}}
.ai-card:hover {{
    background: #ffc107;
    transform: translateY(-3px);
}}

/* استایل کادر ورود متن (کادر سیاه یا تیره سنتی را روشن‌تر و مدرن می‌کند) */
textarea {{
    border-radius: 10px !important;
    border: 1px solid #ccc !important;
    background-color: rgba(255,255,255,0.8) !important;
}}

</style>

<div class="nav-bar">
    <h2>سامانه مهندسی محتوا</h2>
</div>

<div class="logo-box">
    <img src="data:image/png;base64,{logo_base64}" width="100" style="filter: drop-shadow(2px 2px 5px rgba(0,0,0,0.3));">
</div>
""", unsafe_allow_html=True)

# ۴. تنظیمات و انتخاب‌ها در سایدبار
with st.sidebar:
    st.markdown("### ⚙️ کنترل عملیات")
    unit = st.selectbox("بخش اجرایی:", ["واحد فنی و مهندسی", "HSSE و ایمنی", "امور مالی", "ماشین‌آلات"])
    c_type = st.selectbox("نوع محتوا:", ["کلیپ آموزشی", "پادکست صوتی", "بروشور", "موشن گرافیک"])
    st.write("---")
    st.caption("نسخه توسعه‌یافته برای مدیریت تولید محتوا")

# ۵. ورودی در مرکز سایت
col_side_r, col_mid, col_side_l = st.columns([0.5, 2, 0.5])

with col_mid:
    st.markdown("### 🖋️ مرحله اول: طراحی سناریو")
    topic = st.text_area(
        "چالش مهندسی یا حادثه ایمنی را اینجا شرح دهید:",
        height=180,
        placeholder="جزئیات فنی را اینجا وارد کنید..."
    )

    if st.button("🚀 تایید و نهایی‌سازی سناریو"):
        if topic.strip():
            st.success("✅ سناریوی شما تایید و به واحد هوش مصنوعی ابلاغ شد.")
            st.code(f"نقش: مهندس متخصص موسسه عاشورا\nسناریوی {c_type} در خصوص موضوع '{topic}' در واحد {unit} بر اساس استاندارد نشریات ۵۰۰ گام‌به‌گام طراحی شود.", language="markdown")
            st.balloons()
        else:
            st.error("حاجی، اول باید موضوع رو بنویسی!")

# ۶. بخش دکمه‌های ابزار هوشمند (زیر کادر ورودی)
st.write("---")
st.markdown("### 🤖 مرحله دوم: انتخاب ابزار هوش مصنوعی جهت تولید")
st.markdown("""
<div class="ai-grid">
    <a class="ai-card" href="https://chatgpt.com/" target="_blank">💬 ویرایش متن (ChatGPT)</a>
    <a class="ai-card" href="https://aistudio.google.com/" target="_blank">🧠 تحلیل اسناد (Gemini AI)</a>
    <a class="ai-card" href="https://hailuoai.video/" target="_blank">🎬 تولید فیلم (Hailuo)</a>
    <a class="ai-card" href="https://app.heygen.com/" target="_blank">🎭 ساخت آواتار (HeyGen)</a>
    <a class="ai-card" href="https://elevenlabs.io/" target="_blank">🎙️ شبیه ساز صدا (ElevenLabs)</a>
    <a class="ai-card" href="https://www.canva.com/" target="_blank">🎨 طراحی گرافیک (Canva)</a>
</div>
""", unsafe_allow_html=True)

# ۷. فوتر شیک و پهن
st.markdown("""
<br><br><br>
<div style="background-color:#0d47a1; color:#ffc107; padding:20px; text-align:center; border-radius:15px; font-weight:bold; border: 1px solid #ffc107;">
مرکز تحقیق و توسعه موسسه عاشورا - مدیریت تولید محتوای تخصصی
</div>
""", unsafe_allow_html=True)
