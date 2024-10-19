import os


class Music:
    def __init__(self, judul, penyanyi, genre):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre

    def tampilkan(self):
        return f"{self.judul:<20} {self.penyanyi:<20} {self.genre}"


class Jawa(Music):
    def __init__(self, judul, penyanyi):
        super().__init__(judul, penyanyi, "Lagu - J")


class Indo(Music):
    def __init__(self, judul, penyanyi):
        super().__init__(judul, penyanyi, "Lagu - I")


class Mancanegara(Music):
    def __init__(self, judul, penyanyi):
        super().__init__(judul, penyanyi, "Lagu - M")


class DaftarMusic:
    def __init__(self):
        self.daftarMusic = []

    def tambahLagu(self, music):
        self.daftarMusic.append(music)

    def hapusLagu(self, judul):
        self.daftarMusic = [
            lagu for lagu in self.daftarMusic if lagu.judul != judul]

    def tampilLagu(self):
        return [lagu.tampilkan() for lagu in self.daftarMusic]

    def sortAZ(self):
        self.daftarMusic.sort(key=lambda x: x.judul)

    def cariPenyanyi(self, penyanyi):
        return [lagu for lagu in self.daftarMusic if penyanyi.lower() in lagu.penyanyi.lower()]


def bersihkanLayar():
    os.system('cls' if os.name == 'nt' else 'clear')


def tampilkanMenu():
    print("===Spoti-Han | Better than Spotify===")
    print("1. Lagu Jawa")
    print("2. Lagu Indonesia")
    print("3. Lagu Mancanegara")
    print("4. Tampilkan Semua Lagu")
    print("5. Cari Lagu")
    print("0. Keluar")
    print("Masukan Pilihan Menu : ", end="")


def tampilkanSubmenu():
    print("1. Tampilkan Lagu")
    print("2. Tambah Lagu")
    print("3. Hapus Lagu")
    print("0. Kembali ke Menu Utama")
    print("Masukan Pilihan Submenu : ", end="")


def tambahLagu(daftar, jenis):
    judul = input(f"Masukkan judul lagu {jenis}: ")
    penyanyi = input("Masukkan nama penyanyi: ")
    if jenis == "Jawa":
        daftar.tambahLagu(Jawa(judul, penyanyi))
    elif jenis == "Indonesia":
        daftar.tambahLagu(Indo(judul, penyanyi))
    elif jenis == "Mancanegara":
        daftar.tambahLagu(Mancanegara(judul, penyanyi))
    print(f"Lagu {judul} berhasil ditambahkan.")


def hapusLagu(daftar):
    judul = input("Masukkan judul lagu yang akan dihapus: ")
    daftar.hapusLagu(judul)
    print(f"Lagu {judul} berhasil dihapus.")


def tampilkanLagu(daftar, jenis=None):
    daftar.sortAZ()
    if jenis:
        lagu_filtered = [
            lagu for lagu in daftar.daftarMusic if lagu.genre == f"Lagu - {jenis[0]}"]
        for lagu in lagu_filtered:
            print(lagu.tampilkan())
    else:
        for lagu in daftar.tampilLagu():
            print(lagu)


def submenu(daftar, jenis):
    while True:
        bersihkanLayar()
        print(f"=== Submenu Lagu {jenis} ===")
        tampilkanSubmenu()
        pilihan = input()

        if pilihan == "1":
            tampilkanLagu(daftar, jenis)
            input("Tekan Enter untuk kembali ke submenu...")
        elif pilihan == "2":
            tambahLagu(daftar, jenis)
            input("Tekan Enter untuk kembali ke submenu...")
        elif pilihan == "3":
            hapusLagu(daftar)
            input("Tekan Enter untuk kembali ke submenu...")
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")


def utama():
    daftar = DaftarMusic()

    daftar.tambahLagu(Jawa("Mendung Tanpo Udan", "Ndarboy Genk"))
    daftar.tambahLagu(Jawa("Los Dol", "Denny Caknan"))
    daftar.tambahLagu(Jawa("Kartoyono", "Denny Caknan"))
    daftar.tambahLagu(Jawa("Tewas Tertimbun Masa Lalu", "NDX A.K.A."))
    daftar.tambahLagu(Jawa("Sebatas Teman", "Guyon Waton"))
    daftar.tambahLagu(Indo("Duka", "Last Child"))
    daftar.tambahLagu(Indo("Kemarin", "Seventeen"))
    daftar.tambahLagu(Indo("Hati-Hati Di Jalan", "Tulus"))
    daftar.tambahLagu(Indo("Hujan", "Utopia"))
    daftar.tambahLagu(Indo("Indonesia Raya", "W.R. Soepratman"))
    daftar.tambahLagu(Mancanegara("Royalty", "Egzod"))
    daftar.tambahLagu(Mancanegara("Darkside", "Alan Walker"))
    daftar.tambahLagu(Mancanegara("On My Way", "Alan Walker"))
    daftar.tambahLagu(Mancanegara("Snap", "Rosa Linn"))
    daftar.tambahLagu(Mancanegara("Night Changes", "One Direction"))

    while True:
        bersihkanLayar()
        tampilkanMenu()
        pilihan = input()

        if pilihan == "1":
            submenu(daftar, "Jawa")
        elif pilihan == "2":
            submenu(daftar, "Indonesia")
        elif pilihan == "3":
            submenu(daftar, "Mancanegara")
        elif pilihan == "4":
            tampilkanLagu(daftar)
            input("Tekan Enter untuk kembali ke menu utama...")
        elif pilihan == "5":
            penyanyi = input("Masukkan nama penyanyi yang dicari: ")
            hasil = daftar.cariPenyanyi(penyanyi)
            if hasil:
                for lagu in hasil:
                    print(lagu.tampilkan())
            else:
                print("Penyanyi tidak ditemukan.")
            input("Tekan Enter untuk kembali ke menu utama...")
        elif pilihan == "0":
            print("Terima kasih telah menggunakan Spoti-Han!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    utama()
