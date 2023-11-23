def tulis_biodata():
   
    nama = input("Nama: ")
    umur = input("Umur: ")
    alamat = input("Alamat: ")
    email = input("Email: ")
    dosen_wali = input("Dosen Wali: ")

    
    with open("Biodata.txt", "w") as file:
        file.write(f"Nama: {nama}\n")
        file.write(f"Umur: {umur}\n")
        file.write(f"Alamat: {alamat}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Dosen Wali: {dosen_wali}\n")

    print("Biodata telah berhasil disimpan.")

def baca_biodata():
    
    try:
        with open("Biodata.txt", "r") as file:
            biodata = file.read()
            print("Isi Biodata:")
            print(biodata)
    except FileNotFoundError:
        print("Biodata belum tersedia. Harap jalankan fungsi tulis_biodata terlebih dahulu.")


tulis_biodata()


baca_biodata()
def tulis_biodata():
    
    nama = input("Nama: ")
    umur = input("Umur: ")
    alamat = input("Alamat: ")
    email = input("Email: ")
    dosen_wali = input("Dosen Wali: ")

    with open("Biodata.txt", "w") as file:
        file.write(f"Nama: {nama}\n")
        file.write(f"Umur: {umur}\n")
        file.write(f"Alamat: {alamat}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Dosen Wali: {dosen_wali}\n")

    print("Biodata telah berhasil disimpan.")

def baca_biodata():
    
    try:
        with open("Biodata.txt", "r") as file:
            biodata = file.read()
            print("Isi Biodata:")
            print(biodata)
    except FileNotFoundError:
        print("Biodata belum tersedia. Harap jalankan fungsi tulis_biodata terlebih dahulu.")


tulis_biodata()


baca_biodata()
