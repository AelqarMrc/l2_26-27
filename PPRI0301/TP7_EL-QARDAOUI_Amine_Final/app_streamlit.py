import streamlit as st
from core import PenguinData

st.set_page_config(page_title="Penguin Explorer", layout="wide")

@st.cache_data
def load_core():
    return PenguinData()

data_core = load_core()

st.title("🐧 Dashboard Palmer Penguins - Streamlit")

st.sidebar.header("Filtres")
species_list = ["Toutes"] + list(data_core.df['Species'].unique())
selected_species = st.sidebar.selectbox("Espèce", species_list)

sex_list = ["Tous"] + list(data_core.df['Sex'].unique())
selected_sex = st.sidebar.selectbox("Sexe", sex_list)

min_culmen = st.sidebar.slider("Longueur min du bec (mm)", min_value=30, max_value=60, value=30)

filtered_df = data_core.filter_data(species=selected_species, sex=selected_sex, min_culmen=min_culmen)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Aperçu des données")
    st.dataframe(filtered_df, use_container_width=True)

    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Télécharger CSV", data=csv, file_name="penguin_filtres.csv", mime="text/csv")

with col2:
    st.subheader("Statistiques")
    st.dataframe(data_core.get_statistics(filtered_df), use_container_width=True)

st.subheader("Visualisation")

fig=data_core.generate_mass_histogram(filtered_df)
st.pyplot(fig)