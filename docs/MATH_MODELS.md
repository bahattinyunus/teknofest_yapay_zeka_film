# 🧮 Matematiksel Modeller ve Algoritmik Temeller

Bu döküman, **AI Cinematic Universe** projesinin çekirdeğinde yatan yapay zeka modellerinin matematiksel temellerini ve çalışma prensiplerini detaylandırmaktadır.

## 1. Bilişsel Çekirdek (LLM & Self-Attention)
Senaryo üretimi, metnin anlamsal uzaydaki vektörel temsili üzerinden yürütülür. Transformer mimarisinin temeli olan **Self-Attention** mekanizması şu şekilde formülize edilir:

$$Attention(Q, K, V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Burada:
- **Q (Query):** Mevcut kelimenin aradığı bilgi.
- **K (Key):** Diğer kelimelerin sunduğu bilgi etiketi.
- **V (Value):** Gerçek bilgi içeriği.

## 2. Görsel Motor (Latent Diffusion Models)
Görüntü üretimi, rastgele gürültüden (noise) yapısal bir veri oluşturma sürecidir. **Denoising Diffusion Probabilistic Models (DDPM)** tabanlı süreçlerin çekirdek kaybı (loss function) fonksiyonu şudur:

$$L_{simple} = E_{x_t, \epsilon, t} \left[ \|\epsilon - \epsilon_\theta(\sqrt{\bar{\alpha}_t}x_0 + \sqrt{1-\bar{\alpha}_t}\epsilon, t)\|^2 \right]$$

Bu denklem, modelin $t$ anındaki gürültülü görselden orijinal $x_0$ görseline nasıl geri döneceğini öğrenmesini sağlar.

## 3. Optik Akış ve Kinetik Hareket (Optical Flow)
Statik karelerin canlandırılması, piksellerin zaman içindeki yer değiştirmesini (vektör alanlarını) analiz eden **Gunnar-Farnebäck** algoritması veya derin öğrenme tabanlı **RAFT** mimarileriyle sağlanır:

$$I(x, y, t) = I(x + \Delta x, y + \Delta y, t + \Delta t)$$

Bu parlaklık sabiti varsayımı kullanılarak, her piksel için $(\Delta x, \Delta y)$ yer değiştirme vektörleri hesaplanır.

## 4. Akustik Prosodi (Fundamental Frequency - F0)
Ses sentezinde karakterin duygu durumunu belirleyen temel frekans ($F0$) ve enerji dağılımı, dalga biçimi sentezleyicileri (Vocoders) tarafından işlenir. Duygu vektörü $\mathbf{e}$, sesin spektral zarfını (spectral envelope) şu dönüşümle etkiler:

$$y = f(x, \mathbf{e}_{sentiment})$$

---
*Not: Bu modeller, projenin jüri sunumu ve akademik savunması için referans teşkil etmektedir.*
