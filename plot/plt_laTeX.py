import matplotlib.pyplot as plt
import numpy as np

def slika(amplituda = 1, fr = 10, faza = 0, dusenje = 0.):
    t = np.linspace(0, 1 , 200)
    f = amplituda * np.sin(2*np.pi*fr*t - faza) * np.exp(-dusenje*2*np.pi*fr*t)
    plt.plot(t, f, 'r', linewidth = 2, label='sinus')

    plt.ylim(-5, 5)
    plt.title('podpora za LaTeX: $t^2$, $\\sqrt{\\frac{a}{b}}$, $E=mc^2$, $sin(\\alpha)$')
    plt.ylabel('amplituda')
    plt.xlabel('čas')
    plt.grid()
    plt.legend()

    plt.show()

slika(amplituda = 5, dusenje = 0.08, fr = 5, faza = -np.pi/2)