#Redes de computadores.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,ifft

def port_function(t):
    return np.cos(2*np.pi*100*t)

def function(t):
	#fs=6
	f=np.cos(2*np.pi*3*t)+np.sin(2*np.pi*2*t)
	return f
def AM(f,port):
	mod=f*port
	return mod*2

def graph(title,time,signal):
	fftData=fft(signal)
	fftData=np.array(fftData)
	frecuency=np.fft.fftfreq(n=signal.size)
	fig, axs = plt.subplots(2)
	fig.suptitle(title)
	axs[0].plot(time, signal)
	axs[0].set(xlabel="Time [S]",ylabel="Amplitude [dB]")
	axs[1].plot(frecuency, abs(fftData))
	axs[1].set(xlabel="Frecuency [Hz]",ylabel="Y=|F(w)|")
	plt.draw()

t=np.linspace(0,1,num=1000)
f=function(t)
port=port_function(t)
graph("Signal",t,f)
graph("Port",t,port)
mod_sig=AM(f,port)
graph("AM signal",t,mod_sig)
plt.show()