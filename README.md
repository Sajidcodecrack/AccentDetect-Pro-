 ## AccentDetect-Pro

**Automated English Accent Classifier for Hiring – Proof of Concept**

---

## 🌍 Overview

**AccentDetect-Pro** is an end-to-end tool to help automate the screening of spoken English candidates by classifying their English accent from a public video URL (YouTube or direct MP4). It extracts the audio, uses a pre-trained open-source model to identify the English accent, and provides a confidence score and short explanation. Designed as a proof-of-concept for real-world hiring automation.

---

## 🚀 Features

- **Accepts Public Video URL:** YouTube or direct .mp4 link supported.
- **Automatic Audio Extraction:** Uses ffmpeg to pull clear audio from video.
- **Accent Classification:** Utilizes open-source neural models for accent/language ID.
- **Confidence Score:** Displays how sure the model is (0–100%).
- **Short Explanation:** Gives a human-friendly summary of the result.
- **Simple UI (Streamlit):** Paste a URL and see instant results.
- **Open, Reproducible, Extensible:** Built for demonstration, easy to expand.

---

## 🛠️ Usage

### 1. **Requirements**

- Python 3.8+
- [ffmpeg](https://ffmpeg.org/) (auto-installed via pip package)
- See `requirements.txt` for all dependencies.

### 2. **Installation**

Clone the repository:
```bash
git clone https://github.com/yourusername/AccentDetect-Pro.git
cd AccentDetect-Pro.py
```
### Install dependencies:
```bash
pip install -r requirements.txt
```
3. Running as a Script
You can use the Jupyter notebook or run the script directly.

```bash
python accent_detect.py
```
# launch the Streamlit app:
```bash 
streamlit run app.py
```
### Model Details
### Accent Model: SpeechBrain ECAPA-TDNN for Language ID

Robust, open-source, not fine-tuned for regional English (British/American), but suitable for "English vs. non-English" screening.

Easy to swap for more specific accent classifiers as they become available.

### Audio Extraction: ffmpeg

### UI: Streamlit (simple, fast, Pythonic)
