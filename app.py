
import streamlit as st
import os
import subprocess
import torchaudio
from speechbrain.pretrained import EncoderClassifier

st.title("🗣️ English Accent Classifier (Proof of Concept)")

url = st.text_input("Enter public video URL (YouTube or direct MP4):")
if st.button("Analyze"):
    with st.spinner("Downloading video..."):
        if "youtube.com" in url or "youtu.be" in url:
            os.system(f'yt-dlp -o input_video.mp4 "{url}"')
        else:
            os.system(f'wget -O input_video.mp4 "{url}"')
    with st.spinner("Extracting audio..."):
        os.system("ffmpeg -y -i input_video.mp4 -ar 16000 -ac 1 -vn audio.wav")
    with st.spinner("Classifying accent..."):
        accent_model = EncoderClassifier.from_hparams(
            source="speechbrain/lang-id-commonlanguage_ecapa",
            savedir="tmp_accent_model"
        )
        signal, fs = torchaudio.load("audio.wav")
        if signal.shape[0] > 1:
            signal = signal[0].unsqueeze(0)
        prediction = accent_model.classify_batch(signal)
        pred_label = prediction[3][0]
        pred_scores = prediction[1][0]
        confidence = float(pred_scores.max()) * 100
        st.success(f"Predicted Accent: {pred_label} ({confidence:.1f}%)")
        st.info(f"The model is {confidence:.0f}% confident this is a {pred_label} English accent.")
