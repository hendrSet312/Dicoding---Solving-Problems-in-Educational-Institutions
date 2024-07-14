# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Program dalam insitusi pendidikan ini cukup beragam, mulai dari program bidang kesehatan, sains dan teknologi, jurnalistik, animasi, manajemen hingga turis. Mahasiswa dalam institusi pendidikan ini cukup beragam dan banyak menerima banyak mahasiswa yang merupakan pengungsi dari negara - negara konflik. 

### Permasalahan Bisnis
Institusi ini memiliki banyak jumlah mahasiswa yang dropout. Ada 32% mahasiswa yang telah dropout dan diantaranya kebanyakan dari program / jurusan sains dan teknnologi. Dengan adanya permasalahn ini, institut ini ingin mendeteksi mahasiswa yang dropout secepat mungkin sehingga dapat diberi bimbingan khusus.

### Cakupan Proyek

- Tujuan :

    Mengidentifikasi mahasiswa yang berisiko tinggi untuk dropout dari Jaya Jaya Institut, terutama dari program sains dan teknologi, untuk memberikan bimbingan khusus.

- Pengumpulan Data :

    Data diambil dari berbagai mahasiswa dengan berbagai jurusan  seperti agronomi, desain, pendidikan, keperawatan, jurnalisme, manajemen, layanan sosial, dan teknologi. Dataset ini juga mencakup informasi yang diketahui pada saat pendaftaran mahasiswa (jalur akademik, demografi, dan faktor sosial ekonomi) dan prestasi akademik mahasiswa pada akhir semester pertama dan kedua. 

- Data understanding : 
    1. Menyederhanakan kelas "Status" menjadi "Dropout" dan "Not Dropout"
    2. Menyederhanakan data kategorik di beberapa kolom 
    3. Membuat fitur untuk menilai seberapa mampu mahasiswa untuk menyelesaikan perkuliahan di tahun pertama 

-  Exploratory Data Analysis :
    1. Melakukan analisa univariat, bivariat dan multivariat
    2. Memasukan data kedalam metabase untuk dibuat dashboard 

- Data Preprocessing : 
    1. Mengubah beberapa data kategorik menjadi boolean 
    2. Menghapus data yang tidak relevan 
    3. Mengubah data kategorik menjadi angka dengan catboost-encoder 

-  Modelling : 
    1. Melakukan hypertuning parameter model XGBOOST dengan optuna 
    2. Melatih model XGBOOST dengan parameter yang dihasilkan saat proses hypertuning parameter
    3. Mengevaluasi model yang telah dilatih 

-  Prototyping : 
    1. Membuat website dengan framework streamlit dimana pengguna bisa melakukan prediksi berdasarkan informasi kuliah yang dimasukkan
    2. Memasukan model xgboost dan catboost encoder ke dalam website yang dibuat dalam framework streamlit


### Persiapan

**Sumber data**: https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance

**Setup environment**:

1. Buka Anaconda pada CMD
2. Buat virtual environment  : 
    ```
    conda create --name submission_akhir python=3.9
    ```
3. Aktifkan virtual environment :
    ```
    conda activate submission_akhir
    ```
4. Arahkan virtual environment ke directory submission : 
    ```
    cd /d <letak directory submission>
    ```
    contoh 
    ```
    cd /d \submssion
    ```
5. Install module yang dibutuhkan :
    ```
    pip install -r requirements.txt
    ```


## Business Dashboard
Dashboard dibuat dengan program Metabase dan menjelaskan mengenai profil, kondisi ekonomi, prestasi dan kondisi orang tua dari mahasiswa yang dropout. 

**Metabase** : 

- email : root@mail.com
- password : root123


## Menjalankan Sistem Machine Learning
Link prototype : https://submissiondicoding2.streamlit.app/

**Cara menjalankan prototype**:

1. Secara offline : 
    1. Buka file app.py
    2. Jalankan kode python 
    3. Jika kode python berhasil dijalankan, maka muncul pesan dari library streamlit untuk menjalankan command "streamlit run <lokasi file app.py>"
    4. Jalankan command yang diberikan dan prototype akan muncul dari browser
    5. Isi informasi yang dibutuhkan untuk memprediksi status mahasiswa
2. Secara online : 
    1. Buka link protoytpe yang tertera diatas
    2. Isi informasi yang dibutuhkan untuk memprediksi status mahasiswa


## Conclusion
Kebanyakan mahasiswa yang dropout berasal dari jurusan yang berhubungan dengan Sains dan teknologi seperti teknik dan equinculture. Jurusan ini terbilang cukup sulit dan membutuhkan waktu yang banyak untuk mempelajarinya. Karena waktu belajar yang banyak, ini akan menyulitkan mahasiswa yang memiliki status ekonomi yang rendah atau mereka yang sudah menikah, dimana mereka harus bekerja untuk memenuhi kebutuhan sehari - hari mereka. 


### Rekomendasi Action Items
1.  Perluas program beasiswa untuk mahasiswa dengan status ekonomi rendah. Ini dapat mencakup beasiswa penuh atau sebagian yang mencakup biaya kuliah, buku, dan bahkan biaya hidup.
2.  Sediakan program mentoring dari mahasiswa senior atau dosen untuk membantu mahasiswa yang kesulitan mengikuti materi.
3.  Tawarkan lebih banyak program kelas online atau kelas malam yang memungkinkan mahasiswa untuk belajar dengan lebih fleksibel.
