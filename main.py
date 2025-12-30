import streamlit as st
import base64
import os
import urllib.parse

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

# ۳. تزریق CSS اختصاصی
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');

    [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)), url("data:image/png;base64,{bin_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

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

    .main .block-container {{
        padding-top: 100px !important;
        direction: rtl;
        text-align: right;
    }}

    html, body, p, div, label, span, h3 {{
        font-family: 'Vazirmatn', sans-serif !important;
        color: #0d47a1 !important;
        font-weight: bold;
        text-align: center !important;
    }}

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
        display: block;
    }}
    .ai-btn:hover {{
        background: #ffc107;
        transform: translateY(-3px);
    }}

    .hint-box {{
        background: rgba(255, 193, 7, 0.18);
        border: 1px dashed rgba(13, 71, 161, 0.45);
        padding: 12px;
        border-radius: 12px;
        margin-top: 10px;
        text-align: right !important;
    }}
    </style>

    <div class="top-logo-fixed">
        <img src="data:image/png;base64,{bin_logo}" class="official-logo">
    </div>

    <div class="blue-strip">
        <h2>سامانه مهندسی محتوا</h2>
    </div>
""", unsafe_allow_html=True)

# --------- ابزار تولید پرامپت ----------
def build_prompt(unit: str, content_type: str, output: str, topic: str, audience: str, duration: str):
    # قالب پایه (بدون “سناریوی پیشنهادی سیستم” و بدون “ثبت جزئیات واقعه”)
    base = f"""
تو یک کارشناس تولید محتوای آموزشی هستی. خروجی باید برای {unit} مناسب باشد.

نوع تولید محتوا: {content_type}
نوع خروجی نهایی: {output}
مخاطب: {audience}
مدت/حجم تقریبی: {duration}

موضوع/سناریوی آموزشی:
{topic}

الزامات:
- لحن: رسمی، آموزشی، دقیق و ساده
- ساختار: تیترهای کوتاه + مراحل اجرایی + نکات کلیدی + چک‌لیست پایانی
- از مثال‌های واقعی محیط کار استفاده کن (بدون نام افراد)
- خروجی باید آماده استفاده در ابزارهای تولید ویدیو/صدا/گرافیک باشد.
""".strip()

    # تخصصی‌سازی بر اساس نوع تولید محتوا
    if content_type == "کلیپ آموزشی":
        extra = """
خروجی مورد نیاز:
1) اسکریپت ویدیو (صحنه به صحنه) با تایم‌کد
2) متن گویندگی (Voice Over)
3) پیشنهاد شات‌ها/تصاویر (B-roll)
4) متن روی تصویر (On-screen text) کوتاه
5) پیشنهاد موسیقی/افکت (اختیاری)
""".strip()
    elif content_type == "پادکست صوتی":
        extra = """
خروجی مورد نیاز:
1) اسکریپت پادکست با شروع جذاب (Hook)
2) متن گویندگی روان و مکالمه‌ای
3) بخش‌بندی: مقدمه، بدنه، جمع‌بندی
4) پیشنهاد افکت/موسیقی (اختیاری)
""".strip()
    elif content_type == "موشن گراف":
        extra = """
خروجی مورد نیاز:
1) سناریوی موشن (صحنه‌ها + تایم‌کد)
2) متن گویندگی
3) عناصر گرافیکی پیشنهادی (آیکن/اینفوگراف/نمودار)
4) متن‌های کوتاه روی صفحه
""".strip()
    else:  # کارت پستال
        extra = """
