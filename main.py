import streamlit as st
import base64
import os

# ----------------------------
# تنظیمات صفحه
# ----------------------------
st.set_page_config(
    page_title="سامانه مهندسی محتوا | موسسه عاشورا",
    layout="wide"
)

# ----------------------------
# ابزار تبدیل عکس به base64
# ----------------------------
def img_to_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

bg_img = img_to_base64("Picture1.png")
logo_img = img_to_base64("official_logo.png")

# ----------------------------
# CSS
# ----------------------------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');

html, body {{
    font-family: 'Vazirmatn', sans-serif;
}}

[data-testid="stAppViewContainer"] {{
    background-image: linear-gradient(
        rgba(255,255,255,0.9),
        rgba(255,255,255,0.9)
    ), url("data:image/png;base64,{bg_img}");
    background-size: cover;
}}

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

.header h2 {{
    color: #ffc107;
    margin: 0;
}}

.logo {{
    position: fixed;
    top: 10px;
    right: 20px;
    z-index: 1000;
}}

.main .block-container {{
    padding-top: 100px;
    direction: rtl;
    text-align: right;
}}

.ai-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
}}

.ai-btn {{
    background: white;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    text-decoration: none;
    color: #0d47a1;
    font-weight: bold;
    border-right: 6px solid #ffc107;
}}
.ai-btn:hover {{
    background: #ffc107;
}}
</style>

<div class="header">
    <h2>سامانه مهندسی محتوا</h2>
</div>

<div class="logo">
    <img src="data:image/png;base64,{logo_img}" width="90">
</div>
""", unsafe_allow_html=True)

# ----------------------------
# تابع ساخت پرامپت
# ----------------------------
def make_prompt(unit, content_type, output_type, topic):
    return f"""
تو یک متخصص تولید محتوای آموزشی هستی.

بخش اجرایی: {unit}
نوع تولید محتوا: {content_type}
نوع خروجی: {output_type}

موضوع آموزشی:
{topic}

خروجی باید:
- آموزشی، واضح و کاربردی باشد
- مناسب استفاده در ابزارهای هوش مصنوعی باشد
- ساختارمند و مرحله‌بندی شده باشد
""".strip()

# ----------------------------
# سایدبار
# ----------------------------
with st.sidebar:
    st.markdown("### ⚙️ تنظیمات")

    unit = st.selectbox(
        "بخش اجرایی:",
        ["واحد فنی و مهندسی", "HSSE و ایمنی", "امور مالی", "ماشین‌آلات"]
    )

    content_type = st.selectbox(
        "نوع تولید محتوا:",
        ["کلیپ آموزشی", "پادکست صوتی", "موشن گراف", "کارت پستال"]
    )

    output_type = st.selectbox(
        "نوع خروجی:",
        ["کلیپ", "پادکست", "بروشور", "موشن گراف"]
    )

# ----------------------------
# ورودی اصلی
# ----------------------------
st.markdown("### ✏️ مرحله اول: تعریف موضوع آموزشی")

topic = st.text_area(
    "موضوع یا سناریوی آموزشی:",
    height=160,
    placeholder="مثال: اصول ایمنی هنگام تعمیر ماشین‌آلات صنعتی"
)

generate = st.button("🚀 تولید پرامپت")

# ----------------------------
# خروجی
# ----------------------------
if generate:
    if not topic.strip():
        st.error("لطفاً موضوع آموزشی را وارد کنید.")
    else:
        prompt = make_prompt(unit, content_type, output_type, topic)

        st.success("پرامپت آماده شد")

        st.markdown("### 📌 پرامپت نهایی")
        st.code(prompt, language="markdown")

        st.markdown("### 🤖 اتصال به ابزارهای هوش مصنوعی")
        st.markdown("""
        <div class="ai-grid">
            <a class="ai-btn" href="https://chatgpt.com/" target="_blank">💬 ChatGPT</a>
            <a class="ai-btn" href="https://aistudio.google.com/" target="_blank">🧠 Gemini AI</a>
            <a class="ai-btn" href="https://hailuoai.video/" target="_blank">🎬 Hailuo Video</a>
            <a class="ai-btn" href="https://app.heygen.com/" target="_blank">🎭 HeyGen</a>
            <a class="ai-btn" href="https://elevenlabs.io/" target="_blank">🎙️ ElevenLabs</a>
            <a class="ai-btn" href="https://www.canva.com/" target="_blank">🎨 Canva</a>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------
# فوتر
# ----------------------------
st.markdown("""
<hr>
<div style="text-align:center; font-weight:bold; color:#0d47a1">
مرکز تحقیق و توسعه موسسه عاشورا
</div>
""", unsafe_allow_html=True)
