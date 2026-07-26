import streamlit as st

# Konfigurasi Paparan Apps
st.set_page_config(
    page_title="1-Click Content Factory", 
    page_icon="⚡", 
    layout="wide"
)

# Styling Custom (Dark Mode & Kotak Kemas)
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
        color: #f8fafc;
    }
    .stTextInput input, .stTextArea textarea {
        background-color: #1e293b !important;
        color: #f8fafc !important;
        border-radius: 8px;
    }
    .output-box {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #334155;
        margin-bottom: 15px;
        color: #e2e8f0;
    }
    </style>
""", unsafe_allow_html=True)

# Header Utama
st.title("⚡ 1-Click Content Factory")
st.markdown("Hasilkan **Image Prompt (Midjourney), Skrip TikTok, & Copywriting Threads** serentak hanya dengan 1 ayat idea!")

# Sidebar untuk Tetapan AI (Boleh letak API key nanti)
with st.sidebar:
    st.header("⚙️ Tetapan Otak AI")
    ai_model = st.selectbox("Pilih Enjin Otak AI:", ["Gemini Pro (Fast & Smart)", "Claude 3.5 (Deep Storytelling)", "ChatGPT-4o (Direct Response)"])
    api_key = st.text_input("Masukkan API Key (Optional)", type="password", help="Boleh tinggalkan kosong dulu untuk guna mod simulasi pintar.")
    st.markdown("---")
    st.info("💡 **Tips:** Masukkan ayat idea produk atau servis awak di ruangan sebelah, lepas itu tekan butang generate.")

# Ruangan Input Utama
user_idea = st.text_area(
    "Masukkan idea produk / servis / bisnes anda:", 
    placeholder="Contoh: Servis jahit baju kurung custom, dijamin ngam ikut saiz badan dan tak ketat ketiak.",
    height=100
)

# Butang Tindakan
if st.button("🚀 Generate Full Campaign Sekarang", type="primary", use_container_width=True):
    if not user_idea:
        st.warning("⚠️ Sila masukkan idea produk anda terlebih dahulu!")
    else:
        with st.spinner("🤖 Otak AI sedang merangka strategi kempen... Sila tunggu sekejap."):
            
            # Paparan 3 Kolum untuk 3 Output Berbeza
            col1, col2, col3 = st.columns(3)
            
            # OUTPUT 1: IMAGE PROMPT
            with col1:
                st.markdown("### 🎨 1. Image Prompt")
                st.caption("Untuk Midjourney / Flux / Bing")
                
                image_prompt_result = f"Photorealistic high-end commercial shot of {user_idea}, professional studio lighting, rich textures, 85mm lens, cinematic 8k resolution, highly detailed --ar 4:5"
                
                st.markdown(f'''<div class="output-box">
                <b>Prompt (English):</b><br><br>
                <code>{image_prompt_result}</code>
                </div>''', unsafe_allow_html=True)
                
                st.button("📋 Salin Prompt", key="copy1", use_container_width=True)

            # OUTPUT 2: TIKTOK / REELS SCRIPT
            with col2:
                st.markdown("### 🎬 2. Skrip Video")
                st.caption("Format 15-30 Saat (TikTok/Reels)")
                
                st.markdown(f'''<div class="output-box">
                <b>[0-3s] Hook:</b> "Siapa je tak frust kalau beli baju tapi saiz lari?"<br><br>
                <b>[3-15s] Isi:</b> "Sebab tu {user_idea} ni wajib cuba. Ukuran diikut sebiji-sebiji ikut bentuk badan korang."<br><br>
                <b>[15-20s] CTA:</b> "Slot bulan ni sangat terhad. Komen 'NAK' sekarang!"
                </div>''', unsafe_allow_html=True)
                
                st.button("📋 Salin Skrip", key="copy2", use_container_width=True)

            # OUTPUT 3: THREADS / FB COPYWRITING
            with col3:
                st.markdown("### ✍️ 3. Copywriting")
                st.caption("Gaya Borak Santai (Threads/FB)")
                
                st.markdown(f'''<div class="output-box">
                "Jujur cakap, ramai yang buntu bila nak cari pakaian yang betul-betul selesa.<br><br>
                Sebab tu kami perkenalkan <b>{user_idea}</b> ni. Sekali sarung, baru tahu beza selesa dengan tak.<br><br>
                Korang ada masalah sama tak bila beli baju siap kat kedai?"
                </div>''', unsafe_allow_html=True)
                
                st.button("📋 Salin Ayat", key="copy3", use_container_width=True)
                
        st.success("✨ Yay! Kempen berjaya dijana. Sedia untuk digunakan.")

