from matplotlib import pyplot as plt
from numpy import mean, std
from numpy.random import normal
from scipy.stats import norm

# Menghasilkan sampel distribusi normal
sample = normal(loc=50, scale=5, size=1000)

# Menampilkan histogram dari sampel
plt.figure(figsize=(5, 4))
plt.hist(sample, bins=10, density=True)
plt.title('Histogram Sampel')
plt.show()

# Menghitung mean dan standard deviation dari sampel
sample_mean = mean(sample)
sample_std = std(sample)
print('Mean=%.3f, \nStandard Deviation=%.3f' % (sample_mean, sample_std))

# Membuat distribusi normal dengan mean dan std yang dihitung
dist = norm(sample_mean, sample_std)

# Menghasilkan nilai dan probabilitas yang sesuai dari distribusi
values = [value for value in range(30, 70)]
probabilitas = [dist.pdf(value) for value in values]

# Menampilkan histogram sampel dan overlay fungsi densitas probabilitas
plt.hist(sample, bins=10, density=True, alpha=0.5, label='Histogram Sampel')
plt.plot(values, probabilitas, label='Fungsi Densitas Probabilitas')
plt.title('Histogram dan FDP')
plt.legend()
plt.show()

