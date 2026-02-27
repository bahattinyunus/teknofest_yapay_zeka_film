# 📖 Dahili API ve Sınıf Referansı

Bu döküman, geliştiriciler için sistemdeki temel sınıfların ve metodların teknik ayrıntılarını içerir.

## `DirectorOrchestrator` Sınıfı
Ana boru hattını yöneten orkestrasyon sınıfıdır.

### Metodlar:
- `run_pipeline(creative_prompt: str, output_file: str)`
    - **Açıklama:** Uçtan uca üretim sürecini başlatır.
    - **Parametreler:**
        - `creative_prompt`: Filmin temasını belirleyen metin.
        - `output_file`: Çıkış mp4 dosyasının ismi.
- `_generate_mock_script(prompt: str)`
    - **Açıklama:** Senaryo motorunu simüle eden dahili yardımcı metod.

## `src.core.logger.logger`
Sistem genelinde kullanılan profesyonel loglama arayüzüdür.
- `logger.info(msg)`: İşleyiş bilgisi.
- `logger.error(msg)`: Hata raporlama.
- `logger.debug(msg)`: Geliştirici seviyesi detaylar.

## `src.core.exceptions`
Özel hata sınıfları:
- `EngineError`: Motor bazlı (NLP, Vision) hatalar.
- `ConfigurationError`: Eksik .env veya yapılandırma hataları.
