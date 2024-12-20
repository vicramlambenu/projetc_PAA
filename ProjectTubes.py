import random
import matplotlib.pyplot as plt
import numpy as np

# Sesuaikan 3 digit terakhir stambuk (disimpan sebagai string)
stambuk_last_three = "005"  # Ganti dengan 3 digit terakhir stambuk Anda
max_value = 250 - int(stambuk_last_three)  # Konversi ke integer untuk operasi matematika

# Fungsi untuk menghasilkan array acak dengan panjang n
def generate_array(n, seed=42):
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]

# Fungsi untuk memeriksa apakah elemen dalam array unik
def is_unique(arr):
    return len(arr) == len(set(arr))

# Fungsi untuk menghitung worst case dan average case
def calculate_cases(array_sizes, trials=100):
    worst_cases = []
    average_cases = []

    for n in array_sizes:
        unique_counts = []

        for _ in range(trials):
            arr = generate_array(n)
            unique_counts.append(len(set(arr)))

        # Worst case: semua elemen tidak unik (maksimum pengulangan)
        worst_case = n - max(unique_counts)
        # Average case: rata-rata elemen yang unik
        average_case = n - np.mean(unique_counts)

        worst_cases.append(worst_case)
        average_cases.append(average_case)

    return worst_cases, average_cases

# Nilai-nilai n yang digunakan
array_sizes = [100, 150, 200, 250, 300, 350, 400, 500]

# Hitung worst case dan average case
worst_cases, average_cases = calculate_cases(array_sizes)

# Simpan hasil ke dalam file
with open("worst_avg.txt", "w") as f:
    f.write("Array Size\tWorst Case\tAverage Case\n")
    for i, n in enumerate(array_sizes):
        f.write(f"{n}\t{worst_cases[i]}\t{average_cases[i]:.2f}\n")

# Plot grafik
plt.figure(figsize=(10, 6))
plt.plot(array_sizes, worst_cases, label='Worst Case', marker='o', color='red')
plt.plot(array_sizes, average_cases, label='Average Case', marker='s', color='blue')
plt.title('Worst Case vs Average Case for Unique Element Check')
plt.xlabel('Array Size (n)')
plt.ylabel('Number of Non-Unique Elements')
plt.legend()
plt.grid()

# Simpan plot sebagai file PDF dan JPG
plt.savefig("unique_case_plot.jpg")
plt.show()
