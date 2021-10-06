import matplotlib.pyplot as plt
import numpy as np

# Jakub Eliasz

# funkcja
f1 = lambda x: x**2+5
	
# przedziały argumentów    
vect1 = np.linspace(-1, 1)
vect2 = np.linspace(-6, 6)
vect3 = np.linspace(0, 5)


# wykresy funkcji
fig, (axs1, axs2, axs3) = plt.subplots(1, 3)
fig.suptitle('f(x) = x^2+5')

axs1.plot(vect1, f1(vect1), label = 'x**2+5')
axs1.set_title('-1<x<1')
axs1.set_xlabel('x')
axs1.set_ylabel('y')
axs1.legend()

axs2.plot(vect2, f1(vect2), label = 'x**2+5')
axs2.set_title('-6<x<6')
axs2.set_xlabel('x')
axs2.set_ylabel('y')
axs2.legend()

axs3.plot(vect3, f1(vect3), label = 'x**2+5')
axs3.set_title('0<x<5')
axs3.set_xlabel('x')
axs3.set_ylabel('y')
axs3.legend()


plt.show()
