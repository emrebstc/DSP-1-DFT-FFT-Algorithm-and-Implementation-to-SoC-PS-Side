clear all; clc; close all;

[sound_data, fs] = audioread('yapay_telsiz_sesi.wav');

N = 1024;
x = sound_data(1:N); 

n = 0:N-1;      
m = (0:N-1)';    

Wn = exp(-1i * 2 * pi / N) .^ (m * n);

Xm = Wn * x;

Magnitude = abs(Xm) / N; 

Freq_axis = (0 : (N/2 - 1)) * (fs / N);

Magnitude(2:N/2) = Magnitude(2:N/2) * 2;

figure;
plot(Freq_axis, Magnitude(1:N/2), 'LineWidth', 2);
grid on;
xlabel('freq (Hz)');
ylabel('Magnitude');