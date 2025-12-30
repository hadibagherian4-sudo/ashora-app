import streamlit as st
import base64
import os

# ۱. تنظیمات اولیه
st.set_page_config(page_title="پورتال جامع محتوای عاشورا", layout="wide")

# ۲. تبدیل تصاویر به کد
def get_base64(path):
    try:
        if os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    except: return ""
    return ""

img_bg = get_base64("Picture1.png")
img_logo = get_base64("official_logo.png")

# ۳. طراحی هنری و خوانا با CSS (اصلاح رنگ های سفید به تیره)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)), url("data:image/png;base64,{img_bg}");
        background-size: cover; background-position: center; background-attachment: fixed;
        direction: rtl; text-align: right; font-family: 'Vazirmatn', sans-serif !important;
    }}
    
    /* لوگو سمت راست بالا */
    .logo-box {{ position: fixed; top: 12px; right: 25px; z-index: 1001; }}
    
    /* هدر سرمه ای */
    .header-nav {{
        position: fixed; top: 0; left: 0; right: 0; height: 75px;
        background: #0d47a1; display: flex; align-items: center; justify-content: center; z-index: 1000;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }}
    .header-nav h2 {{ color: #ffc107 !important; margin: 0; font-weight: 900; font-size: 24px; }}

    .main .block-container {{ padding-top: 110px !important; }}

    /* --- اصلاح رنگ متون به تیره --- */
    h1, h2, h3, h4, p, span, label, div {{
        color: #1a237e !important; /* سرمه ای تیره برای حداکثر خوانایی */
        text-shadow: none !important;
    }}

    /* استایل دکمه انتخاب (تَب ها) */
    .stTabs [data-baseweb="tab-list"] button {{
        background-color: rgba(13, 71, 161, 0.1);
        color: #0d47a1 !important; border-radius: 8px; margin: 5px; font-weight: bold;
    }}
    .stTabs [aria-selected="true"] {{ background-color: #0d47a1 !important; color: #ffc107 !important; }}

    /* کارت‌های بخش آرشیو */
    .archive-card {{
        background: white; border: 1px solid #ddd; border-right: 8px solid #ffc107;
        padding: 25px; border-radius: 15px; margin-bottom: 20px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.1); transition: 0.3s;
    }}
    .archive-card:hover {{ transform: scale(1.01); box-shadow: 0 8px 20px rgba(0,0,0,0.15); }}
    .archive-card h3 {{ color: #0d47a1 !important; margin-top: 0; font-size: 22px; }}
    .archive-card p {{ color: #444 !important; font-size: 15px; }}

    /* استایل فرم ثبت درخواست */
    [data-testid="stForm"] {{
        background-color: white !important; padding: 40px !important;
        border-radius: 20px !important; border: 2px solid #0d47a1 !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1) !important;
    }}

    /* استایل ورودی ها */
    .stTextInput input, .stTextArea textarea {{
        background-color: #f9f9f9 !important; color: #1a237e !important; font-weight: bold !important;
    }}

</style>

<div class="logo-box"><img src="data:image/png;base64,{img_logo}" width="105"></div>
<div class="header-nav"><h2>سامانه بازآفرینی محتوا و مدیریت دانش</h2></div>
""", unsafe_allow_html=True)

# ۴. سایدبار مدیریتی (سمت راست مانیتور)
with st.sidebar:
    st.image(f"data:image/png;base64,{img_logo}" if img_logo else None, width=160)
    st.markdown("<h3 style='color:#0d47a1;'>🧭 میز فرماندهی</h3>", unsafe_allow_html=True)
    mode = st.radio("بخش عملیاتی را انتخاب کنید:", ["📂 آرشیو محتوا (ویترین دانش)", "🖋️ ثبت درخواست تولید جدید"])
    st.divider()
    st.info("تمامی درخواست‌ها توسط واحد تحقیق و توسعه پایش می‌شود.")

# ---------------------------------------------------
# بخش ۱: ویترین و آرشیو یادگیری (📂)
# ---------------------------------------------------
if mode == "📂 آرشیو محتوا (ویترین دانش)":
    st.markdown("<h1 style='text-align: center; color: #0d47a1;'>📚 ویترین دانش و محتواهای تخصصی</h1>", unsafe_allow_html=True)
    st.write("در این بخش به راحتی به تمام آموزش‌های تولید شده در موسسه دسترسی دارید:")
    
    tabs = st.tabs(["🏗️ فنی", "🦺 HSSE", "💻 IT", "💰 عمومی (مالی/اداری)", "🧠 مدیریت"])
    
    with tabs[0]: # بخش فنی
        st.markdown("""
        <div class="archive-card">
            <h3>🎬 استاندارد روسازی راه (نشریه ۱۰۱)</h3>
            <p>این ویدیو شامل ضوابط اجرایی آسفالت و بتن در مناطق سردسیر است.</p>
            <p><b>تاریخ تولید:</b> ۱۴۰۳/۰۹/۱۵ | <b>مدت:</b> ۱۲ دقیقه</p>
        </div>
        <div class="archive-card">
            <h3>🎙️ پادکست مدیریت خاک‌برداری در پروژه‌های کوهستانی</h3>
            <p>نکات کلیدی برای مهندسین کارگاه جهت کاهش هزینه های عملیاتی.</p>
            <p><b>مدرس:</b> مهندس فنی ارشد | <b>قالب:</b> فایل صوتی</p>
        </div>
        """, unsafe_allow_html=True)
        
    with tabs[1]: # بخش HSSE
        st.info("آموزش‌های ایمنی محیط کار در ارتفاع در حال آپلود نهایی است.")

# ---------------------------------------------------
# بخش ۲: فرم ثبت درخواست محتوا (🖋️)
# ---------------------------------------------------
else:
    st.markdown("<h1 style='text-align: center; color: #0d47a1;'>🖋️ مرکز درخواست تولید محتوا تخصصی</h1>", unsafe_allow_html=True)
    st.write("لطفاً مشخصات زیر را وارد کنید تا موضوع آموزشی شما در صف تولید حرفه‌ای قرار گیرد:")

    col_empty1, central_form, col_empty2 = st.columns([0.1, 1, 0.1])
    
    with central_form:
        with st.form("ashora_request_form"):
            r1_c1, r1_c2 = st.columns(2)
            req_name = r1_c1.text_input("👤 نام و نام خانوادگی درخواست دهنده:")
            req_phone = r1_c2.text_input("📞 شماره تماس مستقیم:")
            
            req_unit = st.selectbox("🎯 موضوع متعلق به کدام بخش است؟", ["واحد فنی", "بخش HSSE", "امور مالی", "نیروی انسانی", "مدیریت پروژه"])
            req_topic = st.text_input("📌 عنوان اصلی آموزش مد نظر:")
            req_desc = st.text_area("📄 شرح چالش یا سناریوی پیشنهادی (بسیار مهم):", height=180)
            
            st.markdown("<br>", unsafe_allow_html=True)
            submit_btn = st.form_submit_button("🚀 ثبت نهایی و ارسال برای کارشناسی")
            
            if submit_btn:
                if req_name and req_phone and req_desc:
                    st.success(f"✅ با تشکر جناب {req_name}، درخواست تولید '{req_topic}' با موفقیت در سامانه ثبت و کد رهگیری صادر شد.")
                    st.balloons()
                    st.info("نتیجه بررسی از طریق پیامک یا ایمیل به اطلاع شما خواهد رسید.")
                else:
                    st.warning("⚠️ لطفاً نام، شماره تماس و شرح موضوع را وارد نمایید.")

# ۶. نوار پاورقی پایدار
st.markdown(f"""
    <div style="background-color:#0d47a1; color:#ffc107; padding:20px; text-align:center; border-radius:15px; margin-top:50px; font-weight:bold; border: 2px solid #ffc107;">
        مرکز تحقیق و توسعه موسسه عاشورا - مدیریت تولید محتوای هوشمند
    </div>
""", unsafe_allow_html=True)
