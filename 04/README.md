# Konsistensi dan Replikasi pada Sistem Terdistribusi


**Nama:** Laesah Afenlia
**NIM:** 255410019

---
## AI yang Digunakan

Claude (Anthropic), model Claude Sonnet 5.5.

## Prompt
buatkan rangkuman,dari modul ini, carilah yang penting2 nya aja.. dari modul semua ini, dm format markdown untuk README.md. 

---

## Konsistensi

Menjamin semua node punya data yang sama (atau tampak sama) walau data tersebar dan diubah bersamaan. Tanpa konsistensi, pengguna bisa melihat versi data berbeda tergantung server yang dibaca (contoh: transfer bank, saldo A sudah berkurang tapi saldo B belum bertambah).

## Teorema CAP

| | Arti |
|---|---|
| **C**onsistency | Semua node punya data sama |
| **A**vailability | Data selalu tersedia saat diminta |
| **P**artition tolerance | Sistem tetap jalan walau jaringan terputus |

Partisi jaringan pasti terjadi, jadi pilihan praktisnya **CP** atau **AP**.

- **AP**: tetap melayani, stok bisa sementara tidak sinkron.
- **CP**: tolak transaksi sampai jaringan pulih, mengorbankan availability.

## Model Konsistensi (kuat → lemah)

| Model | Inti | Contoh |
|---|---|---|
| Linearizability | Paling kuat, tampak seperti satu node atomik | etcd, ZooKeeper, Spanner |
| Sequential | Semua node melihat urutan operasi yang sama | Urutan posting medsos |
| Causal | Urutan sebab-akibat dijaga | Komentar tidak muncul sebelum postingnya |
| Read-your-writes | Penulis langsung melihat tulisannya sendiri | Pesan terkirim langsung tampil |
| Monotonic read | Tidak melihat versi lebih lama dari yang sudah dilihat | Timeline tidak mundur |
| Eventual | Akhirnya sama jika tidak ada update baru | DynamoDB, Cassandra |

- **Strong consistency**: biasanya memakai Two-Phase Commit atau Paxos.
- **BASE**: Basically Available, Soft state, Eventual consistency.
- **Trade-off**: konsistensi ↑ → latensi ↑, konsistensi ↓ → latensi ↓.

## Replikasi Data

Membuat dan memelihara salinan data di beberapa node untuk **availability, performa, reliabilitas, skalabilitas baca**.

### Jenis Replikasi

- **Master-Slave**: satu penulis, banyak pembaca. Contoh: PostgreSQL streaming replication.
- **Multi-Master**: semua node bisa menulis, rawan konflik. Contoh: Cassandra, MongoDB, Apache Ignite.
- **Synchronous**: konsisten tapi lambat (Spanner).
- **Asynchronous**: cepat tapi bisa tertinggal (MySQL async, DynamoDB).

### Strategi Sinkronisasi

| Dimensi | Pilihan |
|---|---|
| Waktu | Asynchronous (tercepat, risiko hilang data tertinggi), semi-synchronous (tunggu 1 replika, dipakai MySQL), synchronous (tunggu semua replika) |
| Cara | Pull-based, push-based (CDC + WebSockets/SSE), hybrid |
| Konflik | LWW, Vector Clock, CRDT, OT |

- **LWW**: timestamp terbaru menang.
- **CRDT**: struktur data konvergen di tiap node, tanpa server pusat (contoh: Yjs). Contoh counter dengan aturan `max` per elemen.
- **OT**: transformasi operasi berdasarkan informasi lokal. Contoh: teks "abc", sisip "x" di indeks 0 dan hapus indeks 2 bersamaan, setelah transformasi hasil sama: "xab".

## Protokol Replikasi

1. **Primary-based** (master-slave).
2. **Quorum-based**: syarat **W + R > N**. Contoh N=3, W=2, R=2, irisan node menjamin pembacaan melihat tulisan terbaru.
3. **State Machine Replication**: leader mengurutkan perintah di log, replika mengeksekusi urutan yang sama.
4. **Gossip protocol**: node acak saling bertukar status, dipakai Cassandra.
5. **Chain replication**: write masuk di head, read dari tail.

## Studi Kasus

PostgreSQL 18 (streaming replication) dan Apache Ignite 3 (multi-master).

## Pertanyaan Diskusi

1. Apa kelebihan dan kekurangan strong vs eventual consistency?
2. Bagaimana jika replikasi gagal di satu node?
