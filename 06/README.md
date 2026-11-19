# Modul 6: Distributed File System (DFS) dan Cloud Storage

**Nama:** Laesah Afenlia
**NIM:** 255410019

---
## AI yang Digunakan

Claude (Anthropic), model Claude Sonnet 5.5.

## Prompt
buatkan rangkuman,dari modul ini, carilah yang penting2 nya aja.. dari modul semua ini, dm format markdown untuk README.md. 

---

## File System (FS)

FS adalah metode OS untuk mengelola dan mengatur file di media penyimpan.

- Linux: ext4, XFS, btrfs. Windows: FAT32, NTFS. Mac: APFS.
- Alur akses: aplikasi → system call interface → virtual FS → driver kernel → hardware.
- **FS** (jenis sistem file) berbeda dengan **hirarki FS** (susunan direktori seperti `/bin`, `/etc`, `/home` menurut standar FHS).

## Distributed File System (DFS)

DFS adalah abstraksi software yang menyatukan banyak media penyimpan menjadi satu penyimpanan yang tampak tunggal bagi pengguna, sambil menutupi heterogenitas, kegagalan, dan konkurensi.

Perbedaan dengan storage lain:
- **DAS (Direct-Attached Storage)**: disk langsung terpasang di mesin.
- **NAS (Network-Attached Storage)**: shared storage lewat jaringan, level **file**.
- **SAN (Storage Area Network)**: jaringan khusus, level **block**, cepat tapi mahal.
- **DFS**: abstraksi level software untuk file dan direktori di banyak node, lebih mirip DAS di tiap node.

**DFS populer**: Google File System / Colossus, CephFS, Gluster, **HDFS**, dan Lustre.

## HDFS (Hadoop Distributed File System)

HDFS adalah DFS open source, scalable, dan fault-tolerant untuk dataset besar di *commodity hardware*. File dibagi menjadi blok, disebar ke beberapa server, dan direplikasi untuk high availability.

- **NameNode**: menyimpan metadata (nama file, lokasi blok, jumlah replika).
- **DataNode**: menyimpan blok data.
- **Client**: operasi metadata ke NameNode, baca/tulis blok langsung ke DataNode.
- Hadoop 3.5.0 dikompilasi dengan JDK 17 (server: Java 17, client: Java 17 atau 21).

Praktik instalasi ada di Modul 7.

## Cloud Storage

Cloud storage adalah layanan penyimpanan di server jarak jauh lewat internet. Contoh: Amazon S3, Azure Blob Storage, Google Cloud Storage.

### Tipe Cloud Storage

**Block storage**
- Transport: FC atau iSCSI.
- Antarmuka: Direct Attached atau SAN.
- Cocok untuk: latensi rendah dan data terstruktur.

**File storage**
- Transport: TCP/IP.
- Antarmuka: NFS, SMB.
- Cocok untuk: file sharing dan file locking.

**Object storage**
- Transport: TCP/IP.
- Antarmuka: HTTP, REST.
- Cocok untuk: skala tanpa batas, akses LAN dan WAN.

### Relasi dengan DFS

Cloud storage adalah **tempat penyimpanan**, sedangkan DFS yang **mengorganisasi** operasi FS. Contoh: S3 bisa dipakai HDFS lewat `core-site.xml`:

```xml
<property><name>fs.s3a.access.key</name><value>YOUR_AWS_ACCESS_KEY_ID</value></property>
<property><name>fs.s3a.secret.key</name><value>YOUR_AWS_SECRET_ACCESS_KEY</value></property>
<property><name>fs.s3a.endpoint</name><value>s3.amazonaws.com</value></property>
```

## Studi Kasus Cloud/Object Storage

- **Ceph**: distributed storage open source (object, block, file).
- **CubeFS**: cloud-native, mendukung protokol S3, HDFS, dan POSIX.
- **RustFS**: alternatif MinIO, kompatibel S3.
- **PGSTY SILO**: fork MinIO, kompatibel S3.
- **Rook**: storage cloud-native untuk Kubernetes (file, block, object).
