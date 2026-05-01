import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Under Maintenance", page_icon="🏗️", layout="centered")

# CSS Kustom untuk tampilan aesthetic
st.markdown("""
    <style>
    /* Menghilangkan menu default Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Background and Font */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Inter', sans-serif;
    }

    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 80vh;
        text-align: center;
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
    }

    .status-badge {
        background-color: #ffffff;
        padding: 8px 20px;
        border-radius: 50px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        color: #0984e3;
        font-weight: 600;
        font-size: 0.9rem;
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# Konten Halaman
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Emoji atau Ilustrasi
st.markdown('<div class="icon-container">⚙️</div>', unsafe_allow_html=True)

# Judul dan Deskripsi
st.markdown('<div class="title">Sedang Maintenance</div>', unsafe_allow_html=True)
st.markdown('''
    <div class="subtitle">
        Kami sedang melakukan pembaruan sistem untuk memberikan pengalaman yang lebih baik. 
        Mohon tunggu sebentar, kami akan segera kembali!
    </div>
    ''', unsafe_allow_html=True)

# Badge Status
st.markdown('<div class="status-badge">Estimasi Selesai: 2 Jam Lagi</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
