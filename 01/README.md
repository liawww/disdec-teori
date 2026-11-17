# Materi Minggu 1: Pengenalan Sistem Terdistribusi dan Terdesentralisasi

Mata Kuliah: Teori Sistem Terdistribusi dan Terdesentralisasi (FIF25002T)
Program Studi: S1 Informatika
Dosen Pengampu: Dr. Bambang Purnomosidi D. P.
Institusi: Universitas Teknologi Digital Indonesia (UTDI)
Sumber Materi: 01 - Pengenalan.pdf

---

## AI yang Digunakan

Claude (Anthropic), model Claude Sonnet 5.5.

## Prompt

**Prompt 1 (rangkuman awal)**

> Tolong buatkan rangkuman materi dari PDF "01 - Pengenalan" ini. Buat yang mudah dipahami dan gaya penulisannya berbeda dari contoh rangkuman yang kuberikan. Bagian modifikasinya boleh kamu tentukan sendiri. Format markdown, mengikuti format penulisan penggunaan AI dari dosen: Materi Minggu 1, Prompt, dan Bagian yang disesuaikan dari keluaran prompt.

## Bagian yang Disesuaikan dari Keluaran Prompt

Bagian bertanda **[MODIFIKASI]** adalah pengembangan di luar poin-poin slide dosen. Bagian tersebut ada pada:

1. Bagian 1: penjelasan hubungan antara pertumbuhan pengguna, skalabilitas, dan fault tolerance.
2. Bagian 2: contoh transparansi pada layanan penyimpanan cloud.
3. Bagian 3: penjelasan cara kerja, kelebihan, dan kekurangan tiap arsitektur, serta contoh Hybrid pada aplikasi pesan.
4. Bagian 5: penjelasan tiga model jaringan Baran dan catatan tentang DNS.
5. Bagian 6: analisis perbedaan terdistribusi dan terdesentralisasi beserta contoh kasus campuran.
6. Bagian 8: ilustrasi CAP Theorem dengan dua server, serta catatan tentang contoh MongoDB dan Cassandra.
7. Bagian 9: penjelasan lebih dalam tentang Strong dan Eventual Consistency.
8. Bagian 10: penjelasan tantangan dengan contoh situasi.
9. Bagian 13: pertanyaan latihan dan jawaban singkat untuk pertanyaan diskusi dosen.

Bagian lain yang tidak bertanda mengikuti isi slide dosen dan hanya dijelaskan ulang dengan bahasa yang lebih mudah dipahami.

---

# RANGKUMAN MATERI

## 1. Arti Penting Sistem Terdistribusi dan Terdesentralisasi

Aplikasi saat ini dipakai oleh jumlah pengguna yang sangat besar, dan data yang dihasilkan juga terus bertambah. Sistem yang hanya mengandalkan satu komputer akan kesulitan menangani kondisi ini. Karena itu dibutuhkan sistem yang bekerja dengan banyak komputer sekaligus. Slide dosen menyebutkan beberapa alasan pentingnya:

- **Pertumbuhan data dan pengguna yang sangat besar.**
- **Layanan modern memerlukan skalabilitas.** Skalabilitas adalah kemampuan suatu sistem, jaringan, proses, atau organisasi untuk berkembang dan menangani peningkatan beban kerja, jumlah pengguna, atau permintaan tanpa mengorbankan kinerja atau kualitas.
- **Sistem harus bersifat fault-tolerant.** Sistem fault-tolerant adalah sistem yang mampu tetap beroperasi secara normal meskipun terjadi kegagalan atau malfungsi pada sebagian komponennya, baik hardware maupun software.
- **Performa dan ketersediaan 24/7.**

Dosen menegaskan bahwa tanpa sistem terdistribusi dan terdesentralisasi, layanan seperti Google, Netflix, dan Blockchain tidak mungkin ada.

**[MODIFIKASI]** Skalabilitas dan fault tolerance saling berkaitan. Ketika jumlah pengguna naik, sistem dapat menambah komputer untuk membagi beban (skalabilitas). Dengan banyaknya komputer, kegagalan satu komputer tidak harus menghentikan seluruh layanan, karena komputer lain dapat mengambil alih tugasnya (fault tolerance). Dua kemampuan inilah yang membuat layanan dapat tersedia terus-menerus.

