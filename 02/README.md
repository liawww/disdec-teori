# Modul 2: Proses dan Komunikasi Antar Proses (IPC) pada Sistem Terdistribusi

**Nama:** Laesah Afenlia
**NIM:** 255410019

---
prommpt:  buatkan rangkuman, carilah yang penting2 nya aja.. dari modul semua ini, dm format markdown untuk README.md. 
## Konsep Dasar

- **Sistem terdistribusi** adalah kumpulan node independen yang bekerja bersama sebagai satu kesatuan logis. Setiap node menjalankan proses, dan antar proses harus saling berkomunikasi.
- **Manajemen proses** terdiri dari process creation, process migration, dan process monitoring.
- Proses bisa berada di node berbeda, jadi **tidak ada shared memory**. Karena itu diperlukan IPC khusus untuk sistem terdistribusi.
- Contoh nyata: multiplayer game, Gojek/Grab (UI berhubungan dengan layanan driver, location tracking, dan biaya), serta chat WhatsApp.

## Model Komunikasi Pesan

- **Langsung**: memakai socket (TCP).
- **Tidak langsung**: mailbox atau message queue.
- **Pub/Sub**: publisher mengirim ke *topic*, subscriber menerima.

## 4 Jenis IPC

- **Shared memory**: tidak cocok untuk sistem terdistribusi.
- **Message passing**: standar **MPI** (versi 5.0), implementasi Python: `mpi4py`.
- **RPC (Remote Procedure Call)**: klien memanggil prosedur di server lewat *stub*. Contoh: **gRPC**.
- **Middleware (MOM)**: Message-Oriented Middleware, pesan dikirim dan diterima secara **asinkron**.

**Standar dan protokol MOM**:
- AMQP (untuk aplikasi enterprise)
- MQTT (untuk perangkat dengan sumber daya terbatas)
- XMPP
- DDS
- XATMI
- HLA IEEE 1516

## Komunikasi Sinkron vs Asinkron

- **Sinkron**: klien menunggu respons dulu sebelum lanjut.
- **Asinkron**: klien tetap bekerja, respons diproses belakangan.

## Masalah pada IPC dan Solusinya

- **Reliability** (pesan hilang): acknowledgement, retransmisi, TCP.
- **Ordering**: FIFO pipes, message queue, socket, RPC.
- **Security**: enkripsi dan autentikasi (SSL/TLS, OAuth2).
- **Performance**: perhatikan latency dan bandwidth.
- **Deadlock**: timeout dan algoritma deteksi.
- **Inkonsistensi data**: protokol konsensus (Raft, Paxos).

## Protokol Komunikasi

- Protokol dasar: TCP, UDP, HTTP (HTTP/3 berjalan di atas QUIC/UDP).
- Protokol di atas HTTP: **REST, GraphQL, gRPC**.

## Sinkronisasi Waktu (Ringkas)

- Setiap node punya jam lokal yang bisa menyimpang (*drift*), jadi perlu sinkronisasi.
- **Waktu fisik**: atomic clock, lalu GPS, lalu NTP/PTP. PTP lebih presisi dari NTP.
- **Logical clock (Lamport)**:
  1. Setiap kejadian, counter bertambah 1.
  2. Saat kirim pesan, sertakan counter.
  3. Saat terima pesan, `counter = max(lokal, pesan) + 1`.
- Pengembangan lanjutan: Vector clock, Plausible clock, Chain clock, Interval Tree clock, Bloom clock.

## Koordinasi Proses

Mekanisme agar proses independen bekerja harmonis tanpa konflik seperti deadlock dan race condition. Contoh tool: **ZooKeeper, etcd, Consul, ClickHouse Keeper, Oxia, KRaft**.

## Topik Terkini

- Edge dan Fog computing
- Observability dan tracing (telemetry)
- Container orchestration (Kubernetes, Docker Swarm)

## Pertanyaan Diskusi

1. Apakah GraphQL merupakan contoh RPC?
2. Apakah REST merupakan contoh RPC?
3. Apakah telemetry merupakan solusi yang etis?
