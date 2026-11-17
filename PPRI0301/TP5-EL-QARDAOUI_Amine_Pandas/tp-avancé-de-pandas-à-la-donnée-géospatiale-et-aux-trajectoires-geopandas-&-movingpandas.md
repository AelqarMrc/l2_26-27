# TP avancé : De pandas à la donnée géospatiale et aux trajectoires


## Prérequis techniques


Remarque : MovingPandas s'appuie sur GeoPandas, qui s'appuie sur pandas. Un GeoDataFrame est un DataFrame dont une colonne (nommée `geometry`) contient des objets géométriques (points, lignes, polygones) décrits par la bibliothèque shapely. Toutes les méthodes pandas (loc, groupby, merge, apply...) restent utilisables. C'est ce fil rouge qui structure tout le TP : ne jamais perdre de vue que sous chaque GeoDataFrame il y a un DataFrame.

---

## Partie A — Découverte de GeoPandas (exercices progressifs)


### A.0 — Mise en place : un DataFrame devient géographique

Construisez à la main, dans une cellule, un DataFrame pandas listant 8 villes avec leurs coordonnées décimales : Paris (48.85, 2.35), Marseille (43.30, 5.37), Lyon (45.76, 4.84), Lille (50.63, 3.06), Brest (48.39, -4.49), Strasbourg (48.57, 7.75), Nice (43.70, 7.27), Perpignan (42.70, 2.90). Ajoutez une colonne `population` de valeurs plausibles.

1. Transformez ce DataFrame en `gpd.GeoDataFrame` avec `gpd.points_from_xy(longitude, latitude)`, en précisant `crs="EPSG:4326"`.
2. Vérifiez avec `type(df)`, `df.geometry`, `df.crs`. Qu'observez-vous de différent par rapport à un DataFrame classique ? Quel est le rôle de la colonne spéciale `geometry` ?
3. Affichez `df.plot()`, puis `df.plot(column="population", legend=True, markersize=...)`.

### A.1 — Le piège des projections 

Les coordonnées EPSG:4326 sont des degrés. Toute mesure de distance ou de surface en degrés est fausse.

1. Projetez le GeoDataFrame en Lambert conforme : `df_l93 = df.to_crs("EPSG:2154")` (projection officielle française).
2. Calculez la distance Paris–Marseille dans les deux CRS (`df.geometry.distance()`). Comparez à la valeur attendue (environ 660 km). Expliquez l'écart observé en degrés.
3. Règle à retenir : on stocke en 4326, on calcule dans une projection métrique adaptée à la zone d'étude.

### A.2 — Requêtes spatiales : le point d'intérêt et le rayon de couverture

1. Créez un point représentant une antenne de couverture près de Lyon (45.75, 4.85), projetez-le en EPSG:2154.
2. Générez un tampon de 400 km autour de l'antenne (`buffer(400_000)`). Combien de villes du DataFrame sont couvertes ?
3. Faites-le de deux façons : (a) test géométrique booléen avec `df_l93.geometry.within(buffer)` combiné au filtrage pandas ; (b) jointure spatiale `gpd.sjoin(df_l93, antennes_gdf, predicate="within")`. Comparez les deux approches : quand la jointure spatiale devient-elle indispensable ?

### A.3 — Un mini-réseau : points vers lignes et polygones

1. Construisez une ligne Paris → Lyon → Marseille (`shapely.LineString` à partir des points), mesurez sa longueur. Discutez : pourquoi une ligne « droite » entre deux villes ne correspond pas à une distance routière ?
2. Créez le polygone (triangle) Paris–Lille–Strasbourg, calculez son aire en km² dans le bon CRS.
3. Exportez le GeoDataFrame complet en `GeoPackage` (`to_file("villes.gpkg")`), puis relisez-le. Vérifiez que le CRS a été conservé.

### A.4 — Cartographie interactive

1. Utilisez `df.explore(column="population", tiles="CartoDB positron")` pour produire une carte folium interactive.
2. Superposez le tampon de l'exercice A.2 sur la carte (folium accepte un GeoDataFrame converti en GeoJSON, ou passez par `folium.GeoJson`).

Compétences validées en fin de partie A : construction d'un GeoDataFrame, gestion des CRS, mesures métriques, tampons, jointures spatiales, export et cartographie.

---

## Partie B — Découverte de MovingPandas : trajectoires synthétiques

MovingPandas manipule des trajectoires : des séquences de positions horodatées. Vous allez générer vous-mêmes trois petites trajectoires simulées, ce qui évite tout « exemple prêt à l'emploi » et vous oblige à comprendre la structure attendue des données.

### B.1 — Génération de trois objets mobiles

Simulez trois navires fictifs partant de Brest, Cherbourg et Bordeaux, chacun avec 60 positions relevées toutes les heures. Pour chaque navire, dessinez une trajectoire en ligne droite (cap constant, vitesse propre) avec du bruit gaussien ajouté aux positions. Stockez le tout dans un DataFrame pandas long : colonnes `navire_id` (A, B, C), `time` (pandas Timestamp, fréquence horaire), `lon`, `lat`. Concaténez le tout.

1. Convertissez en GeoDataFrame (EPSG:4326) avec un index temporel : `gdf = gdf.set_index("time")`.
2. Créez une collection : `tc = mpd.TrajectoryCollection(gdf, "navire_id")`. Combien de trajectoires détecte-t-elle ? Pourquoi l'index temporel est-il obligatoire ?

### B.2 — Caractéristiques de mouvement