## 2. Pengertian Sistem Terdistribusi

Menurut Andrew S. Tanenbaum dan Maarten van Steen (2007), sistem terdistribusi adalah *"a collection of independent computers that appears to its users as a single coherent system"*, yaitu sekumpulan komputer independen yang terlihat oleh penggunanya sebagai satu sistem yang utuh.

Tiga hal pokok dari definisi tersebut:

1. **Komponen independen.** Setiap komputer atau node memiliki sumber daya dan kemampuan pemrosesan sendiri.
2. **Berkomunikasi melalui jaringan.** Node saling bertukar pesan untuk meminta, menjawab, dan berkoordinasi.
3. **Transparansi.** Kerumitan sistem disembunyikan dari pengguna. Slide menyebutkan empat bentuknya:
   - Transparansi lokasi: pengguna tidak perlu tahu di mana sumber daya berada.
   - Transparansi akses: sumber daya dapat diakses dengan cara yang seragam.
   - Transparansi replikasi: pengguna tidak perlu tahu bahwa ada beberapa salinan data.
   - Transparansi kegagalan: kegagalan komponen disembunyikan sehingga layanan tetap berjalan.

Slide juga menampilkan contoh arsitektur toko online: aplikasi mobile dan browser mengakses beberapa layanan terpisah (Account Service, Inventory Service, dan Shipping Service) melalui REST API dan API Gateway, dengan basis data masing-masing. Dari sisi pengguna, semuanya terlihat sebagai satu aplikasi toko.

**[MODIFIKASI]** Contoh yang mudah adalah layanan penyimpanan cloud seperti Google Drive. Pengguna hanya mengunggah dan membuka file, tanpa perlu tahu file disimpan di server mana, apakah ada salinan cadangan, atau bagaimana permintaan dibagi ke berbagai server. Itulah wujud transparansi lokasi dan replikasi dalam praktik.

## 3. Arsitektur Sistem Dasar

Slide membahas tiga arsitektur dasar.

### 3.1 Client-Server

Pada arsitektur ini, client mengirim permintaan dan server memproses serta mengirim jawabannya. Pada gambar slide, beberapa client (laptop, ponsel, komputer) terhubung melalui internet ke satu server.

**[MODIFIKASI]** Contohnya browser yang meminta halaman web dari web server. Kelebihan model ini adalah pengelolaan data dan layanan yang terpusat sehingga mudah diatur dan dirawat. Kekurangannya, bila server utama mati dan tidak ada cadangan, seluruh client ikut tidak terlayani. Kondisi ini disebut *single point of failure*.

### 3.2 Peer-to-Peer (P2P)

Pada arsitektur P2P, setiap komputer (peer) terhubung langsung dengan peer lain dan berstatus setara. Slide memberi contoh BitTorrent dan berbagai mata uang kripto seperti Bitcoin dan Ethereum.

**[MODIFIKASI]** Setiap peer dapat menjadi penyedia sekaligus penerima layanan, sehingga tidak ada satu server pusat yang menjadi penopang utama. Pada BitTorrent, misalnya, sebuah file dipecah menjadi bagian-bagian dan diunduh dari banyak peer sekaligus.

### 3.3 Hybrid

Arsitektur Hybrid menggabungkan Client-Server dan P2P. Gambar slide menunjukkan beberapa *supernode*: client terhubung ke supernode, antar supernode saling terhubung, dan pertukaran data tertentu dapat berlangsung langsung antar-peer. Slide menampilkan logo WhatsApp, Signal, dan Telegram sebagai contoh aplikasi yang dikaitkan dengan model ini.

**[MODIFIKASI]** Dalam model ini, server menangani fungsi yang butuh pengelolaan pusat, misalnya pencarian pengguna, sedangkan pertukaran data tertentu dapat dilakukan langsung antar-perangkat. Pendekatan ini mencoba mengambil kemudahan pengelolaan dari Client-Server dan fleksibilitas berbagi sumber daya dari P2P.

## 4. Karakteristik Sistem Terdistribusi

Slide menyebutkan lima karakteristik:

