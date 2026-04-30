# Dashboard Analisis Kualitas Udara (PM2.5)

Proyek ini bertujuan untuk menganalisis tren konsentrasi PM2.5 serta pengaruh faktor cuaca terhadap kualitas udara di Beijing selama periode 2013–2017 menggunakan dashboard interaktif berbasis Streamlit.

---

## Pertanyaan Bisnis

1. Bagaimana tren rata-rata konsentrasi PM2.5 per tahun pada seluruh stasiun pengamatan di Beijing selama periode 2013–2017, serta pada tahun berapa terjadi tingkat polusi tertinggi?
2. Seberapa besar pengaruh variabel cuaca (suhu, tekanan udara, dan kecepatan angin) terhadap variasi konsentrasi PM2.5 selama periode 2013–2017?

---

## Cara Menjalankan Proyek

### 1. Clone Repository

```bash
git clone https://github.com/r4iizeen/streamlit-dashboard.git
cd streamlit-dashboard
```

---

### 2. Setup Environment

Langkah ini dilakukan untuk menghindari konflik versi library.

#### Opsi 1: Menggunakan Anaconda

```bash
conda create --name air-quality python=3.9
conda activate air-quality
```

#### Opsi 2: Menggunakan Virtual Environment (venv)

```bash
python -m venv venv
```

Aktivasi:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Menjalankan Dashboard

```bash
streamlit run dashboard.py
```

---

## Insight

* Rata-rata konsentrasi PM2.5 berfluktuasi selama periode 2013–2017, dengan nilai tertinggi terjadi pada tahun 2017

* Suhu (TEMP) memiliki hubungan negatif yang lemah terhadap PM2.5 (≈ -0.13), sehingga peningkatan suhu hanya sedikit berkaitan dengan penurunan konsentrasi polutan

* Tekanan udara (PRES) tidak menunjukkan hubungan yang signifikan terhadap PM2.5 (≈ 0.02), sehingga bukan faktor utama dalam variasi polusi udara

* Kecepatan angin (WSPM) memiliki hubungan negatif paling kuat terhadap PM2.5 (≈ -0.27), di mana peningkatan kecepatan angin berkontribusi dalam menurunkan konsentrasi polutan melalui proses dispersi

---
