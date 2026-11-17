# Materi Minggu 1: Pengenalan Sistem Terdistribusi dan Terdesentralisasi

Mata Kuliah: Teori Sistem Terdistribusi dan Terdesentralisasi (FIF25002T)
Dosen: Dr. Bambang Purnomosidi D. P.
Prodi: Informatika, UTDI
Sumber: 01 - Pengenalan.pdf (slide dosen)

---

## AI yang Digunakan

Claude (Anthropic), model Claude Sonnet 5.5.

## Prompt

> Tolong buatkan rangkuman materi dari PDF "01 - Pengenalan" ini. Buat yang simple tapi mudah dipahami dan gaya penulisannya berbeda dari contoh yang ada. Jangan pakai tabel, gunakan tulisan biasa saja. Bagian modifikasinya boleh kamu tentukan sendiri. Format markdown, mengikuti format penulisan penggunaan AI dari dosen: Materi Minggu 1, Prompt, dan Bagian yang disesuaikan dari keluaran prompt.

## Bagian yang Disesuaikan dari Keluaran Prompt

Bagian bertanda **[MODIFIKASI]** adalah tambahan di luar isi slide dosen, yaitu:

1. Analogi warung dan restoran pada bagian 1, 3, dan 6.
2. Catatan tentang DNS pada bagian 5.
3. Ilustrasi CAP Theorem dengan transfer saldo pada bagian 8.
4. Catatan koreksi contoh MongoDB dan Cassandra pada bagian 8.
5. Jawaban singkat untuk pertanyaan diskusi pada bagian 12.
6. Cek Pemahaman dan Jembatan Keledai pada bagian 13.

Bagian lainnya mengikuti isi slide dosen, hanya diringkas dengan bahasa yang lebih sederhana.

---

# ISI RANGKUMAN

## 0. Versi Super Singkat

- Sistem terdistribusi: banyak komputer berbagi **beban kerja**, tetapi pengguna merasa hanya memakai satu sistem.
- Sistem terdesentralisasi: **kontrol dan keputusan dibagi** ke banyak pihak, tidak ada satu pusat yang menguasai semuanya.
- CAP Theorem: saat jaringan antar-node terputus, kita harus memilih antara data yang konsisten atau layanan yang tetap tersedia.
- Konsistensi data: bank butuh strong consistency, media sosial cukup eventual consistency.

---

## 1. Kenapa Perlu Sistem Seperti Ini?

Satu komputer saja tidak cukup untuk melayani jutaan pengguna. Alasan utama dari slide:

- Data dan pengguna tumbuh sangat besar.
- Layanan modern perlu skalabilitas, yaitu kemampuan sistem berkembang dan menangani beban yang naik tanpa menurunkan kinerja atau kualitas.
- Sistem harus fault-tolerant, yaitu tetap beroperasi normal walau sebagian komponennya (hardware maupun software) gagal.
- Performa dan ketersediaan harus terjaga 24/7.

Kata dosen, tanpa sistem terdistribusi dan terdesentralisasi, Google, Netflix, dan Blockchain tidak mungkin ada.

**[MODIFIKASI] Analogi warung:** Warung dengan 1 kasir akan antre panjang kalau pembeli ramai. Solusinya menambah kasir (skalabilitas). Kalau satu kasir sakit, kasir lain tetap melayani (fault tolerance). Itulah inti idenya.

---

## 2. Sistem Terdistribusi

Definisi menurut Tanenbaum dan van Steen (2007): *"a collection of independent computers that appears to its users as a single coherent system."*

Artinya, banyak komputer independen saling terhubung lewat jaringan, tetapi pengguna melihatnya sebagai satu sistem yang utuh.

Tiga ciri utamanya:

1. Komponen bersifat independen.
2. Komponen berkomunikasi lewat jaringan.
3. Ada transparansi, yaitu kerumitan di belakang layar disembunyikan dari pengguna.

Jenis transparansi yang disebut di slide:

- **Lokasi:** pengguna tidak perlu tahu server ada di mana.
- **Akses:** cara mengakses sumber daya terasa seragam.
- **Replikasi:** pengguna tidak sadar bahwa datanya punya banyak salinan.
- **Kegagalan:** kerusakan komponen disembunyikan supaya layanan tetap jalan.

Contoh: saat membuka file di Google Drive, kita tidak tahu file itu tersimpan di server mana. Kita cukup klik dan file terbuka.

---

## 3. Arsitektur Sistem Dasar

**Client-Server.** Client meminta layanan, server memproses dan menjawab. Contohnya browser yang meminta halaman web ke web server. Kelebihannya, pengelolaan terpusat sehingga mudah diatur. Kekurangannya, kalau server mati maka semua client ikut terganggu. Kondisi ini disebut single point of failure.

