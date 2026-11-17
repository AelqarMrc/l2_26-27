import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

class PenguinData:

    def __init__(self):
        self.url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins_raw.csv"
        self.df = pd.DataFrame()
        self.load_and_clean_data()

    def load_and_clean_data(self):
        raw_df = pd.read_csv(self.url)
        cols = ['Species', 'Island', 'Sex', 'Culmen Length (mm)', 'Body Mass (g)']
        df_clean = raw_df[cols].dropna().copy()
        self.df = df_clean

    def filter_data(self, species="Toutes", sex='Tous', min_culmen=0.0):
        filtered = self.df.copy()
        if species != "Toutes":
            filtered =filtered[filtered['Species'] == species]
        if sex != "Tous":
            filtered = filtered[filtered['Sex'] == sex]
        if min_culmen > 0 :
            filtered = filtered[filtered['Culmen Length (mm)'] >= float(min_culmen)]

        return filtered

    def get_statistics(self, df=None):
        data = self.df if df is None else df
        return data.describe()

    def generate_mass_histogram(self, df=None):
        data = self.df if df is None else df
        fig, ax = plt.subplots(figsize=(8,5))

        for species in data['Species'].unique():
            subset = data[data['Species'] == species]
            ax.hist(subset['Body Mass (g)'], alpha=0.6, label=species, bins=15)

        ax.set_title('Distribution de la masse par espèce')
        ax.set_xlabel('Masse corporelle (g)')
        ax.set_ylabel('Fréquence')    
        ax.legend()
        fig.tight_layout()

        return fig

    def get_plot_as_base64(self, fig):
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)
        return base64.b64encode(buf.read()).decode('utf-8')