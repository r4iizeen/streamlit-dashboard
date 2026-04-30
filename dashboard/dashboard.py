import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ========================
# CONFIG
# ========================
st.set_page_config(
    page_title="Air Quality Dashboard",
    layout="wide"
)

FIG_SIZE = (4, 3)
DPI = 120

# ========================
# LOAD DATA
# ========================
@st.cache_data
def load_data():
    file_id = "18SJfGBNBEviWArMvZ7l6gH4bM5mIXtX1"
    url = f"https://drive.google.com/uc?id={file_id}"
    df = pd.read_csv(url)
    return df

df = load_data()

# ========================
# TITLE
# ========================
st.title("Air Quality Dashboard (Beijing 2013–2017)")
st.caption("Analisis tren PM2.5 dan pengaruh faktor cuaca")

# ========================
# SIDEBAR FILTER
# ========================
st.sidebar.header("Filter")

stations = st.sidebar.multiselect(
    "Pilih Stasiun",
    options=sorted(df['station'].unique()),
    default=sorted(df['station'].unique())
)

year_min, year_max = int(df['year'].min()), int(df['year'].max())
year_range = st.sidebar.slider(
    "Rentang Tahun",
    year_min, year_max, (year_min, year_max)
)

df_filtered = df[
    (df['station'].isin(stations)) &
    (df['year'].between(year_range[0], year_range[1]))
].copy()

# ========================
# KPI
# ========================
k1, k2, k3 = st.columns(3)
k1.metric("Avg PM2.5", f"{df_filtered['PM2.5'].mean():.2f}")
k2.metric("Max PM2.5", f"{df_filtered['PM2.5'].max():.2f}")
k3.metric("Min PM2.5", f"{df_filtered['PM2.5'].min():.2f}")

st.divider()

# ========================
# TREND (Pertanyaan 1)
# ========================
st.subheader("Trend PM2.5 per Tahun")

pm25_year = df_filtered.groupby('year')['PM2.5'].mean()

fig1, ax1 = plt.subplots(figsize=FIG_SIZE, dpi=DPI)
ax1.plot(pm25_year.index, pm25_year.values, marker='o')
ax1.set_xlabel("Tahun")
ax1.set_ylabel("PM2.5")
ax1.grid(alpha=0.3)
st.pyplot(fig1)

tahun_tertinggi = pm25_year.idxmax()

st.info(f"Tingkat PM2.5 tertinggi terjadi pada tahun {tahun_tertinggi}")

st.divider()

# ========================
# PENGARUH CUACA (Pertanyaan 2)
# ========================
st.subheader("Pengaruh Variabel Cuaca terhadap PM2.5")

c1, c2, c3 = st.columns(3)

# TEMP
with c1:
    st.markdown("**Suhu (TEMP)**")
    fig2, ax2 = plt.subplots(figsize=FIG_SIZE, dpi=DPI)
    sns.regplot(
        data=df_filtered,
        x="TEMP",
        y="PM2.5",
        scatter_kws={"alpha":0.3},
        ax=ax2
    )
    st.pyplot(fig2)

# PRES
with c2:
    st.markdown("**Tekanan Udara (PRES)**")
    fig3, ax3 = plt.subplots(figsize=FIG_SIZE, dpi=DPI)
    sns.regplot(
        data=df_filtered,
        x="PRES",
        y="PM2.5",
        scatter_kws={"alpha":0.3},
        ax=ax3
    )
    st.pyplot(fig3)

# WSPM
with c3:
    st.markdown("**Kecepatan Angin (WSPM)**")
    fig4, ax4 = plt.subplots(figsize=FIG_SIZE, dpi=DPI)
    sns.regplot(
        data=df_filtered,
        x="WSPM",
        y="PM2.5",
        scatter_kws={"alpha":0.3},
        ax=ax4
    )
    st.pyplot(fig4)

st.divider()

# ========================
# INSIGHT 
# ========================
st.subheader("Insight")

st.markdown(f"""
- Rata-rata PM2.5 berfluktuasi selama periode 2013–2017, dengan nilai tertinggi terjadi pada tahun **{tahun_tertinggi}**  

- Suhu (TEMP) memiliki hubungan negatif yang lemah terhadap PM2.5 (≈ -0.13), sehingga peningkatan suhu hanya sedikit berkaitan dengan penurunan konsentrasi polutan  

- Tekanan udara (PRES) tidak menunjukkan hubungan yang signifikan terhadap PM2.5 (≈ 0.02), sehingga bukan faktor utama dalam variasi polusi udara  

- Kecepatan angin (WSPM) memiliki hubungan negatif paling kuat terhadap PM2.5 (≈ -0.27), di mana peningkatan kecepatan angin berkontribusi dalam menurunkan konsentrasi polutan melalui proses dispersi  
""")