**Peer-to-Peer (P2P).** Semua komputer setara, masing-masing bisa menjadi penyedia sekaligus penerima layanan. Contohnya BitTorrent dan jaringan blockchain.

**Hybrid.** Gabungan keduanya. Gambar di slide menampilkan supernode, dan logo WhatsApp, Signal, serta Telegram, artinya ada server perantara tetapi ada juga hubungan langsung antar-peer.

**[MODIFIKASI] Cara mengingatnya:**

- Client-Server itu seperti restoran: pelanggan memesan, dapur memasak.
- P2P itu seperti arisan atau patungan: semua orang ikut berkontribusi.
- Hybrid itu seperti pasar yang punya kantor pengelola: pedagang saling bertransaksi, pengelola yang mengatur.

---

## 4. Karakteristik Sistem Terdistribusi

1. Transparansi lokasi.
2. Skalabilitas.
3. Fault tolerance.
4. Kinerja tinggi.
5. Heterogenitas, yaitu perangkat, sistem operasi, dan teknologinya boleh beragam. Misalnya server Linux, aplikasi Android, dan layanan Windows bisa bekerja sama.

---

## 5. Sistem Terdesentralisasi

- Sentralisasi: kontrol ada pada 1 titik.
- Desentralisasi: kontrol dibagi, sehingga tidak ada single point of failure.
- Keputusan diambil secara kolektif lewat konsensus, yaitu kesepakatan antar-node.
- Contoh: Blockchain, DNS, dan BitTorrent.

Gambar dari Paul Baran (1964) menunjukkan tiga model jaringan:

- **Centralized (A):** semua titik terhubung ke satu pusat.
- **Decentralized (B):** ada beberapa titik pusat atau hub.
- **Distributed (C):** jaringan menyebar rata seperti jaring.

**[MODIFIKASI] Catatan DNS:** DNS sering disebut terdesentralisasi, tetapi sebenarnya bersifat hierarkis karena ada otoritas di tingkat atas. Jadi DNS lebih tepat dipahami sebagai sistem terdistribusi dengan pengelolaan berjenjang. Wajar kalau ada yang memperdebatkannya.

---

## 6. Terdistribusi vs Terdesentralisasi

- Terdistribusi berfokus pada **pembagian beban kerja**. Contoh di slide: Google File System dan MinIO Object Storage (slide menyebut MinIO sekarang sudah di-fork ke Silo).
- Terdesentralisasi berfokus pada **pembagian kontrol**. Contoh di slide: Blockchain.

**[MODIFIKASI] Analogi restoran:**

Kalau satu perusahaan punya 100 cabang restoran dan semuanya diatur kantor pusat, itu **terdistribusi**: pekerjaan dibagi ke banyak tempat, tetapi kontrol tetap di satu pihak.

Kalau ada 100 warung independen yang sepakat memakai aturan yang sama dan mengambil keputusan bersama, itu **terdesentralisasi**: kontrolnya yang dibagi.

Kesimpulannya, sistem terdistribusi belum tentu terdesentralisasi, dan keduanya bisa digabungkan.

---

## 7. Studi Kasus

Sistem terdistribusi:

- Google File System dan HDFS untuk menyimpan data berukuran besar.
- Apache Kafka dan Apache Pulsar untuk messaging dan streaming.
- Netflix dan Twitch untuk streaming video skala besar.
- YouTube untuk berbagi video.
- Instagram, Threads, Facebook, dan TikTok untuk media sosial dengan data dan interaksi masif.

Sistem terdesentralisasi:

- Blockchain, seperti Bitcoin, Ethereum, Algorand, Sui, Near, dan Aptos.
- DNS, yang menerjemahkan nama domain menjadi alamat IP.
- BitTorrent, yang berbagi file lewat P2P.

---

## 8. CAP Theorem (Brewer's Theorem, tahun 2000)

Tiga komponennya menurut slide:

- **Consistency:** setiap operasi baca mengembalikan tulisan terbaru, atau error.
- **Availability:** setiap permintaan ke node yang tidak gagal dijawab dengan respons non-error, walau bukan data terbaru.
- **Partition Tolerance:** sistem tetap beroperasi walau komunikasi antar-node terputus atau terfragmentasi.

Intinya, pada distributed data store, partisi jaringan pasti bisa terjadi. Jadi saat partisi, perancang sistem harus memilih salah satu:

- **AP (Availability + Partition Tolerance):** permintaan selalu dilayani, tetapi data bisa tidak sinkron. Konsistensi dikorbankan.
- **CP (Consistency + Partition Tolerance):** permintaan baca maupun tulis ditolak demi menjaga data tetap konsisten. Ketersediaan dikorbankan.

**[MODIFIKASI] Ilustrasi transfer saldo:**

