// Apply the FFT
DoubleFFT_1D fft = new DoubleFFT_1D(FFT_SIZE);
int numFrames = (audioData.length - FFT_SIZE) / HOP_SIZE + 1;
double[][] frames = new double[numFrames][FFT_SIZE];
for (int i = 0; i < numFrames; i++) {
for (int j = 0; j < FFT_SIZE; j++) {
frames[i][j] = audioData[i * HOP_SIZE + j] * (0.54 - 0.46 * Math.cos(2 * Math.PI * j / (FFT_SIZE - 1)));
}
fft.realForward(frames[i]);
}

// Convert to decibels
double[][] spectrogram = new double[numFrames][FFT_SIZE / 2];
for (int i = 0; i < numFrames; i++) {
for (int j = 0; j < FFT_SIZE / 2; j++) {
double re = frames[i][2 * j];
double im = frames[i][2 * j + 1];
double magnitude = Math.sqrt(re * re + im * im);
spectrogram[i][j] = 20 * Math.log10(magnitude);
}
}