import matplotlib.pyplot as plt
import numpy as np

plt.style.use('classic')

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.show() # egy szkriptben csak egyszer használjuk!

####################################

# Két diagram:

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

plt.style.use('classic')

plt.figure() # create a plot figure

plt.subplot(2, 1, 1) # (rows, columns, panel number)
plt.plot(x, np.sin(x))
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x));

plt.show()

####################################
