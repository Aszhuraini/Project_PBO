import sqlite3
import os

connection = sqlite3.connect('coba.db')
cursor = connection.cursor()

class data_manager():
    def __init__(self):
        self.con = sqlite3.connect("coba.sqlite")
        self.cursor = self.con.cursor() #mengeksekusi perintah sql pd basisdata sqllite
    def exe_query(self, query):
        self.cursor.execute(query)
        self.con.commit()

class table(data_manager):
    def create_table_pelanggan(self):
        self.query = """CREATE TABLE "pelanggan" (
            "id_pelanggan" INTEGER NOT NULL UNIQUE,
            "nama_pelanggan" TEXT NOT NULL,
            "jenis_kelamin"	TEXT NOT NULL,
            "umur" INTEGER NOT NULL,
            "nomor_telepon" INTEGER NOT NULL,
            "alamat" TEXT NOT NULL,
            FOREIGN KEY("id_admin") REFERENCES "admin",
            PRIMARY KEY("id_pelanggan" AUTOINCREMENT))"""
        self.exe_query(self.query)

    def create_table_admin(self):
        self.query = """CREATE TABLE "admin" (
            "id_admin" INTEGER NOT NULL UNIQUE,
            "nama_admin" TEXT NOT NULL,
            "username" TEXT NOT NULL,
            "password" INTEGER NOT NULL,
            PRIMARY KEY ("id_admin" AUTOINCREMENT))"""
        self.exe_query(self.query)

    def create_table_laundry(self):
        self.query = """CREATE TABLE "laundry" (
            "id_laundry" INTEGER NOT NULL UNIQUE,
            "id_admin" INTEGER NOT NULL,
            "id_pelanggan" INTEGER NOT NULL,
            "jenis_cuci" text NOT NULL,
            "berat_baju" INTEGER NOT NULL,
            "total_baju" INTEGER NOT NULL,
            "harga"	INTEGER NOT NULL,
            "tanggal" DATE TIME NOT NULL,
            FOREIGN KEY("id_admin") REFERENCES "admin",
            FOREIGN KEY("id_pelanggan") REFERENCES "pelanggan",
            PRIMARY KEY("id_laundry" AUTOINCREMENT))"""
        self.exe_query(self.query)

# run the code to make the table
#create_table = table()
#create_table.create_table_admin()
#create_table.create_table_pelanggan()
#create_table.create_table_laundry()

class register (data_manager):
    def register_admin(self):
        self.__nama_admin = input("masukkan nama: ")
        self.__username = input("masukkan username: ")
        self.__password = int(input("masukkan password: "))
        self.query = 'INSERT INTO admin(nama_admin, username, password) VALUES (?, ?, ?)'
        self.cursor.execute(self.query, [self.__nama_admin, self.__username, self.__password])
        self.con.commit()
        self.con.close()
        print('data berhasil didaftarkan')

akun = []
class set_login(data_manager):
    def __init__(self, username = None, password = None):
        self.username = username
        self.password = password
    def set_login_admin(self):
        query = 'SELECT username, password FROM admin WHERE username = ? AND password = ?'
        cursor.execute(query, [self.username, self.password])
        connection.commit()
        result = cursor.fetchone()
        if(result):
            akun.append(result)
            print("Selamat datang")
        else:
            print("Username atau password salah")
            return result
        connection.close()