1. **Transparansi lokasi:** pengguna tidak perlu mengetahui lokasi fisik sumber daya.
2. **Skalabilitas:** sistem dapat berkembang mengikuti kenaikan pengguna, data, dan permintaan.
3. **Fault tolerance:** sistem tetap berjalan walau sebagian komponen gagal, biasanya didukung replikasi dan redundansi.
4. **Kinerja tinggi:** beban kerja dibagi ke banyak komputer sehingga pemrosesan dapat dilakukan bersamaan.
5. **Heterogenitas:** sistem dapat terdiri dari perangkat keras, sistem operasi, jaringan, dan teknologi yang berbeda-beda.

## 5. Pengertian Sistem Terdesentralisasi

Berdasarkan slide:

- **Sentralisasi:** kontrol berada pada satu titik.
- **Desentralisasi:** kontrol didistribusikan sehingga tidak ada *single point of failure*.
- **Keputusan kolektif melalui konsensus.** Konsensus adalah mekanisme agar node-node mencapai kesepakatan tentang suatu keputusan atau keadaan bersama.
- **Contoh:** Blockchain, DNS, dan BitTorrent.

Slide menampilkan gambar dari Paul Baran (1964), *On Distributed Communications*, yang membandingkan tiga bentuk jaringan:

- **Centralized (A):** semua stasiun terhubung ke satu pusat.
- **Decentralized (B):** ada beberapa pusat (hub), masing-masing melayani sekelompok stasiun.
- **Distributed (C):** stasiun saling terhubung membentuk jaring tanpa pusat tunggal.

**[MODIFIKASI]** Gambar ini membantu melihat bahwa semakin tersebar koneksi suatu jaringan, semakin kecil dampak kegagalan satu titik. Pada model A, rusaknya titik pusat memutus seluruh jaringan. Pada model C, banyak jalur alternatif tersedia.

**[MODIFIKASI] Catatan tentang DNS:** DNS dikelompokkan sebagai contoh terdesentralisasi di slide. Namun struktur DNS bersifat hierarkis (ada otoritas pada tingkat atas dan pengelolaan berjenjang), sehingga DNS tidak sepenuhnya terdesentralisasi dalam arti tanpa otoritas pusat. DNS lebih tepat dipahami sebagai sistem dengan pengelolaan yang tersebar dan berjenjang.

## 6. Sistem Terdistribusi vs Sistem Terdesentralisasi

Perbedaan menurut slide:

- Sistem **terdistribusi** berfokus pada **pembagian beban kerja**. Contoh: Google File System dan MinIO Object Storage (slide menyebut MinIO sekarang sudah di-fork ke Silo).
- Sistem **terdesentralisasi** berfokus pada **pembagian kontrol**. Contoh: Blockchain.

**[MODIFIKASI]** Dengan kata lain, terdistribusi menjawab pertanyaan "siapa yang mengerjakan?", sedangkan terdesentralisasi menjawab pertanyaan "siapa yang memutuskan?". Sebuah perusahaan dapat menjalankan ribuan server di banyak negara (terdistribusi), tetapi bila semuanya dikendalikan satu perusahaan, sistemnya tidak terdesentralisasi. Sebaliknya, jaringan Blockchain publik menyebar kontrol validasi transaksi ke banyak peserta (terdesentralisasi), dan jaringan itu sekaligus terdistribusi karena dijalankan banyak komputer. Jadi keduanya saling terkait, tetapi tidak sama.

## 7. Studi Kasus Sistem Terdistribusi

- **Google File System dan HDFS:** penyimpanan data berukuran besar. **[MODIFIKASI]** Data dipecah menjadi blok-blok yang disimpan di banyak node dan direplikasi agar tetap tersedia saat ada node yang gagal.
- **Apache Kafka dan Apache Pulsar:** messaging dan streaming. **[MODIFIKASI]** Komponen aplikasi dapat saling mengirim pesan melalui perantara tanpa harus terhubung langsung satu sama lain, misalnya pada pemrosesan pesanan di e-commerce.
- **Netflix dan Twitch:** layanan streaming video yang harus melayani pengguna dalam jumlah besar.
- **YouTube:** berbagi video yang melibatkan penyimpanan, pemrosesan, dan distribusi video.
- **Instagram, Threads, Facebook, dan TikTok:** media sosial yang mengelola unggahan, interaksi, dan data pengguna dalam skala besar.

## 8. Studi Kasus Sistem Terdesentralisasi

