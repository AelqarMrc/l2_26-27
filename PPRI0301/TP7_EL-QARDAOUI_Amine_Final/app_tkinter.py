import tkinter as tk
from tkinter import ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from core import PenguinData

class PenguinTkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Penguin Explorer - TkInter")
        self.root.geometry("800x600")

        self.data_core = PenguinData()
        self.current_df = self.data_core.df

        self.setup_ui()
        self.update_table()

    def setup_ui(self):
        filter_frame = tk.LabelFrame(self.root, text="Filtres", padx=10, pady=10)
        filter_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(filter_frame, text="Espèce:").grid(row=0, column=0, padx=5)
        self.species_var = tk.StringVar(value="Toutes")
        species_cb = ttk.Combobox(filter_frame, textvariable=self.species_var, 
                                values=["Toutes"] + list(self.data_core.df['Species'].unique()))
        species_cb.grid(row=0, column=1, padx=5)

        tk.Label(filter_frame, text="Sexe:").grid(row=0, column=0, padx=5)
        self.sex_var = tk.StringVar(value="Tous")
        sex_cb = ttk.Combobox(filter_frame, textvariable=self.sex_var,
                            values=["Tous"] + list(self.data_core.df['Sex'].unique()))
        sex_cb.grid(row=0, column=0, padx=5)

        ttk.Button(filter_frame, text="Appliquer", command=self.apply_filters).grid(row=0, column=4, padx=10)
        ttk.Button(filter_frame, text="Voir Graphique", command=self.show_plot).grid(row=0, column=5, padx=5)
        ttk.Button(filter_frame, text="Exporter CSV", command=self.export_csv).grid(row=0, column=6, padx=5)

        cols = list(self.data_core.df.columns)
        self.tree = ttk.Treeview(self.root, columns=cols, show='headings')
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def apply_filters(self):
        self.current_df = self.data_core.filter_data(
            species=self.species_var.get(),
            sex=self.sex_var.get()
        )
        self.update_table()

    def update_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for _, row in self.current_df.iterrows():
            self.tree.insert("", "end", values=list(row))

    def show_plot(self):
        plot_window = tk.Toplevel(self.root)
        plot_window.title("Graphique Matplotlib")

        fig = self.data_core.generate_mass_histogram(self.current_df)
        canvas = FigureCanvasTkAgg(fig, master=plot_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def export_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                filetypes=[("CSV files", "*.csv")])

        if file_path:
            self.current_df.to_csv(file_path, index=False)

if __name__ == "__main__":
    root = tk.Tk()
    app = PenguinTkApp(root)
    root.mainloop()