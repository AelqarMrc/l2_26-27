from flask import Flask, render_template, request, Response
from core import PenguinData

app = Flask(__name__)
data_core = PenguinData()

@app.route("/", methods=["GET", "POST"])
def index():
    species_filter = request.form.get("species", "Toutes")

    filtered_df = data_core.filter_data(species=species_filter)

    stats_html = data_core.get_statistics(filtered_df).to_html(classes="table table-striped")
    data_html = filtered_df.head(50).to_html(classes="table table-hover", index=False)

    fig = data_core.generate_mass_histogram(filtered_df)
    plot_base64 = data_core.get_plot_as_base64(fig)

    species_list = ["Toutes"] + list(data_core.df['Species'].unique())

    return render_template("index.html",
                           stats = stats_html,
                           table=data_html,
                           plot=plot_base64,
                           species_list=species_list,
                           selected_species=species_filter)

if __name__ == "__main__":
    app.run(debug=True)