- **Blockchain:** contohnya Bitcoin, Ethereum, Algorand, Sui, Near, dan Aptos. Transaksi divalidasi oleh banyak node berdasarkan aturan protokol dan konsensus, tidak oleh satu server pusat.
- **DNS (Domain Name System):** menerjemahkan nama domain menjadi alamat IP.
- **BitTorrent:** protokol berbagi file berbasis P2P. **[MODIFIKASI]** Semakin banyak peer yang memiliki bagian file, semakin banyak sumber unduhan, namun ketersediaan file tetap bergantung pada peer yang aktif.

## 9. CAP Theorem (Brewer's Theorem)

CAP Theorem sering disebut Brewer's Theorem, diperkenalkan oleh Eric Brewer pada tahun 2000. Tiga komponennya menurut slide:

- **Consistency:** setiap operasi baca mengembalikan penulisan terbaru, atau error.
- **Availability:** setiap permintaan ke node yang tidak gagal akan menerima respons non-error, meskipun bukan data terbaru.
- **Partition Tolerance:** sistem tetap beroperasi meskipun komunikasi antar-node terputus atau terfragmentasi.

Pada distributed data store, tidak mungkin mendapatkan Consistency dan Availability sekaligus karena partisi pasti bisa terjadi. Saat terjadi partisi, perancang sistem harus menentukan AP atau CP, meskipun sistem dapat pulih otomatis (*auto healing*) setelah partisi selesai:

- **AP (Availability + Partition Tolerance):** permintaan data selalu dilayani, dengan risiko data tidak sinkron, artinya konsistensi dikorbankan. Slide memberi contoh MongoDB.
- **CP (Consistency + Partition Tolerance):** permintaan data (baca maupun tulis) ditolak untuk memastikan data tetap konsisten, artinya availability dikorbankan. Slide memberi contoh Apache Cassandra.

**[MODIFIKASI] Ilustrasi dua server:** Misalkan Server A dan Server B menyimpan data saldo rekening yang sama, lalu koneksi antar keduanya terputus. Jika sistem memilih AP, kedua server tetap melayani pengguna, tetapi saldo yang ditampilkan bisa berbeda karena belum tersinkron. Jika sistem memilih CP, server menolak sebagian permintaan sampai koneksi pulih, sehingga data aman tetapi pengguna harus menunggu atau mendapat error.

**[MODIFIKASI] Catatan tentang contoh di slide:** Penempatan MongoDB sebagai AP dan Cassandra sebagai CP pada slide adalah penyederhanaan. Pada banyak referensi, Cassandra justru lebih sering dikategorikan AP, sedangkan MongoDB dengan konfigurasi default cenderung CP. Perilaku keduanya sebenarnya bergantung pada konfigurasi dan tingkat konsistensi yang dipilih. Untuk keperluan ujian, rangkuman ini mengikuti slide dosen, dan sebaiknya dikonfirmasi ke dosen bila perlu.

## 10. Konsistensi Data

Slide membedakan dua model:

- **Strong Consistency:** hasil selalu sama. Contoh: bank, yang butuh strong consistency.
- **Eventual Consistency:** lama-lama konsisten. Contoh: media sosial, yang cukup dengan eventual consistency.

**[MODIFIKASI]** Pada strong consistency, setelah suatu data berhasil diperbarui, semua pembacaan berikutnya harus melihat data terbaru. Ini penting pada saldo rekening karena informasi yang keliru dapat menimbulkan kerugian. Pada eventual consistency, perubahan dibolehkan belum terlihat di semua node untuk sementara waktu. Jika tidak ada perubahan baru dan sinkronisasi berjalan, semua node pada akhirnya akan menunjukkan data yang sama. Model ini cocok untuk hal seperti jumlah "like" atau unggahan foto, karena keterlambatan beberapa saat tidak berbahaya dan sistem dapat melayani lebih banyak pengguna.

## 11. Tantangan

Slide menyebutkan empat tantangan:

