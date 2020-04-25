import os
import sys
import geopandas
import fiona
import pandas
import matplotlib.pyplot as plt
import descartes
from create_stats.county_information import get_county_means
from pathlib import Path
import pandas as pd

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append( os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )

def create_map(df):
    file = "C:/Users/Octa/Desktop/EducationAnalytica-master/ro_judete_poligon.shp"
    df.columns = ["index","mnemonic","medie"]
    map_df = geopandas.read_file(file)
    centroids = map_df.geometry.centroid
    centroids.append(df['mnemonic'])
    map_df = map_df.merge(df, on='mnemonic')
    map_df['coords']=map_df['geometry'].apply(lambda x: x.representative_point().coords[:])
    map_df['coords'] = [coords[0] for coords in map_df['coords']]

    variable ='medie'
    vmin=min(df['medie'])
    vmax=max(df['medie'])
    fig, ax = plt.subplots(1, figsize=(10, 6))
    map_df.plot(column=variable,cmap='Reds', linewidth = 0.8, ax = ax, edgecolor ='0.8')
    for idx, row in map_df.iterrows():
        plt.annotate(s=str(row['mnemonic']), xy=row['coords'], horizontalalignment='center')
    ax.axis('off')
    # add a title
    ax.set_title('Medie bacalaureat 2019', fontdict = {'fontsize': '25', 'fontweight': '3'})
    # create an annotation for the data source
    ax.annotate('Source:Ministerul Educatiei, 2019', xy = (0.1, .08), xycoords ='figure fraction', horizontalalignment ='left', verticalalignment ='top',
    fontsize = 12)
    # Create colorbar as a legend
    sm = plt.cm.ScalarMappable(cmap='Reds', norm = plt.Normalize(vmin=vmin, vmax=vmax))
    # empty array for the data range
    sm._A = []
    # add the colorbar to the figure
    cbar = fig.colorbar(sm)
    plt.savefig("C:/Users/Octa/Desktop/EducationAnalytica-master/maps/MediiJudete2019.png", dpi = 300)
    plt.show()

if __name__== "__main__":
    dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    input_csv_means = Path("../Tables/CountyMeans.xlsx")
    df =pd.read_excel(input_csv_means,sheet_name = "2019")
    df = pd.DataFrame(df)
    create_map(df)