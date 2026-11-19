# Modul 5: Praktik Load Balancing Aplikasi dengan nginx

**Nama:** Laesah Afenlia
**NIM:** 255410019

---
## AI yang Digunakan

Claude (Anthropic), model Claude Sonnet 5.5.

## Prompt
buatkan rangkuman,dari modul ini, carilah yang penting2 nya aja.. dari modul semua ini, dm format markdown untuk README.md. 

---
# Modul 5: Praktik Load Balancing Aplikasi dengan nginx

**Nama:** Laesah Afenlia
**NIM:** 255410019

---

Aplikasi ASGI Python (**BlackSheep**) di-scale menjadi 2 instance, lalu nginx menjadi load balancer di depannya. Semuanya dijalankan dengan Docker Compose. Materi ini bagian dari topik Fault Tolerance (high availability lewat scaling).

## Prasyarat

- Docker dan Docker Compose (Windows: Docker Desktop, Linux: lewat package manager).
- Python dengan env manager (uv, micromamba, atau miniconda).

## Struktur Proyek

```
.
├── blacksheep_lb/        # aplikasi BlackSheep + Dockerfile bawaan
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
├── docker-compose.yml
└── env.sh                # alias (opsional, Linux/Bash)
```

## 1. Buat Aplikasi

```bash
uv venv && source .venv/bin/activate
uv pip install blacksheep blacksheep-cli
blacksheep create               # template: mvc
cd blacksheep_lb
uv pip install -r requirements.txt
python dev.py                   # http://localhost:44777
```

> Dockerfile bawaan BlackSheep membuka **port 80**, bukan 44777. Satu-satunya perubahan di materi ini: versi Python menjadi `3.14.4-slim`.

## 2. `nginx/Dockerfile`

```dockerfile
FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
```

## 3. `nginx/nginx.conf`

```nginx
events { worker_connections 4096; }

http {
  upstream backend {
    server bs_app:80;       # nama service di docker-compose.yml
  }
  server {
    listen 80;
    location / {
      proxy_pass http://backend;
    }
  }
}
```

## 4. `docker-compose.yml`

```yaml
services:
  bs_app:
    build: ./blacksheep_lb
  nginx:
    container_name: nginx
    build: ./nginx
    ports:
      - 80:80
    depends_on:
      - bs_app
```

## 5. `env.sh` (opsional)

```bash
alias dcu="sudo docker-compose up --build -d --scale bs_app=2"
alias dcd="sudo docker compose down"
alias dps="docker ps --format '{{.Image}} {{.Names}}'"
alias dcln="docker logs nginx"
```

## 6. Jalankan

```bash
sudo dinitctl start dockerd        # dinit
# atau: sudo systemctl start docker
dcu                                # build + jalankan, bs_app di-scale jadi 2
dps                                # lihat container
```

Akses lewat `http://localhost` (port 80, bukan 44777).

## 7. Verifikasi Load Balancing

Cek log tiap instance. Request akan terbagi ke `load-balancing-bs_app-1` dan `load-balancing-bs_app-2`:

```bash
sudo docker logs load-balancing-bs_app-1
sudo docker logs load-balancing-bs_app-2
```

## 8. Matikan

```bash
dcd
```
