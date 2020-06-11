import numpy as np
import matplotlib.pyplot as plt
import json

def make_scatter_plot(ox_values, oy_values, ox_name, oy_name, title, current_export_path):
    
    plt.figure(figsize=(20, 20))
    fig, ax = plt.subplots()
    
    for county in ox_values.keys():
        plt.plot(ox_values[county], oy_values[county], 'o', markersize=np.sqrt(12.))
        plt.annotate(county, (ox_values[county], oy_values[county]), fontsize = 6)

    ax.set_title(title)
    ax.set_xlabel(ox_name)
    ax.set_ylabel(oy_name)
    ax.set_xlim([0,10])
    ax.set_ylim([0,1])
    plt.savefig(current_export_path, dpi = 300)

if __name__== "__main__":
    ox = {}
    oy = {}
    ox["A"] = 1
    ox["B"] = 2
    oy["A"] = 5
    oy["B"] = 10
    title = ["alabala"]
    path = "pozatest"
    make_scatter_plot(ox, oy, "numeox", "numeoy", title, path)
