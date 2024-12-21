import matplotlib.pyplot as plt
import numpy as np
import wave 
from numpy import linalg as LA


def save_data_to_wav(filename, wav, data):
    # round the data to int16 format for writing to .wav file
    data   = data.astype(np.int16)
    outwav = wave.open(filename, 'w')
    outwav.setparams(wav.getparams())
    outwav.setnchannels(1)
    # convert data to bytes for storage
    outwav.writeframes(data.tobytes())
    outwav.close()
    
def read_from_wav(filename):
    # the output: int16 numpy array
    obj  = wave.open(filename, 'rb')
    data = obj.readframes(-1)
    data = np.frombuffer(data, dtype='int16')
    obj.close()
    return data

fn = "sample.wav" # change to the correct location 
data = read_from_wav(fn)

## Your work here
d = len(data)
# Plot the original signal
plt.plot(range(d), data)
plt.xlabel('Time index')
plt.ylabel('Signal Output')
plt.title(f'Signal from sample.wav with d = {d}')
plt.show()

# Fourier Transform 
# fourier_basis_matrix = [[np.exp(1j*2*np.pi*f/d) for f in range(d)] for k in range(d)]
fourier_basis_coeffs = np.fft.fft(data)
frequencies = np.fft.fftfreq(d)
# frequencies = np.fft.fftshift(range(len(fourier_basis_coeffs)))
T = 10
frequencies = np.multiply(d/T, frequencies)
plt.plot(frequencies, abs(fourier_basis_coeffs))
plt.xlabel('Frequency')
plt.ylabel('Modulus of Complex Coefficient in Fourier Basis')
plt.title(f'Fourier Transform of signal from sample.wav with d = {d}')
plt.show()

# Plot abs values as a function of frequency f
#  Processing of data

def project_subspace(b):
    print(b)
    # Set high frequency components (columns!) to zero
    projected_data = np.copy(fourier_basis_coeffs)
    projected_data[b+1:len(frequencies) - b] = 0
    # IDFT to obtain the time domain signal post-projection onto low frequencies
    b_signal = np.fft.ifft(projected_data)

    plt.plot(frequencies, abs(projected_data))
    plt.xlabel('Frequency')
    plt.ylabel('Modulus of Complex Coefficient in Fourier Basis')
    plt.title(f'Fourier Transform of Projected signal from sample.wav with d = {d}, b = {b}')
    plt.savefig(f'fourier_transform_b-{b}.png')
    plt.show()

    
    plt.plot(range(d), b_signal)
    plt.xlabel('Time index')
    plt.ylabel('Signal Output')
    plt.title(f'Projected Signal from sample.wav with d = {d}, b = {b}')
    plt.savefig(f'sample_signal_b-{b}.png')
    plt.show()

    # MSE
    mse =(LA.norm(data - b_signal)**2) / d
    print(mse)

    # store data_processed into .wav file with parameters the same as "sample.wav"
    wav = wave.open(fn, 'rb')
    save_data_to_wav(f"b-{b}Hz-output.wav", wav, b_signal)
    wav.close()

# Projections Processing, Fourier Transform, and MSE
b_vals = [5000, 10000, 40000]

for b in b_vals:
    project_subspace(b)

