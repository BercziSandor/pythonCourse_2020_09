# https://seaborn.pydata.org/generated/seaborn.pairplot.html
# https://stackoverflow.com/questions/28417293/sample-datasets-in-pandas

# A seaborn magasabb szintű parancsokkal teszi lehetővé a megjelenítést, mint a matplotlib,
# ezen kívül nagyon jó "beépített" adatmintái vannak kísérletezéshez.
# Érdemes megismerkedni vele, ha adatvizualizációval akarunk foglalkozni. Hátrány: még
# viszonylag sokat változik verziók között.

# Ha az ő adatmintáit akarjuk használni, akkor az irodai hálózatból a Python felhívása
# előtt ugyanúgy be kell állítani a proxy-t, mint a pip esetében, mivel ezeket a netről
# tölti le:

# SET HTTPS_PROXY=http://10.196.68.20:3128

import matplotlib.pyplot as plt
import seaborn as sns

print(sns.get_dataset_names())

# ['anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 'dots', 'exercise',
#  'flights', 'fmri', 'gammas', 'geyser', 'iris', 'mpg', 'penguins', 'planets', 'tips', 'titanic']

# Játsszunk egy kicsit a pingvinekkel, tanulmányozzuk a pairplot megjelenítés lehetőségeit.

penguins = sns.load_dataset("penguins")

#sns.pairplot(penguins)
#sns.pairplot(penguins, hue="species")
#sns.pairplot(penguins, hue="species", diag_kind="hist")
#sns.pairplot(penguins, hue="species", markers=["o", "s", "D"])
#sns.pairplot(penguins, kind="kde")

#g = sns.pairplot(penguins, kind="kde")
#g.map_lower(sns.kdeplot, levels=4, color=".2")

plt.show()
