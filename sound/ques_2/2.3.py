import soundfile as sf
from scipy import signal

#reading .wav file
# input_signal,fs=sf.read("Sound_Noise.wav")
input_signal,fs = sf.read('ques_2/Sound_Noise.wav')

#sampling frequency of Input signal
sampl_freq=fs

#order of the filter
order=4   

#cutoff frquency 4kHz
cutoff_freq=4000.0  

#digital frequency
Wn=2*cutoff_freq/sampl_freq  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order,Wn, 'low') 

#filter the input signal with butterworth filter
output_signal = signal.filtfilt(b, a, input_signal)
#output_signal = signal.lfilter(b, a, input_signal)

#write the output signal into .wav file
sf.write('ques_2/Sound_Without_Noise.wav', output_signal, fs) 