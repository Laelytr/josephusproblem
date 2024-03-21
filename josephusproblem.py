def main():
    """
    Menjalankan simulasi permainan Josephus.
    """

    # Meminta input jumlah orang dan langkah pembunuhan dari pengguna
    jumlah_orang = int(input("Masukkan jumlah orang dalam lingkaran: "))
    langkah = int(input("Masukkan langkah pembunuhan: "))

    # Menghitung orang yang selamat
    pemenang = josephus(jumlah_orang, langkah)

    # Menampilkan hasil
    print("Orang terakhir yang tersisa adalah orang pada posisi", pemenang)

def josephus(n, k):
    """
    Menemukan orang yang selamat dalam permainan Josephus.

    Args:
        n (int): Jumlah orang dalam lingkaran.
        k (int): Langkah pembunuhan.

    Returns:
        int: Posisi orang yang selamat.
    """

    # Membuat daftar orang dari 1 hingga n
    orang = list(range(1, n + 1))

    # Inisialisasi indeks awal
    indeks = 0

    # Looping selama masih ada lebih dari satu orang
    while len(orang) > 1:
        # Menghitung indeks orang yang akan dieleminasi
        # Rumus: (indeks saat ini + langkah - 1) modulo jumlah orang
        indeks = (indeks + k - 1) % len(orang)

        # Menghapus orang yang dieliminasi dari daftar
        orang.pop(indeks)

    # Mengembalikan posisi orang yang selamat
    return orang[0]

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
