import numpy as np
import matplotlib.pyplot as plt

# Parameter Dasar
kVp = 80  # Tegangan dalam kV (bisa diubah)
mA = 10   # Arus dalam miliampere (bisa diubah)
jarak = 10  # Panjang tabung X-ray (cm)

# Fungsi untuk menghitung energi elektron
def energi_elektron(kVp):
    q = 1.6e-19  # Muatan elektron (Coulomb)
    V = kVp * 1000  # Konversi ke Volt
    E = q * V  # Energi elektron dalam Joule
    return E

# Fungsi untuk visualisasi lintasan elektron
def lintasan_elektron(kVp, mA, jarak):
    x = np.linspace(0, jarak, 100)  # Lintasan horizontal
    y = -0.05 * x**2  # Lintasan vertikal sederhana (parabola)
    
    energi = energi_elektron(kVp)
    
    # Plot lintasan
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f"Lintasan Elektron (kVp={kVp}, mA={mA})", color="blue")
    plt.title(f"Simulasi Lintasan Elektron dalam Tabung X-ray\nEnergi Elektron: {energi:.2e} Joule")
    plt.xlabel("Jarak Horizontal (cm)")
    plt.ylabel("Jarak Vertikal (cm)")
    plt.legend()
    plt.grid()
    plt.show()

# Menjalankan Simulasi
lintasan_elektron(kVp, mA, jarak)
# Input manual untuk kVp dan mA
kVp = float(input("Masukkan nilai kVp (tegangan): "))
mA = float(input("Masukkan nilai mA (arus): "))

# Menjalankan simulasi dengan input pengguna
lintasan_elektron(kVp, mA, jarak)
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact

# Fungsi visualisasi
def lintasan_interaktif(kVp=80, mA=10):
    x = np.linspace(0, 10, 100)
    y = -0.05 * x**2
    
    energi = (kVp)
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f"Lintasan Elektron\nkVp={kVp}, mA={mA}")
    plt.title(f"Simulasi Tabung X-ray | Energi: {energi:.2e} Joule")
    plt.xlabel("Jarak Horizontal (cm)")
    plt.ylabel("Lintasan Vertikal (cm)")
    plt.legend()
    plt.grid()
    plt.show()

# Slider Interaktif
interact(lintasan_interaktif, kVp=(50, 150, 10), mA=(5, 50, 5))