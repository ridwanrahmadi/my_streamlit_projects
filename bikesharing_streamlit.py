import os
import zipfile
import pandas as pd
import streamlit as st
import requests
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1.0)

df_day = pd.read_csv('day.csv')
df_hour = pd.read_csv('hour.csv')

df_day['dteday'] = pd.to_datetime(df_day['dteday'], format='%Y-%m-%d')
df_hour['dteday'] = pd.to_datetime(df_hour['dteday'], format='%Y-%m-%d')

st.write(
    """
    # ANALISIS DATA BIKE SHARING
    by Rahmadi Ridwan Sadhewo

    rahmadi.ridwan.s@gmail.com

    """
)

st.write(
    """
    ## Pertanyaan Bisnis
    Pertanyaan 1:
    **Apakah perbedaan dengan pengguna casual dan registered dari segi waktu penggunaannya?**

    Pertanyaan 2:
    **Adakah faktor lain yang bisa menjelaskan perbedaan pengguna casual dan registered yang 
    bisa digunakan sebagai insight untuk memperbaiki model bisnis pengada jasa bike sharing untuk 
    mengakomodir pelanggannya dengan lebih efektif?**

    """
)

st.write(
    """

    ## Visualization & Explanatory Analysis
    ### Pertanyaan 1: **Apakah perbedaan dengan pengguna casual dan registered dari segi waktu penggunaannya?**

    """
)

st.write('**Penggunaan Berdasarkan Jam**')

hr_grouped = df_hour[["hr", "casual", "registered"]].groupby(["hr"]).mean()
plt.figure(figsize=(12, 8))
plt.plot(hr_grouped.index, hr_grouped["casual"], label = "casual", color="C3")
plt.plot(hr_grouped.index, hr_grouped["registered"], label = "registered", color="C0")
plt.xticks(np.arange(0, 24, 1))
# plt.xlabel("Jam")
# plt.ylabel("Jumlah Rata-Rata Pengguna")
plt.xlabel('Jam', fontweight ='bold', fontsize = 15)
plt.ylabel('Jumlah Rata-Rata Pengguna', fontweight ='bold', fontsize = 15)
plt.legend()
st.pyplot(plt)

st.write(
    """
    Bagi pengguna registered, terlihat memuncak di dua titik yaitu pada jam 8 pagi dan jam 5 sore. Hal ini kemungkinan besar disebabkan mode penggunaan untuk pengguna register yaitu sebagai sarana transportasi untuk menuju dan pulang dari kantor/kampus.
    
    Untuk pengguna casual, puncak penggunaan ini tidak terlihat dan tingkat pengunaannya secara kesuluruhan tidak sebanyak pengguna registered. Peningkatan tampak dari jam 5-6 pagi hingga memuncak & relatif stabil di siang hari sebelum kembali menurun setelah jam 5 sore

    """
)

st.write('**Penggunaan Berdasarkan Hari**')

wd_grouped = df_day[["weekday", "casual", "registered"]].groupby(["weekday"]).sum()
wd_grouped["weekday"] = ['Minggu','Senin','Selasa','Rabu','Kamis','Jumat','Sabtu']

fig = plt.subplots(figsize =(12, 8))

br1 = np.arange(len(wd_grouped["casual"]))
br2 = [x + 0.25 for x in br1]

plt.bar(br1, wd_grouped["casual"], color ='C3', width = 0.25, label ='casual')
plt.bar(br2, wd_grouped["registered"], color ='C0', width = 0.25, label ='registered')

# Adding Xticks
plt.xlabel('Hari', fontweight ='bold', fontsize = 15)
plt.ylabel('Jumlah Perjalanan', fontweight ='bold', fontsize = 15)
plt.xticks([r + 0.25 for r in range(len(wd_grouped["casual"]))], wd_grouped["weekday"])
plt.legend()
st.pyplot(plt)

st.write(
  """
  **Pengguna Casual** lebih cenderung menggunakan sepeda di **hari libur**
  
  **Pengguna registered** lebih cenderung menggunakan sepeda di **hari kerja**

  Maka dari itu bisa diuraikan bahwa pengguna casual menggunakan jasa bike sharing untuk rekreasi dan pengguna registered menggunakan jasa bike sharing lebih sebagai sarana transportasi untuk aktivitas sehari-hari
  
  """
)

st.write('**Penggunaan Berdasarkan Bulan**')

