# Basit Python Projesi

Bu proje, GitLab CI/CD ile basit bir pipeline kurulumu örneği sunar.

## Çalıştırmak için

```bash
python main.py
```

## Testleri çalıştırmak için

```bash
pytest
```

## CI/CD

Pipeline, `.gitlab-ci.yml` dosyasındaki adımları takip ederek testleri otomatik olarak çalıştırır.


![CI](https://github.com/azattekce/devops_cicd_example/actions/workflows/ci.yml/badge.svg)

---

# Teknik Doküman: Python FastAPI + CI/CD + SonarCloud Projesi

## Kullanılan Teknolojiler

- Python 3.11
- FastAPI
- Uvicorn
- Pytest
- Coverage.py
- Docker
- GitHub Actions
- SonarCloud
- GHCR (GitHub Container Registry)
- Kubernetes (örnek deploy)

## Dosya Yapısı ve İçerikleri

- `main.py` veya `src/app.py`: FastAPI uygulaması
- `requirements.txt`: Python bağımlılıkları
- `test_main.py`, `tests/test_app.py`: Unit testler
- `Dockerfile`: Containerize
- `.github/workflows/ci.yml`: CI/CD pipeline
- `sonar-project.properties`: SonarCloud ayarları
- `README.md`: Dokümantasyon

## CI/CD Pipeline Akışı

1. build: Bağımlılık kurulumu
2. test-and-analyze: Test, coverage, SonarCloud
3. docker: Image build & push
4. deploy_staging: Staging deploy (örnek)

## Sık Sorulan Sorular ve Yanıtları

**Docker build/run hatası: Türkçe karakterli tag kullanımı**
Tag’lerde sadece İngilizce karakterler kullanılmalı.

**Docker run hatası: Image bulunamıyor**
Build edilen image adı ile run komutunda aynı isim kullanılmalı.

**Container hemen kapanıyor, logda çıktı var**
Uygulama kodu hemen bitiyorsa container kapanır. Sürekli çalışan bir servis için FastAPI gibi bir framework kullanılmalı.

**FastAPI unit testleri nasıl yazılır?**
`fastapi.testclient` ile endpoint’ler test edilir.

**Pytest ile testler CI’da bulunamıyor**
Test dosya ve fonksiyon isimleri pytest standartlarına uygun olmalı. Paket importları için `__init__.py` dosyaları eklenmeli.

**httpx hatası**
`requirements.txt` dosyasına `httpx` eklenmeli.

**CI badge görünmüyor**
README.md’de badge linkinde gerçek owner ve repo adı kullanılmalı.

**SonarCloud hatası: Proje veya branch bulunamıyor**
SonarCloud’da proje ve organization anahtarları doğru olmalı, default branch ayarlanmalı.

**SonarCloud quality gate failed**
Kodda kalite kapısından geçmeyen bulgular var. SonarCloud panelinden detaylar incelenip düzeltme yapılmalı.

**CI dosyasında syntax hatası**
Her job’da sadece bir kez `runs-on` ve `steps` olmalı, duplicate tanımlar kaldırılmalı.

**SonarCloud entegrasyonu için gerekli ayarlar**
`sonar-project.properties` dosyası repo kökünde olmalı, `SONAR_TOKEN` GitHub secrets’a eklenmeli.

**CI/CD pipeline sırası ve bağımlılıkları**
build → test-and-analyze → docker → deploy_staging şeklinde olmalı.

---

CI/CD Pipeline Akışı
build: Bağımlılıkların kurulumu.
test-and-analyze: Testlerin çalıştırılması, coverage ölçümü ve SonarCloud analizi.
docker: Testlerden sonra Docker image’ının build edilip GHCR’ye push edilmesi.
deploy_staging: Docker image’ı staging ortamına deploy etmek için örnek adım.