def hitung_total_harga(jumlah_barang):
    total = 0
    for i in range(jumlah_barang):
        harga_barang = float(input(f"Masukkan harga barang ke-{i+1}: "))
        total += harga_barang
    return total

jumlah_barang = int(input("Masukkan jumlah barang: "))
total_harga = hitung_total_harga(jumlah_barang)

print(f"Total harga belanjaan adalah: {total_harga}")