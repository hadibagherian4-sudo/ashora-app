import gradio as gr
import os

# کدهای CSS اختصاصی برای برندینگ موسسه عاشورا
custom_css = """
body { background-color: #f0f2f5; }
.gradio-container {
    background-image: linear-gradient(rgba(255,255,255,0.88), rgba(255,255,255,0.88)), url('file=Picture1.png');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    direction: rtl;
}
.header-box {
    background: #0d47a1;
    color: #ffc107 !important;
    padding: 20px;
    border-radius: 0 0 30px 30px;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}
.right-logo {
    position: absolute;
    top: 15px;
    right: 25px;
    width: 80px;
    z-index: 1000;
}
.ai-link-btn {
    display: block;
    background: white;
    padding: 15px;
    border-radius: 12px;
    margin: 8px 0;
    text-align: center;
    text-decoration: none;
    color: #0d47a1 !important;
    font-weight: bold;
    border-right: 6px solid #ffc107;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.ai-link-btn:hover { background: #ffc107; }
"""

with gr.Blocks(css=custom_css) as demo:
    # لوگوی گوشه سمت راست
    gr.HTML(f"""
        <div class="logo-area">
            <img src="file=official_logo.png" class="right-logo">
        </div>
        <div class="header-box">
            <h1>🛡️ پلتفرم مهندسی محتوا و بازآفرینی دانش</h1>
        </div>
    """)

    with gr.Row():
        # ستون سمت چپ: تنظیمات و انتخاب‌ها
        with gr.Column(scale=1):
            gr.Markdown("### ⚙️ تنظیمات داشبورد")
            unit = gr.Dropdown(["فنی و مهندسی", "HSSE و ایمنی", "امور مالی", "ماشین‌آلات"], label="بخش اجرایی")
            output = gr.Radio(["کلیپ", "پادکست", "بروشور", "موشن گراف"], label="نوع خروجی")
        
        # ستون وسط (اصلی): کادر نوشتن سناریو
        with gr.Column(scale=2):
            gr.Markdown("### 🖋️ مرحله اول: تدوین سناریو")
            topic = gr.Textbox(label="", placeholder="چالش مهندسی یا حادثه ایمنی را اینجا شرح دهید...", lines=8)
            generate_btn = gr.Button("🚀 تایید و آماده‌سازی برای AI", variant="primary")
            final_output = gr.Code(label="پرامپت نهایی برای تزریق به سایت‌های هوش مصنوعی", interactive=False)

        # ستون سمت راست: میانبر سایت‌های AI
        with gr.Column(scale=1):
            gr.Markdown("### 🤖 مرحله دوم: اتصال به AI")
            gr.HTML("""
                <a href="https://chatgpt.com/" target="_blank" class="ai-link-btn">💬 ChatGPT (متن)</a>
                <a href="https://hailuoai.video/" target="_blank" class="ai-link-btn">🎞️ Hailuo AI (فیلم)</a>
                <a href="https://app.heygen.com/" target="_blank" class="ai-link-btn">🎭 HeyGen (آواتار)</a>
                <a href="https://elevenlabs.io/" target="_blank" class="ai-link-btn">🎙️ ElevenLabs (صدا)</a>
                <a href="https://www.canva.com/" target="_blank" class="ai-link-btn">🎨 Canva (گرافیک)</a>
            """)

    # منطق تولید متن (وقتی دکمه زده بشه)
    def create_prompt(u, o, t):
        if not t: return "حاجی ابتدا شرح واقعه رو بنویس!"
        return f"تو متخصص تولید محتوا در موسسه عاشورا هستی. بر اساس موضوع '{t}'، یک سناریو برای '{o}' واحد '{u}' با استانداردهای نظام فنی طراحی کن."

    generate_btn.click(fn=create_prompt, inputs=[unit, output, topic], outputs=final_output)

    # فوتر سازمان
    gr.HTML("<div style='text-align:center; padding:20px; font-weight:bold; color:#0d47a1'>مرکز تحقیق و توسعه موسسه عاشورا - مدیریت تولید محتوا</div>")

# اجازه دسترسی به فایل‌های تصویر در محیط Gradio
demo.launch(allowed_paths=["Picture1.png", "official_logo.png"])
