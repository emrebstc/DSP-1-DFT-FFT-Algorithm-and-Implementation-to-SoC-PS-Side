import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import os

wav_path = "yapay_telsiz_sesi.wav"
if not os.path.exists(wav_path):
    print(f"[-] {wav_path} not found.")
    exit()

sample_rate, data = wav.read(wav_path)

if len(data.shape) > 1:
    data = data[:, 0]

print(f"[+] Sound Reading Done")
print(f"Fs (Sample Rate): {sample_rate} Hz")
print(f"N (sample number) : {len(data)}")

N = len(data)
data_normalized = data / np.max(np.abs(data) + 1e-10)

fft_result = np.fft.fft(data_normalized)
fft_freqs = np.fft.fftfreq(N, 1/sample_rate)

half_N = N // 2
frequencies = fft_freqs[:half_N]
power_spec = 20 * np.log10(np.abs(fft_result[:half_N]) + 1e-10)

print("[>>>] Spectrum creating...")
plt.figure(figsize=(12, 6))
plt.plot(frequencies, power_spec, color='magenta', linewidth=1)
plt.title(f"Radio Sound Spectrum ({wav_path})", fontsize=14, fontweight='bold')
plt.xlabel("Freq (Hz)", fontsize=12)
plt.ylabel("Power / Mag (dB)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

plt.xlim(0, 8000) 

output_img = "telsiz_spektrumu.png"
plt.savefig(output_img, dpi=300, bbox_inches='tight')
plt.close()

print(f"[+] Done, image '{output_img}' has been saved.")