# ☁️ AI AWS Cloud Architect

CrewAI ve OpenAI kullanarak AWS bulut mimarisi tasarlayan yapay zeka asistanı.

## 🚀 Özellikler

- **Gereksinim Analizi**: Uygulama gereksinimlerini analiz eder
- **Mimari Tasarım**: Ölçeklenebilir AWS mimarisi önerir
- **Güvenlik İncelemesi**: AWS güvenlik best practice'lerini uygular
- **Maliyet Tahmini**: Aylık maliyet tahmini ve optimizasyon önerileri sunar

## 📋 Gereksinimler

- Python 3.11+
- OpenAI API Key

## ⚙️ Kurulum

1. Repoyu klonlayın:
```bash
git clone https://github.com/your-username/ai-cloud-architect.git
cd ai-cloud-architect
```

2. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

3. `.env` dosyası oluşturun:
```bash
OPENAI_API_KEY=your-api-key-here
```

## 🎯 Kullanım

```bash
streamlit run app.py
```

Tarayıcınızda `http://localhost:8501` adresini açın.

## 📁 Proje Yapısı

```
ai-cloud-architect/
├── app.py              # Streamlit arayüzü
├── requirements.txt    # Python bağımlılıkları
├── crew/
│   ├── agents.py       # CrewAI agent tanımları
│   ├── crew.py         # Crew konfigürasyonu
│   └── tasks.py        # Task tanımları
└── llm/
    └── openai_llm.py   # OpenAI LLM konfigürasyonu
```

## 🛠️ Teknolojiler

- [Streamlit](https://streamlit.io/) - Web arayüzü
- [CrewAI](https://crewai.com/) - Multi-agent framework
- [LangChain](https://langchain.com/) - LLM entegrasyonu
- [OpenAI GPT-4](https://openai.com/) - Yapay zeka modeli

## 📄 Lisans

MIT License