mt_grouped = df_day[["mnth", "casual", "registered", "atemp"]].groupby(["mnth"]).sum()
mt_grouped["month"] = ['Jan','Feb','Mar','Apr','Mei','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

fig = plt.subplots(figsize =(12, 8))

br1 = np.arange(len(mt_grouped["casual"]))
br2 = [x + 0.25 for x in br1]

plt.bar(br1, mt_grouped["casual"], color ='C3', width = 0.25, label ='casual')
plt.bar(br2, mt_grouped["registered"], color ='C0', width = 0.25, label ='registered')

plt.xlabel('Bulan', fontweight ='bold', fontsize = 15)
plt.ylabel('Jumlah Perjalanan', fontweight ='bold', fontsize = 15)
plt.xticks([r + 0.25 for r in range(len(mt_grouped["casual"]))], mt_grouped["month"])
plt.legend()
st.pyplot(plt)

st.write('**Penggunaan Berdasarkan Musim**')

ss_grouped = df_day[["season", "casual", "registered", "atemp"]].groupby(["season"]).sum()
ss_grouped["season"] = ['Semi','Panas','Gugur','Dingin']

fig = plt.subplots(figsize =(12, 8))

br1 = np.arange(len(ss_grouped["casual"]))
br2 = [x + 0.25 for x in br1]

plt.bar(br1, ss_grouped["casual"], color ='C3', width = 0.25, label ='casual')
plt.bar(br2, ss_grouped["registered"], color ='C0', width = 0.25, label ='registered')

plt.xlabel('Musim', fontweight ='bold', fontsize = 15)
plt.ylabel('Jumlah Perjalanan', fontweight ='bold', fontsize = 15)
plt.xticks([r + 0.25 for r in range(len(ss_grouped["casual"]))], ss_grouped["season"])
plt.legend()
st.pyplot(plt)

st.write(
  """
  Penggunaan jasa bike sharing apabila ditinjau dari segi bulan dan musim penggunaannya banyak digunakan di bulan-bulan di musim panas dan musim gugur. 
  Ini bisa disebabkan oleh faktor cuaca di bulan-bulan dan musim tersebut yang ideal untuk bersepeda.
  
  """
)

st.write(
    """

    ### Pertanyaan 2: **Adakah faktor lain yang bisa menjelaskan perbedaan pengguna casual dan registered yang 
    bisa digunakan sebagai insight untuk memperbaiki model bisnis pengada jasa bike sharing untuk 
    mengakomodir pelanggannya dengan lebih efektif?**

    """
)


st.write('**Cluster Analysis Penggunaan Bike Sharing berdasarkan Suhu Relatif**')

fig, ax = plt.subplots(figsize=(12, 8))

sns.scatterplot(
    x=df_day["dteday"], y=df_day["cnt"], hue=df_day["atemp"],
    size=df_day["atemp"], sizes=(20, 200), palette='Greens', ax=ax
)
plt.legend(title='Suhu Relatif', loc='upper left')
plt.ylabel('Jumlah Pengguna')
plt.xlabel('Tanggal')
st.pyplot(plt)

st.write(
  """
  Dapat dilihat bahwa cluster-cluster puncak penggunaan tahunan terjadi pada tanggal-tanggal dimana suhu relatif juga tinggi, yaitu pada tanggal yang berkorespondensi dengan musim panas dan musim gugur (Juni hingga November)
  
  """
)

st.write('**Bar Graph Suhu Relatif terhadap Musim**')

ss_temp = df_day[["season", "atemp"]].groupby(["season"]).mean()
ss_temp["season"] = ['Semi','Panas','Gugur','Dingin']
plt.figure(figsize=(12, 8))
# plt.plot(ss_temp["season"], 50*ss_temp["atemp"], label = "casual", color="C2")
plt.bar(ss_temp["season"], 50*ss_temp["atemp"], color ='C2')
# plt.xticks(np.arange(0, len(ss_grouped["atemp"]), 1))
# plt.xlabel("Jam")
# plt.ylabel("Jumlah Rata-Rata Pengguna")
plt.xlabel('Musim', fontweight ='bold', fontsize = 15)
plt.ylabel('Suhu Relatif', fontweight ='bold', fontsize = 15)
st.pyplot(plt)

st.write('Apabila suhu relatif ditinjau per musim pun, terlihat memang suhu relatif tertinggi terjadi pada musim panas dan musim semi')
st.write('')

st.write('**Pengguna Casual di Hari Libur berdasarkan Suhu Relatif**')

hld_grouped = df_hour[df_hour["holiday"] == 1][["hr", "casual", "registered","atemp"]].groupby(["hr"]).mean()

fig, ax1 = plt.subplots(figsize=(12, 8))
ax1.title.set_text('Pengguna Causal Hari Libur & Suhu Relatif')
ax1.set_xlabel('Jam', fontweight ='bold', fontsize = 15)
ax1.set_ylabel('Jumlah Rata-Rata Pengguna', fontweight ='bold', fontsize = 15, color="C3")
ax1.plot(hld_grouped.index, hld_grouped["casual"], color="C3")
ax2 = ax1.twinx()
ax2.set_ylabel('Suhu Relatif', fontweight ='bold', fontsize = 15, color="C2")
ax2.plot(hld_grouped.index, 50*hld_grouped["atemp"], color="C2", linestyle="--")
fig.tight_layout()
st.pyplot(plt)

st.write(
  """
  Dilihat dari pengguna casual pada hari libur, jam pada hari libur dengan suhu relatif yang tinggi juga menunjukkan penggunaan jasa bike sharing yang tinggi. Hal ini sesuai dengan intuisi sebelumnya bahwa pengguna casual cenderung menggunakan jasa bike sharing untuk rekreasi dan tentunya lebih memilih untuk bersepeda dengan kondisi cuaca yang optimal agar lebih bisa menikmati pengalamannya

  """
)

st.write('**Pengguna Registered di Hari Libur berdasarkan Suhu Relatif**')

fig, ax1 = plt.subplots()
ax1.title.set_text('Pengguna Registered Hari Libur & Suhu Relatif')
ax1.set_xlabel('Jam', fontweight ='bold', fontsize = 15)
ax1.set_ylabel('Jumlah Rata-Rata Pengguna', fontweight ='bold', fontsize = 15, color="C0")
ax1.plot(hld_grouped.index, hld_grouped["registered"], color="C0")
ax2 = ax1.twinx()
ax2.set_ylabel('Suhu Relatif', fontweight ='bold', fontsize = 15, color="C2")
ax2.plot(hld_grouped.index, 50*hld_grouped["atemp"], color="C2", linestyle="--")
fig.tight_layout()
st.pyplot(plt)

st.write(
  """
  Pengguna registered yang menggunakan jasa bike sharing di akhir pekan juga lebih memilih untuk bersepeda dengan kondisi cuaca yang optimal dimana penggunaanya memuncak di sekitar saat suhu relatif juga memuncak

  """
)

st.write('**Pengguna Casual di Hari Kerja berdasarkan Suhu Relatif**')

hld_grouped = df_hour[df_hour["holiday"] == 0][["hr", "casual", "registered","atemp"]].groupby(["hr"]).mean()

fig, ax1 = plt.subplots()
ax1.title.set_text('Pengguna Causal Hari Kerja & Suhu Relatif')
ax1.set_xlabel('Jam', fontweight ='bold', fontsize = 15)
ax1.set_ylabel('Jumlah Rata-Rata Pengguna', fontweight ='bold', fontsize = 15, color="C3")
ax1.plot(hld_grouped.index, hld_grouped["casual"], color="C3")
ax2 = ax1.twinx()
ax2.set_ylabel('Suhu Relatif', fontweight ='bold', fontsize = 15, color="C2")
ax2.plot(hld_grouped.index, 50*hld_grouped["atemp"], color="C2", linestyle="--")
fig.tight_layout()
st.pyplot(plt)

st.write(
  """
  Bahkan di hari biasa pun terlihat korelasi kuat antara penggunaan jasa bike sharing oleh pengguna casual dan pergerakan suhu relatif

  """
)

st.write('**Pengguna Registered di Hari Kerja berdasarkan Suhu Relatif**')

fig, ax1 = plt.subplots(figsize=(12, 8))
ax1.title.set_text('Pengguna Registered Hari Kerja & Suhu Relatif')
ax1.set_xlabel('Jam', fontweight ='bold', fontsize = 15)
ax1.set_ylabel('Jumlah Rata-Rata Pengguna', fontweight ='bold', fontsize = 15, color="C0")
ax1.plot(hld_grouped.index, hld_grouped["registered"], color="C0")
ax2 = ax1.twinx()
ax2.set_ylabel('Suhu Relatif', fontweight ='bold', fontsize = 15, color="C2")
ax2.plot(hld_grouped.index, 50*hld_grouped["atemp"], color="C2", linestyle="--")
fig.tight_layout()
st.pyplot(plt)

st.write(
  """
  Namun hal ini berbeda dengan pola penggunaan jasa bike sharing oleh pengguna registered 
  di hari kerja karena memang digunakan untuk menuju tempat aktivitas sehari-harinya dan lebih 
  berpatok dengan rutinitas dan suhu relatif menjadi faktor yang kurang penting daripada yang 
  diamati secara umum. Saat suhu relatif memuncak di tengah hari pun, pengguna registered berada 
  di puncak kesibukan aktivitas sehari-harinya sehingga penggunaan jasa bike sharing tidak 
  mengikuti pola pada umumnya.

  """
)

fig, ax1 = plt.subplots()
ax1.title.set_text('Pengguna Registered Hari Kerja & Suhu Relatif')
ax1.set_xlabel('Jam', fontweight ='bold', fontsize = 15)
ax1.set_ylabel('Jumlah Rata-Rata Pengguna', fontweight ='bold', fontsize = 15, color="C0")
ax1.plot(hld_grouped.index, hld_grouped["registered"], color="C0")
ax2 = ax1.twinx()
ax2.set_ylabel('Suhu Relatif', fontweight ='bold', fontsize = 15, color="C2")
ax2.plot(hld_grouped.index, 50*hld_grouped["atemp"], color="C2", linestyle="--")
fig.tight_layout()
st.pyplot(plt)

st.write("")

df_temp = df_hour[(df_hour["holiday"] == 0) & (df_hour["hr"] <= 8)]
hld_grouped = df_temp[df_temp["holiday"] == 0][["hr", "casual", "registered","atemp"]].groupby(["hr"]).mean()

fig, ax1 = plt.subplots()
ax1.title.set_text('Sebelum Jam 8 Pagi')
ax1.set_xlabel('Jam', fontweight ='bold', fontsize = 15)
ax1.set_ylabel('Jumlah Rata-Rata Pengguna', fontweight ='bold', fontsize = 15, color="C0")
ax1.plot(hld_grouped.index, hld_grouped["registered"], color="C0")
ax2 = ax1.twinx()
ax2.set_ylabel('Suhu Relatif', fontweight ='bold', fontsize = 15, color="C2")
ax2.plot(hld_grouped.index, 50*hld_grouped["atemp"], color="C2", linestyle="--")
fig.tight_layout()
st.pyplot(plt)

st.write(
  """
  Tapi apabila ditinjau di jam-jam diluar aktivitas sehari-hari pada biasanya, 
  penggunaan jasa bike sharing untuk pengguna registered pun mengikuti pola 
  pergerakan suhu relatif (seperti bisa dilihat dari grafik penggunaan pengguna 
  registered sebelum jam 8 pagi dan setelah jam 5 sore di hari-hari kerja diatas)

  """
)

st.write(
  """
  ## Conclusion
  1) Pengguna Registered lebih cenderung menggunakan jasa bike sharing sebagai sarana 
    transportasi untuk melakukan aktivitas sehari-hari di hari kerja terutama di jam 8 
    pagi dan jam 5 sore sedangkan pengguna casual lebih cenderung menggunakan jasa bike 
    sharing untuk rekreasi di hari libur

  2) Secara umum penggunaan jasa bike sharing berkorelasi kuat dengan suhu relatif atau 
    'feel temperature', yaitu suhu yang sudah diperhitungkan faktor kecepatan angin dan 
    kelembapan udara. Semakin tinggi suhu relatif semakin tinggi juga pengguna jasa bike 
    sharing, seperti di saat musim panas dan musim gugur apabila dilihat secara musiman 
    dan apabila dilihat secara harian hal ini terjadi di waktu-waktu yang mendekati tengah hari

  **Rekomendasi**
  - Model bisnis perusahaan dapat disesuaikan dengan tidak menawarkan satu jenis program langganan (registered users) saja

  - Mengadakan program langganan musiman (seasonal pass) untuk jasa bike sharing khusus di musim panas dan musim gugur untuk 
    mengakomodasi pengguna yang tidak teregistrasi namun menggunakan jasa bike sharing yang sebagian besar terjadi di musim-musim tersebut

  - Mengadakan program langganan yang lebih murah khusus di weekday saja bagi pengguna yang memanfaatkan jasa bike sharing sebagai sarana 
    transportasi untuk beraktivitas sehari-hari dan program langganan khusus weekend untuk pengguna casual yang sering menggunakan jasa 
    bike sharing di akhir pekan untuk berekreasi
  """
)