خروجی مورد نیاز:
1) پیام اصلی بسیار کوتاه و تاثیرگذار
2) 3 شعار جایگزین
3) پیشنهاد تصویر/پس‌زمینه
4) چیدمان متن روی کارت
""".strip()

    return base + "\n\n" + extra


def tool_prompts(master_prompt: str):
    # برای هر ابزار یک راهنمای کوتاه + پرامپت مناسب
    prompts = {
        "ChatGPT (اصلاح و تکمیل متن)": (
            "https://chatgpt.com/",
            master_prompt + "\n\nدر پایان، یک نسخه خیلی کوتاه (TL;DR) هم بده."
        ),
        "Gemini / AI Studio (تحلیل و ساخت سناریو)": (
            "https://aistudio.google.com/",
            master_prompt + "\n\nاگر نیاز به داده/فرض داری، فرض‌های معقول پیشنهاد بده."
        ),
        "Hailuo (تبدیل متن به ویدیو)": (
            "https://hailuoai.video/",
            "Prompt برای Text-to-Video:\n" + master_prompt + "\n\nسبک ویدیو: آموزشی، واقع‌گرایانه، مینیمال، متن روی تصویر کوتاه."
        ),
        "HeyGen (آواتار و ویدیو آموزشی)": (
            "https://app.heygen.com/",
            "Script برای HeyGen (Avatar Video):\n" + master_prompt + "\n\nخروجی: متن گویندگی نهایی + تقسیم‌بندی پاراگرافی برای خوانش."
        ),
        "ElevenLabs (گویندگی/صداگذاری)": (
            "https://elevenlabs.io/",
            "متن آماده برای Voice Over:\n" + master_prompt + "\n\nلطفاً متن گویندگی را کاملاً روان، جمله‌ها کوتاه، قابل خواندن بساز."
        ),
        "Canva (بروشور/کارت/اینفوگراف)": (
            "https://www.canva.com/",
            "متن و ساختار برای طراحی در Canva:\n" + master_prompt + "\n\nخروجی را به بلوک‌های کوچک (عنوان/زیرعنوان/نکته/چک‌لیست) تقسیم کن."
        )
    }
    return prompts


# ۴. پنل سایدبار (بخش اجرایی + نوع تولید محتوا + نوع خروجی)
with st.sidebar:
    st.markdown("### ⚙️ تنظیمات داشبورد")

    unit = st.selectbox(
        "بخش اجرایی را انتخاب کنید:",
        ["واحد فنی و مهندسی", "واحد HSSE و ایمنی", "امور مالی", "ماشین‌آلات"]
    )

    content_type = st.selectbox(
        "نوع تولید محتوا:",
        ["پادکست صوتی", "کلیپ آموزشی", "موشن گراف", "کارت پستال"]
    )

    output = st.selectbox(
        "نوع خروجی:",
        ["کلیپ (Clip)", "پادکست (Podcast)", "بروشور", "موشن گراف"]
    )

    audience = st.selectbox(
        "مخاطب هدف:",
        ["کارگران/اپراتورها", "کارشناسان", "سرپرستان/ناظران", "عمومی"]
    )

    duration = st.selectbox(
        "مدت/حجم تقریبی:",
        ["30-60 ثانیه", "1-2 دقیقه", "2-4 دقیقه", "5-8 دقیقه", "متن کوتاه یک صفحه‌ای"]
    )

    st.divider()
    st.info(f"آماده‌سازی: {content_type} | خروجی: {output} | واحد: {unit}")

# ۵. ورودی مرکزی (بدون ثبت جزئیات واقعه)
st.write("### 🧩 مرحله اول: تعریف موضوع/سناریوی آموزشی")

col_side1, col_center, col_side2 = st.columns([1, 2, 1])

with col_center:
    topic = st.text_area(
        "موضوع یا سناریوی آموزشی را اینجا بنویسید:",
        height=160,
        placeholder="مثال: نحوه ایمن‌سازی محیط کار قبل از تعمیرات، کنترل انرژی (Lockout/Tagout)، یا نکات ایمنی کار با ماشین‌آلات..."
    )

    confirm_btn = st.button("🚀 تولید پرامپت و آماده‌سازی اتصال به ابزارهای AI")

# ۶. تولید پرامپت و اتصال
st.write("---")
st.markdown("### 🤖 مرحله دوم: اتصال به موتورهای تولید هوش مصنوعی")

if confirm_btn:
    if not topic.strip():
        st.error("لطفاً موضوع/سناریوی آموزشی را وارد کنید.")
    else:
        master = build_prompt(unit, content_type, output, topic, audience, duration)
        st.success("پرامپت آماده شد. از پایین، ابزار مدنظر را انتخاب و پرامپت را کپی کنید.")

        st.markdown('<div class="hint-box">✅ نکته: بیشتر سرویس‌ها «پرامپت از طریق لینک» را پشتیبانی نمی‌کنند؛ بهترین روش این است که پرامپت را کپی و در سایت مقصد Paste کنید.</div>', unsafe_allow_html=True)

        st.markdown("#### 📌 پرامپت اصلی (Master Prompt)")
        st.code(master, language="markdown")

        tools = tool_prompts(master)

        # نمایش دکمه‌ها
        c_l, c_m, c_r = st.columns([0.2, 1, 0.2])
        with c_m:
            st.markdown(f"""
                <div class="ai-tool-grid">
                    <a href="{tools['ChatGPT (اصلاح و تکمیل متن)'][0]}" target="_blank" class="ai-btn">💬 ChatGPT</a>
                    <a href="{tools['Gemini / AI Studio (تحلیل و ساخت سناریو)'][0]}" target="_blank" class="ai-btn">🧠 Gemini AI Studio</a>
                    <a href="{tools['Hailuo (تبدیل متن به ویدیو)'][0]}" target="_blank" class="ai-btn">🎞️ Hailuo Video</a>
                    <a href="{tools['HeyGen (آواتار و ویدیو آموزشی)'][0]}" target="_blank" class="ai-btn">🎭 HeyGen</a>
                    <a href="{tools['ElevenLabs (گویندگی/صداگذاری)'][0]}" target="_blank" class="ai-btn">🎙️ ElevenLabs</a>
                    <a href="{tools['Canva (بروشور/کارت/اینفوگراف)'][0]}" target="_blank" class="ai-btn">🎨 Canva</a>
                </div>
            """, unsafe_allow_html=True)

        st.write("")

        st.markdown("#### 🧰 پرامپت مخصوص هر ابزار (کپی کن و داخل سایت Paste کن)")
        tab_names = list(tools.keys())
        tabs = st.tabs(tab_names)
        for i, name in enumerate(tab_names):
            with tabs[i]:
                url, p = tools[name]
                st.write(f"**لینک ابزار:** {url}")
                st.code(p, language="markdown")

# ۷. فوتر
st.markdown("""
    <div style="background-color: #0d47a1; color: #ffc107; padding: 15px; text-align: center; font-weight: bold; border-radius: 12px; margin-top: 50px;">
        مرکز تحقیق و توسعه موسسه عاشورا - مدیریت تولید محتوا
    </div>
""", unsafe_allow_html=True)
