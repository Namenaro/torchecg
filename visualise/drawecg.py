import matplotlib.pyplot as plt
import numpy as np

def draw12leads(leads, start=0, end=4999):
    numleads = len(leads)
    print (numleads)
    if numleads==0:
        print ("here problem with visualising ecg")
        return
    fig, axs = plt.subplots(10, 1, figsize=(15, 15), sharex=True, sharey=True)


    axs = axs.ravel()

    for i in range(10):
        axs[i].plot(leads[i][start:end])
        axs[i].set_title(str(i))
    plt.show()