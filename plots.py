import matplotlib.pyplot as plt
import numpy as np

def plot_3ch_signal(sig_1, sig_2, fs=100):
    t = np.arange(0, (len(sig_1) / fs), 1 / fs) #Assuming sig_1 and sig_2 have the same length
    plt.figure()
    ax1 = plt.subplot(311)
    ax1.plot(t, sig_1[0], color='blue')
    ax1.plot(t, sig_2[0], color='red')
    ax1.margins(x=0, y=-0.25)  #No zoom on x axis, zoom in on y. If y = +0.25, zooms out.
    ax1.legend(['Signal_XX', 'Signal_YY']) #plt.legend(['C', 'W'])

    # ax1.plot(sig_1[0]- 3 * sig_2[0], color='green')
    plt.ylabel(' Signal X_ ch 1', fontsize=16)
    # plt.xlabel('Time (s)', fontsize=16)

    ax2 = plt.subplot(312, sharex=ax1)
    ax2.plot(t, sig_1[1], color='blue')
    ax2.plot(t, sig_2[1], color='red')
    plt.ylabel(' Signal X_ Ch 2', fontsize=16)

    ax3 = plt.subplot(313, sharex=ax1)
    ax3.plot(t, sig_1[2], color='blue')
    ax3.plot(t, sig_2[2], color='red')
    plt.ylabel(' Signal X_ Ch 3', fontsize=16)
    plt.xlabel('Time (s)', fontsize=16)

    plt.show(block=False)