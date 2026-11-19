# Sinkronisasi dan Koordinasi pada Sistem Terdistribusi

**Nama:** Laesah Afenlia
**NIM:** 255410019

---
## AI yang Digunakan

Claude (Anthropic), model Claude Sonnet 5.5.

## Prompt
buatkan rangkuman,dari modul ini, carilah yang penting2 nya aja.. dari modul semua ini, dm format markdown untuk README.md. 

---

## Apa dan Mengapa Sinkronisasi?

Koordinasi proses, data, dan resource di banyak node agar operasi **konsisten dan andal**. Tujuan: integritas data, sinkronisasi state, koordinasi task, pengelolaan resource, recovery, mencegah deadlock, dan scalable operations.

### Data Race vs Race Condition

| | Data Race | Race Condition |
|---|---|---|
| Level | Low-level (akses memori) | High-level (logika bisnis) |
| Penyebab | ≥2 thread akses memori sama, ≥1 write, tanpa sinkronisasi | Hasil bergantung pada urutan eksekusi tak terduga |
| Solusi | Mutex/lock, tipe atomic | Atomic check-and-act, database transaction lock |

**Contoh e-commerce**: stok produk X = 10. User A dan B sama-sama membaca 10, sama-sama menulis 9. Seharusnya 8.

### Tantangan

Network latency dan partitioning, skalabilitas, fault tolerance, concurrency control, konsistensi data, sinkronisasi waktu.

## Sinkronisasi Waktu Fisik

- Standar: **UTC** (berbasis TAI, International Atomic Time). GMT sudah tidak dipakai.
- Rantai waktu: atomic clock → satelit GPS → GPS dongle → server Linux (NTP/PTP) → klien.
- Sumber atomic clock: ±31 satelit GPS (US Space Force), DSAC (NASA), misi ACES di ISS, master clock di darat (U.S. Naval Observatory dan Schriever Space Force Base).
- **NTP**: implementasi `chrony`. Akurasi milidetik lewat internet, puluhan mikrodetik di LAN.
  ```bash
  chronyc -n sources
  chronyc -n tracking
  ```
- **PTP** (IEEE 1588): lebih presisi. Implementasi `linuxptp` (`ptp4l`, `phc2sys`). NIC wajib mendukung *hardware timestamping*:
  ```bash
  sudo ethtool -T eth0
  ```

## Sinkronisasi Waktu Logis

Menetapkan urutan sebab-akibat kejadian tanpa jam fisik (transitif: A→B dan B→C maka A→C).

### Vector Clock

- Tiap proses menyimpan vektor counter untuk semua proses, awal `[0,0,0]`.
- Setiap event, tambah 1 pada posisi sendiri. Terima pesan: ambil **max per elemen**, lalu tambah 1 pada posisi sendiri.
- **A terjadi sebelum B** jika semua elemen A ≤ B dan minimal satu lebih kecil.
- Jika tidak memenuhi, kejadian **concurrent**.

Contoh akhir: A `[2,0,0]`, B `[2,1,0]`, C `[2,1,2]`. A lebih dulu dari B, sedangkan C dan A concurrent (di slide, C vs A disebut independen).

## Mutual Exclusion

Hanya satu proses boleh masuk *critical section* (CS) pada satu waktu. Prinsip: mutual exclusion, progress, bounded waiting, fairness.

| Algoritma | Kelebihan | Kekurangan |
|---|---|---|
| Centralized | Sederhana, murah | Single point of failure, bottleneck |
| Ricart-Agrawala | Terdistribusi penuh, fault tolerant | Overhead 2×(N−1) pesan per CS |
| Token-based | Hanya 1 pesan per CS | Deteksi token hilang sulit |

## Pemilihan Koordinator (Leader Election)

Saat koordinator gagal atau node baru bergabung, sistem harus memilih pemimpin baru otomatis.

- Algoritma: **Bully**, **Ring**, **Raft/Paxos** (konsensus).
- Contoh: ZooKeeper memakai **Zab**, Kubernetes memakai **Raft** (via etcd).