1. Calculez la vitesse : `tc.add_speed()`. Par défaut, pour un CRS géographique, la vitesse est en mètres par seconde ; convertissez-la en nœuds dans une colonne dérivée. La vitesse calculée correspond-elle à celle que vous avez simulée ? Quantifiez l'erreur due au bruit.
2. Calculez le cap : `tc.add_heading()`. Comparez au cap théorique de chaque navire. Expliquez pourquoi le cap instantané est très sensible au bruit de position, et proposez une méthode de lissage (par exemple une moyenne mobile sur les caps, en tenant compte de la circularité des angles).
3. Pour chaque navire : durée totale, distance parcourue (`get_length()` sur chaque trajectoire), vitesse moyenne.

### B.3 — Extraire de l'information des trajectoires

1. `tc.get_start_locations()` : récupérez les points de départ. Quelles colonnes sont conservées ?
2. Extraites les segments de trajectoire passant dans une zone : créez le polygone « Golfe de Gascogne » (rectangle approximatif en lat/lon), puis explorez la méthode de découpage de trajectoires (`clip` sur la collection). Pour chaque navire, déterminez le temps passé dans la zone.
3. Détection de comportement : identifiez, pour le navire B, les périodes où sa vitesse passe sous 1 nœud (stationnaire). Enrichissez le DataFrame des trajectoires et filtrez avec les outils pandas habituels — c'est le cœur du message du TP : l'analyse de mouvement se fait in fine en pandas.

---

## Partie C — Étude de cas : les cyclones tropicaux atlantiques (HURDAT2)

### C.0 — Le jeu de données

HURDAT2 est la base « best track » du National Hurricane Center : pour chaque cyclone tropical ou subtropical du bassin atlantique depuis 1851, des relevés toutes les 6 heures (position, vent maximal, pression centrale). Le fichier texte et son format sont décrits sur la page HURDAT du NHC (nhc.noaa.gov/data/hurdat) — téléchargez la version courante (le nom de fichier intègre la dernière année de révision, il change à chaque mise à jour annuelle).

### C.1 — Parsing : réinvestissement pandas (difficulté principale)

Le format est inhabituel et c'est voulu : il ne se lit pas avec un simple `read_csv`.

- Chaque cyclone commence par une ligne d'en-tête : nom, nombre d'enregistrements.
- Suivent n lignes de relevés : date (YYYYMMDDHH), identifiant d'événement, statut du système (`HU` ouragan, `TS` tempête tropicale, `TD` dépression, `EX` extratropical, `LO` low...), latitude suffixée (`28.7N`), longitude suffixée (`46.4W` — attention, ouest positive), vent maximal en nœuds, pression.

Consignes :

1. Écrivez un parseur (une boucle avec `read_csv` ligne à ligne, ou `skiprows` bien réfléchi, ou une lecture complète en lignes puis un traitement vectorisé). Interdiction d'utiliser un parseur HURDAT existant trouvé sur Internet : c'est l'exercice.
2. Produisez un DataFrame long avec colonnes : `storm_id`, `name`, `datetime`, `status`, `wind_kt`, `pressure`, `lat` (float, signée), `lon` (float, signée, ouest négatif).
3. Contrôlez votre parsing : nombre de cyclones, date couverte, gestion des ouragans de nom `UNNAMED` en XIXe siècle, valeurs manquantes (-99). Documentez vos choix de nettoyage.

### C.2 — Passage à GeoPandas

1. Convertissez en GeoDataFrame (EPSG:4326) puis projetez en une projection métrique adaptée à l'Atlantique nord (par exemple EPSG:326xx par zone UTM, ou une projection équidistante : discutez ce choix et ses limites pour des objets couvrant 50° de latitude).
2. Cartographiez tous les relevés de statut `HU` (ouragan) depuis 1950. Faites un groupby pandas sur l'année : y a-t-il une tendance apparente du nombre de jours-ouragan ? Attention à ne pas conclure trop vite : le nombre de relevés dépend des pratiques d'enregistrement.

### C.3 — Passage à MovingPandas

1. Filtrez la base aux cyclones postérieurs à 1970 (données plus homogènes), créez la `TrajectoryCollection` avec `storm_id` comme identifiant de trajectoire.
2. Calculez vitesse et cap par trajectoire. Comparez la vitesse « best track » calculée à la climatologie connue : un ouragan se déplace typiquement à 15–25 km/h en translation. Vos résultats sont-ils plausibles ?
3. Question scientifique 1 : les ouraganés (tempête vers ouragan, changement de statut) sont-ils associés à une accélération ou un ralentissement de translation ? Utilisez un join pandas entre les relevés et le statut précédent/suivant.
4. Question scientifique 2 : identification des zones de recurvation (le cap change d'est vers nord-ouest/nord-est). Proposez une heuristique basée sur `heading` et testez-la sur un ouragan connu (par exemple Katrina 2005, Sandy 2012, ou un ouragan récent au choix).


### C.4 — Bonus (pour aller plus loin)

- Agrégation de trajectoires : étudiez la documentation de `TrajectoryAggregator` et produisez une carte des corridors de déplacement des cyclones de catégorie 3+.
- Carte interactive `explore()` colorée par vitesse de translation, par saison.
- Comparaison avec la base HURDAT2 Pacifique (même format) : la vitesse de translation diffère-t-elle entre bassins ?



## Pièges à anticiper 
- Longitude ouest positive dans HURDAT2 : indispensable de rendre le signe négatif, sinon toutes les trajectoires partent vers l'Afrique.
- Index temporel dupliqué entre trajectoires : MovingPandas exige des trajectoires identifiables ; l'index doit être trié.
- Vitesse calculée par MovingPandas en m/s sur EPSG:4326 : bien lire la documentation des unités avant de comparer aux nœuds.
- Ne pas confondre vent maximal (intensité du cyclone, en nœuds) et vitesse de translation.
- Buffer/sjoin en degrés : toujours projeter avant tout calcul métrique.