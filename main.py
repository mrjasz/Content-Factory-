import streamlit as st
import google.generativeai as genai

# Konfigurasi Paparan Apps
st.set_page_config(
    page_title="1-Click Content Factory", 
    page_icon="⚡", 
    layout="wide"
)

# Styling Custom (Dark Mode)
st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    .stTextInput input, .stTextArea textarea { background-color: #1e293b !important; color: #f8fafc !important; border-radius: 8px; }
    .output-box { background-color: #1e293b; padding: 20px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 15px; color: #e2e8f0; white-space: pre-wrap; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ 1-Click Content Factory")
st.markdown("Hasilkan **Image Prompt, Skrip TikTok, & Copywriting Threads** serentak mengikut apa sahaja produk/servis anda!")

# Ambil API Key dari Secrets automatik jika ada
secret_key = st.secrets.get("GEMINI_API_KEY", "")

# Sidebar
with st.sidebar:
    st.header("⚙️ Tetapan Otak AI")
    if secret_key:
        st.success("✅ API Key disambung automatik!")
        api_key = secret_key
    else:
        api_key = st.text_input("Masukkan Gemini API Key (Percuma):", type="password", help="Ambil percuma di aistudio.google.com")
        st.markdown("👉 [**Klik Sini Ambil API Key Percuma**](https://aistudio.google.com/app/apikey)")
        st.markdown("---")
        st.info("💡 **Nota:** Masukkan API Key Google jika Secrets belum ditetapkan.")

# Ruang Input
user_idea = st.text_area(
    "Masukkan idea produk / servis anda:", 
    placeholder="Contoh: Servis repair telefon dari rumah ke rumah, tukar skrin, bateri & siap cepat.",
    height=100
)

# Butang Tindakan
if st.button("🚀 Generate Full Campaign Sekarang", type="primary", use_container_width=True):
    if not user_idea:
        st.warning("⚠️ Sila masukkan idea produk / servis anda dulu!")
    elif not api_key:
        st.error("⚠️ Sila masukkan **Gemini API Key** di menu sebelah kiri dulu bro!")
    else:
        with st.spinner("🤖 Otak Gemini AI sedang merangka strategi kempen khas untuk anda..."):
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-2.0-flash')
                
                combined_prompt = f"""
                Tolong jana 3 perkara untuk perniagaan/servis ini: '{user_idea}'

                Formatkan jawapan TEPAT seperti struktur pembahagi di bawah ini tanpa sebarang intro:

                ===IMAGE===
                (Tulis 1 detailed Midjourney image prompt dalam Bahasa Inggeris. Include realistic details, cinematic lighting, 8k. Hanya prompt sahaja.)

                ===SCRIPT===
                (Tulis 1 skrip video TikTok/Reels pendek 15-30 saat dalam Bahasa Melayu santai. Format kemas ada [0-3s] Hook penarik, [3-15s] Isi/Penyelesaian, [15-20s] Call to Action.)

                ===COPY===
                (Tulis 1 ayat copywriting khas Threads/FB dalam Bahasa Melayu santai gaya borak manusia/storytelling. Elakkan hard sell.)
                """

                res = model.generate_content(combined_prompt)
                response_text = res.text

                res_img = "Gagal menjana gambar."
                res_script = "Gagal menjana skrip."
                res_copy = "Gagal menjana copywriting."

                if "===IMAGE===" in response_text and "===SCRIPT===" in response_text and "===COPY===" in response_text:
                    parts = response_text.split("===IMAGE===")[1].split("===SCRIPT===")
                    res_img = parts[0].strip()
                    
                    script_and_copy = parts[1].split("===COPY===")
                    res_script = script_and_copy[0].strip()
                    res_copy = script_and_copy[1].strip()
                else:
                    res_copy = response_text

                # Paparan 3 Kolum
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.markdown("### 🎨 1. Image Prompt")
                    st.caption("Untuk Midjourney / Flux / Bing")
                    st.markdown(f'<div class="output-box">{res_img}</div>', unsafe_allow_html=True)

                with col2:
                    st.markdown("### 🎬 2. Skrip Video")
                    st.caption("Format 15-30 Saat (TikTok/Reels)")
                    st.markdown(f'<div class="output-box">{res_script}</div>', unsafe_allow_html=True)

                with col3:
                    st.markdown("### ✍️ 3. Copywriting")
                    st.caption("Gaya Borak Santai (Threads/FB)")
                    st.markdown(f'<div class="output-box">{res_copy}</div>', unsafe_allow_html=True)

                st.success("✨ Siap! Kempen berjaya dijana secara 100% dinamik.")

            except Exception as e:
                st.error(f"⚠️ Masalah dikesan: {e}")