1. **Latency dan throughput.** Latency adalah seberapa lama sebuah permintaan diproses, sedangkan throughput adalah seberapa banyak permintaan yang dapat diproses.
2. **Keamanan**, khususnya:
   - **DDoS (Distributed Denial of Service):** membanjiri layanan dengan permintaan sehingga tidak dapat melayani pengguna yang sah.
   - **Sybil Attack:** serangan siber dengan membuat banyak identitas palsu (akun, node, atau pseudonim, sampai ribuan) secara bersamaan untuk mendominasi pengaruh, suara, atau reputasi dalam jaringan. Biasanya terjadi pada sistem terdesentralisasi seperti P2P atau blockchain. Dengan menyamar sebagai banyak pengguna sah, penyerang dapat memanipulasi sistem, merusak integritasnya, melakukan tindakan tidak sah, dan mengakses informasi sensitif. Nama "Sybil" berasal dari nama seorang perempuan dengan gangguan identitas dalam sebuah buku tahun 1973.
3. **Kompleksitas manajemen node.**
4. **Governance (tata kelola) pada sistem terdesentralisasi.**

**[MODIFIKASI]** Kompleksitas manajemen node muncul karena semakin banyak node, semakin sulit memantau, mengonfigurasi, dan menangani kegagalannya. Governance menjadi tantangan karena keputusan tidak dipegang satu pihak, sehingga perlu aturan yang jelas tentang bagaimana perubahan sistem disepakati dan bagaimana konflik antarpeserta diselesaikan. Pada jaringan dengan sistem pemungutan suara, Sybil Attack berbahaya karena penyerang bisa memperbesar pengaruhnya dengan banyak identitas palsu.

## 12. Tren Masa Depan

Slide menyebutkan empat tren:

- **Cloud-native (Kubernetes, Docker):** Docker mengemas aplikasi beserta lingkungannya dalam container, dan Kubernetes mengelola container tersebut dalam cluster.
- **Edge dan Fog Computing:** pemrosesan data dilakukan lebih dekat dengan sumber data atau pengguna, sehingga mengurangi latency dan kebutuhan bandwidth.
- **Web3 dan DeFi:** layanan internet dan keuangan yang memanfaatkan Blockchain dan smart contract, tanpa sepenuhnya bergantung pada perantara tradisional.
- **Federated Data dan Federated Learning (AI terdistribusi):** model AI dilatih di banyak perangkat atau lokasi tanpa harus mengumpulkan semua data mentah di satu server pusat.

## 13. Ringkasan dan Diskusi

Ringkasan dari slide:

- Sistem terdistribusi berarti berbagi beban kerja.
- Sistem terdesentralisasi berarti berbagi kontrol.
- Keduanya saling terkait tetapi berbeda fokus.
- Keduanya menjadi fondasi teknologi modern.

Pertanyaan diskusi dari dosen:

**1. Mengapa dunia semakin bergerak menuju distribusi dan desentralisasi?**

**[MODIFIKASI]** Karena jumlah pengguna dan data terus bertambah, sementara satu komputer atau satu pusat kendali memiliki batas kapasitas dan risiko kegagalan. Distribusi memberi kapasitas dan ketahanan, sedangkan desentralisasi mengurangi ketergantungan pada satu pihak.

**2. Contoh sehari-hari yang paling terasa?**

**[MODIFIKASI]** Menonton YouTube atau Netflix tanpa terputus (distribusi), menyimpan file di cloud, serta transaksi aset kripto di jaringan Blockchain (desentralisasi).

---

## Kesimpulan

Sistem terdistribusi membagi beban kerja ke banyak komputer independen yang terlihat sebagai satu sistem, sedangkan sistem terdesentralisasi membagi kontrol dan pengambilan keputusan ke banyak pihak melalui konsensus. Keduanya menjadi dasar layanan modern seperti cloud, streaming, dan Blockchain, dengan tantangan berupa latency, keamanan, kompleksitas node, dan tata kelola. CAP Theorem menunjukkan bahwa saat terjadi partisi jaringan, perancang harus memilih antara konsistensi dan ketersediaan, dan pilihan itu bergantung pada kebutuhan aplikasi, misalnya strong consistency untuk bank dan eventual consistency untuk media sosial.

## Referensi

1. Bambang Purnomosidi D. P. *Pengenalan Sistem Terdistribusi dan Terdesentralisasi*. Slide perkuliahan, Universitas Teknologi Digital Indonesia.
2. Tanenbaum, A. S., dan van Steen, M. (2007). *Distributed Systems: Principles and Paradigms*.
3. Baran, P. (1964). *On Distributed Communications*. Memorandum RM-3420-PR.

---

Repo: https://github.com/<username>/disdec-teori, direktori `01/`, file `README.md`
