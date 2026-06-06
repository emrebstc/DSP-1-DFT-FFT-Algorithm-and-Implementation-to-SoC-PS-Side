import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

sample_rate = 8000 
duration = 3.0     
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

f1 = 400.0   
f2 = 1200.0  
f3 = 2500.0 

sinyal1 = np.sin(2 * np.pi * f1 * t)
sinyal2 = np.sin(2 * np.pi * f2 * t)
sinyal3 = np.sin(2 * np.pi * f3 * t)

telsiz_sinyali = sinyal1 + sinyal2 + sinyal3
telsiz_sinyali = telsiz_sinyali / np.max(np.abs(telsiz_sinyali))

wav_output_name = "yapay_telsiz_sesi.wav"
audio_int16 = (telsiz_sinyali * 32767).astype(np.int16)
wav.write(wav_output_name, sample_rate, audio_int16)

print(f"[+] Signal created and saved as : {wav_output_name}")
print(f"-> Parameters: {sample_rate} Hz | {duration} Seconds | Freqs: {f1}Hz, {f2}Hz, {f3}Hz")

N = len(audio_int16)
fft_result = np.fft.fft(telsiz_sinyali)
fft_freqs = np.fft.fftfreq(N, 1/sample_rate)

half_N = N // 2
frequencies = fft_freqs[:half_N]
power_spec = 20 * np.log10(np.abs(fft_result[:half_N]) + 1e-10)

print("[>>>] Spectrum Creating...")
plt.figure(figsize=(12, 6))
plt.plot(frequencies, power_spec, color='cyan', linewidth=1.5, label="Signal Spectrum")

plt.axvline(x=f1, color='red', linestyle='--', alpha=0.7, label=f"{f1} Hz Tepesi")
plt.axvline(x=f2, color='green', linestyle='--', alpha=0.7, label=f"{f2} Hz Tepesi")
plt.axvline(x=f3, color='yellow', linestyle='--', alpha=0.7, label=f"{f3} Hz Tepesi")

plt.title("Radio Freq Analysis", fontsize=14, fontweight='bold')
plt.xlabel("Freq (Hz)", fontsize=12)
plt.ylabel("Pow / Mag (dB)", fontsize=12)
plt.xlim(0, 4000)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

img_output_name = "yapay_telsiz_spektrumu.png"
plt.savefig(img_output_name, dpi=300, bbox_inches='tight')
plt.close()

print(f"[+] Done, Spectrum has been created: {img_output_name}")