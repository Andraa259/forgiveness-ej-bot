import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Under Maintenance", page_icon="🏗️", layout="wide")

# CSS Kustom
st.markdown("""
    <style>
    /* 1. Menghilangkan elemen default */
    #MainMenu, footer, header {visibility: hidden;}

    /* 2. MEMBUANG PADDING ATAS STREAMLIT (Sangat Penting) */
    .block-container {
        padding: 0px !important;
    }

    /* 3. Background dan Font */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Inter', sans-serif;
    }

    /* 4. Modifikasi Main Container agar Full Screen & Fixed ke Atas */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh; /* Tinggi penuh layar */
        width: 100vw;  /* Lebar penuh layar */
        text-align: center;
        position: fixed; /* Kunci posisi */
        top: 0;         /* Tempel paling atas */
        left: 0;
        z-index: 9999;
    }

    .icon-container {
        font-size: 80px;
        margin-bottom: 20px;
        animation: float 3s ease-in-out infinite;
    }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }

    .title {
        color: #2d3436;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .subtitle {
        color: #636e72;
        font-size: 1.1rem;
        max-width: 500px;
        line-height: 1.6;
        padding: 0 20px;
    }

    .status-badge {
        background-color: #ffffff;
        padding: 8px 20px;
        border-radius: 50px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        color: #0984e3;
        font-weight: 600;
        font-size: 0.9rem;
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# Konten Halaman (Tetap menggunakan div class yang kamu buat)
st.markdown(f"""
    <div class="main-container">
        <div class="icon-container">⚙️</div>
        <div class="title">Sedang Maintenance</div>
        <div class="subtitle">
            Website sedang melakukan pembaruan sistem supaya lebih membantu. <br>
            Mohon tunggu sebentar, website-nya akan segera kembali!
        </div>
        <div class="status-badge">Estimasi Selesai: Nanti dikasih tau Zuyyi</div>
    </div>
    """, unsafe_allow_html=True)