class admin(register):

    def get_data_admin(self):
        print('*** MELIHAT DATA ADMIN ***')
        self.query = '''SELECT * FROM admin'''
        self.cursor.execute(self.query)
        self.con.commit()
        self.all_results = self.cursor.fetchall()
        for result in self.all_results:
            print(result)
        self.con.close()

    def update_data_admin(self):
        print('*** MENGUBAH DATA ADMIN ***')
        username = input("masukkan username yang ingin diubah: ")
        self.__nama_admin = input("masukkan nama baru: ")
        self.__username = input("masukkan username baru: ")
        self.__password = int(input("masukkan password baru: "))
        self.query = '''UPDATE admin SET nama_admin = ?, username = ?, password = ? WHERE username = ?'''
        self.cursor.execute(self.query, [self.__nama_admin, self.__username, self.__password, username])
        self.con.commit()
        self.con.close()
        print('Data Berhasil Diubah')
    
    def delete_data_admin(self):
        id_admin = int(input('masukkan id: '))
        self.query = f'DELETE FROM admin WHERE id_admin = ?'
        self.con.execute(self.query, [id_admin])
        self.con.commit()
        print('Data Berhasil Dihapus')
    
    def tambah_data_pelanggan(self):
        print("***MENAMBAH DATA PELANGGAN***")
        self.__nama = input('Nama pelanggan: ')
        self.__jenis_kelamin = input('Jenis Kelamin pelanggan: ')
        self.__umur = int(input('Umur Pelanggan: '))
        self.__nomor_telepon = int(input('Nomor Telepon Pelanggan: '))
        self.__alamat = input('Alamat Pelanggan: ')
        self.query = 'INSERT INTO pelanggan(nama, jenis_kelamin, umur, nomor_telepon, alamat) VALUES (?, ?, ?, ?, ?)'
        self.cursor.execute(self.query, [self.__nama, self.__jenis_kelamin, self.__umur, self.__nomor_telepon, self.__alamat])
        self.con.commit()
        print('Data Pelanggan Berhasil Ditambah')

    def get_data_pelanggan(self):
        self.query = '''SELECT * FROM pelanggan'''
        self.cursor.execute(self.query)
        self.con.commit()
        self.all_results = self.cursor.fetchall()
        for result in self.all_results:
            print(result)
        self.con.close()

    def update_data_pelanggan(self):
        id_pelanggan = int(input("masukkan id pelanggan: "))
        self.__nama = input("masukkan nama baru: ")
        self.__jenis_kelamin = input("masukkan jenis kelamin baru: ")
        self.__umur = int(input("masukkan umur: "))
        self.__nomor_telepon = int(input("masukkan nomor hp baru : "))
        self.__alamat = input("masukkan alamat baru : ")
        self.query = '''UPDATE pelanggan SET nama_pelanggan = ?, jenis_kelamin = ?, umur = ?, nomor_telepon = ?, alamat = ? WHERE id_pelanggan = ?'''
        self.cursor.execute(self.query, [self.__nama, self.__jenis_kelamin, self.__umur, self.__nomor_telepon, self.__alamat, id_pelanggan])
        self.con.commit()
        print('Data Berhasil Diupdate')

    def delete_data_pelanggan(self):
        id_pelanggan = int(input('masukkan id: '))
        self.query = f'DELETE FROM pelanggan WHERE id_pelanggan = ?'
        self.con.execute(self.query, [id_pelanggan])
        self.con.commit()
        print('Data Berhasil Dihapus')
    
    def tambah_data_laundry(self):
        id_pelanggan = int(input('ID Pelanggan: '))
        self.__jenis_cuci = input('Pilih Laundry Kering atau Laundry Basah? : ')
        self.__berat_baju = int(input('Berat Baju: '))
        self.__total_baju = int(input('Banyak Baju: '))
        self.__harga = int(input('Harga Laundry: '))
        self.__tanggal = int(input('Tanggal Reservasi: ')) # Y-M-D H:I:S
        self.query = 'INSERT INTO laundry(jenis_cuci, berat_baju, total_baju, harga, tanggal) VALUES (?, ?, ?, ?, ?, ?) WHERE id_pelanggan = ?'
        self.con.execute(self.query, [self.__jenis_cuci, self.__berat_baju, self.__total_baju, self.__harga, self.__tanggal, id_pelanggan])
        self.con.commit()

    def get_data_laundry(self):
        self.query = '''SELECT * FROM laundry JOIN pelanggan on laundry.id_pelanggan = pelanggan.id'''
        self.cursor.execute(self.query)
        self.con.commit()
        self.all_results = self.cursor.fetchall()
        for result in self.all_results:
            print(result)

    def delete_data_laundry(self):
        id_pelanggan = int(input('masukkan id: '))
        self.query = f'DELETE FROM laundry WHERE id_pelanggan = ?'
        self.con.execute(self.query, [id_pelanggan])
        self.con.commit()
        print('Data Berhasil Dihapus')

#register().register_admin() 
#register().get_data_admin() 
#register().update_data_admin()
#admin().tambah_data_pelanggan()
#admin().get_data_pelanggan()

clear = lambda: os.system('cls')
def main():
    start = True
    while start:
        print('''                           *****HOME LAUNDRY*****
    Pilih menu:
    Apakah Sudah Punya Akun?
    1. Login
    Apakah Belum Punya Akun?
    2. Registrasi''')
        pilihan = input('masukkan pilihan anda: ')
        if pilihan == '1':
            username = input('masukkan username anda: ')
            password = input('masukkan password: ')
            login = set_login(username, password).set_login_admin()
            while True:
                print("-----Pilihan Menu*****")
                print("""
                    1. Tampilkan data pelanggan
                    2. Tampilkan data laundry
                    3. Tambahkan data pelanggan
                    4. Tambahkan data laundry
                    5. Update data pelanggan berdasarkan id
                    6. Delete data pelanggan berdasarkan id
                    7. Tampilkan data admin
                    8. Update data admin berdasarkan id
                    9. Delete data admin berdasarkan id
                    10. Keluar
                """)
                pilih_menu = input('masukkan pilihan anda: ')
                if pilih_menu == '1':
                    admin().get_data_pelanggan()
                elif pilih_menu == '2':
                    admin().get_data_laundry()
                elif pilih_menu == '3':
                    admin().tambah_data_pelanggan()
                elif pilih_menu == '4':
                    admin().tambah_data_laundry()
                elif pilih_menu == '5':
                    admin().update_data_pelanggan()   
                elif pilih_menu == '6':
                    admin().delete_data_pelanggan()
                elif pilih_menu == '7':
                    admin().get_data_admin()
                elif pilih_menu == '8':
                    admin().update_data_admin()
                elif pilih_menu == '9':
                    admin().delete_data_admin()
                elif pilih_menu == '10':
                    exit()
                    clear()
                else:
                    print('pilihan tidak ada')

        elif pilihan == '2':
            register().register_admin()  
        else:
            print('menu tidak ada')
    return False

#main()
admin().get_data_admin()