Bayangkan Server A dan Server B sama-sama menyimpan saldo rekening. Tiba-tiba koneksi antar keduanya putus.

Kalau sistem tetap melayani, bisa jadi A mencatat saldo Rp100.000 sementara B masih mencatat Rp150.000. Itu pilihan **AP**.

Kalau sistem menolak transaksi dulu sampai sambungan pulih, saldo tetap aman tetapi pengguna harus menunggu. Itu pilihan **CP**.

**[MODIFIKASI] Catatan tentang contoh di slide:** Slide menulis MongoDB sebagai AP dan Cassandra sebagai CP. Di banyak referensi, pengelompokannya justru kebalikannya: Cassandra umumnya dianggap AP, sedangkan MongoDB pada konfigurasi default cenderung CP. Perilaku keduanya memang bergantung pada konfigurasi. Untuk ujian ikuti slide dosen, tetapi sebaiknya dikonfirmasi ke dosen.

---

## 9. Konsistensi Data

**Strong Consistency:** hasil baca selalu sama dan terbaru. Contohnya bank, karena salah saldo itu fatal.

**Eventual Consistency:** awalnya data antar-node bisa berbeda, tetapi lama-lama akan konsisten. Contohnya media sosial, karena telat beberapa detik melihat jumlah "like" tidak masalah.

---

## 10. Tantangan

- **Latency:** seberapa lama permintaan diproses.
- **Throughput:** seberapa banyak permintaan yang bisa diproses.
- **Keamanan**, dengan dua contoh serangan:
  - DDoS: membanjiri layanan dengan permintaan sampai tidak bisa melayani pengguna yang sah.
  - Sybil Attack: membuat banyak identitas palsu (akun, node, atau pseudonim, bisa sampai ribuan) untuk mendominasi pengaruh, suara, atau reputasi. Biasanya menyerang sistem P2P dan blockchain. Nama "Sybil" berasal dari buku tahun 1973 tentang seorang perempuan dengan gangguan identitas.
- **Kompleksitas manajemen node:** makin banyak node, makin sulit dipantau dan dirawat.
- **Governance (tata kelola):** siapa yang memutuskan perubahan pada sistem terdesentralisasi?

---

## 11. Tren Masa Depan

- **Cloud-native:** aplikasi dirancang untuk lingkungan cloud, dengan Docker untuk mengemas aplikasi dan Kubernetes untuk mengelolanya.
- **Edge dan Fog Computing:** pemrosesan data dilakukan lebih dekat dengan sumber data.
- **Web3 dan DeFi:** layanan internet dan keuangan berbasis teknologi terdesentralisasi.
- **Federated Data dan Learning:** AI dilatih secara terdistribusi tanpa harus mengumpulkan semua data mentah di satu tempat.

---

## 12. Ringkasan dan Diskusi

- Sistem terdistribusi berarti berbagi beban kerja.
- Sistem terdesentralisasi berarti berbagi kontrol.
- Keduanya saling terkait tetapi fokusnya berbeda, dan keduanya menjadi fondasi teknologi modern.

Pertanyaan diskusi dari dosen:

1. Mengapa dunia semakin bergerak menuju distribusi dan desentralisasi?
2. Contoh sehari-hari mana yang paling terasa bagi Anda?

**[MODIFIKASI] Jawaban singkat:**

1. Karena pengguna dan data terus bertambah, sedangkan satu komputer atau satu pihak pusat punya batas kapasitas dan risiko kegagalan.
2. Menonton YouTube atau Netflix tanpa buffering (distribusi), serta transfer atau trading kripto (desentralisasi).

---

## 13. [MODIFIKASI] Cek Pemahaman

1. Apa beda fokus sistem terdistribusi dan terdesentralisasi?
2. Mengapa client-server bisa mengalami single point of failure?
3. Saat terjadi partisi jaringan, apa pilihan yang harus diambil perancang sistem?
4. Mengapa bank butuh strong consistency, sedangkan media sosial cukup eventual consistency?
5. Apa itu Sybil Attack dan sistem apa yang rentan terhadapnya?

Jembatan keledai:

- Terdi**S**tribusi: **S**haring kerja.
- Terdesen**T**ralisasi: **T**anggung jawab dibagi.
- CAP: saat jaringan putus, pilih salah satu, **C** atau **A**.

---

## Referensi

1. Bambang Purnomosidi D. P. *Pengenalan Sistem Terdistribusi dan Terdesentralisasi*. Slide perkuliahan, UTDI.
2. Tanenbaum, A. S., dan van Steen, M. (2007). *Distributed Systems: Principles and Paradigms*.
3. Baran, P. (1964). *On Distributed Communications*, Memorandum RM-3420-PR.

---

Repo: https://github.com/<username>/disdec-teori, direktori `01/`, file `README.md`
