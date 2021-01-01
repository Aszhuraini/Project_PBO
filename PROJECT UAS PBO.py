import sqlite3

connection = sqlite3.connect('laundry.db')
cursor = connection.cursor()

def register():
    global connection
    username = input("masukkan username: ")
    password = int(input("masukkan password: "))
    query = f'INSERT INTO admin(username, password) VALUES ("{username}", "{password}")'
    connection.execute(query)
    connection.commit()
    print('anda berhasil mendaftar')
    
def tambahDataPelanggan():
    global connection
    print("***MENAMBAH DATA PELANGGAN")
    nama = input('Nama pelanggan: ')
    jenis_kelamin = input('Jenis Kelamin pelanggan: ')
    umur = (input('Umur Anda: '))
    alamat = input('Alamat Anda: ')
    queryStr = f'INSERT INTO pelanggan(nama, jenis_kelamin, umur, alamat) VALUES ("{nama}", "{jenis_kelamin}", "{umur}", "{alamat}")'
    connection.execute(queryStr)
    connection.commit();
    print('data berhasil ditambah')

def dataPelanggan():
    global connection
    for row in connection.execute('SELECT * FROM pelanggan'):
        print("***MENAMPILKAN DATA PELANGGAN***")
        print(row)

def updateDataPelanggan():
    id = int(input("masukkan id pelanggan: "))
    nama = input("masukkan nama baru: ")
    jenis_kelamin = input("masukkan jenis kelamin baru: ")
    umur = int(input("masukkan umur: "))
    alamat = input("masukkan alamat: ")
    query = '''UPDATE pelanggan SET nama = ?, jenis_kelamin = ?, umur = ?, alamat = ? WHERE id = ?'''
    connection.execute(query, [nama, jenis_kelamin, umur, alamat, id])
    connection.commit()
    print('data berhasil diupdate')

def deleteDataPelanggan():
    id = int(input('masukkan id: '))
    query = f'DELETE FROM pelanggan WHERE id = ?'
    connection.execute(query, [id])
    connection.commit()
    print('data berhasil dihapus')

def tambahDataLaundry():
    global connection
    id_pelanggan = int(input('ID pelanggan: '))
    jenis_cuci = input('Pilih Laundry Kering atau Laundry Basah? : ')
    berat_baju = int(input('Berat Baju: '))
    total_baju = int(input('Banyak Baju: '))
    harga = int(input('Harga Laundry: '))
    tanggal = input('Tanggal Reservasi: ') # Y-m-d H:i:s
    query = f'INSERT INTO laundry(id_pelanggan, jenis_cuci, berat_baju, total_baju, harga, tanggal) VALUES ("{id_pelanggan}", "{jenis_cuci}", "{berat_baju}", "{total_baju}", "{harga}", "{tanggal}")'
    connection.execute(query)
    connection.commit()

def dataLaundry():
    global connection
    for row in connection.execute('SELECT * FROM laundry JOIN pelanggan on laundry.id_pelanggan = pelanggan.id'):
        print(row)

class set_login:
    def __init__(self,username = None, password = None):
        self.username = username
        self.password = password

    def set_login_admin(self):
        akun = []
        query = 'SELECT * FROM admin WHERE username = username AND password = password'
        connection.execute(query)
        connection.commit()
        result = connection.fetchone()
        if(result):
            akun.append(result)
            print("Selamat datang")
        else:
            print("Username atau password salah")
            return result

while True:

    print("-------TAMPILAN HOME LAUNDRY-------")
    print("Pilihan Menu")
    print(""" 
        1. Login
        2. Register
    """)

    pilihan = int(input("Pilihan : "))

    if (pilihan == 1):
        username = input('masukkan username anda: ')
        password = input('masukkan password: ')
        login = set_login(username, password).set_login_admin()

        print("Pilihan Menu")
        print("""
            1. Tampilkan data pelanggan
            2. Tampilkan data laundry
            3. Tambahkan data pelanggan
            4. Tambahkan data laundry
            5. Ubah data pelanggan berdasarkan id
            6. Delete data pelanggan berdasarkan id
            7. Keluar
        """)

        pilihan = int(input('Pilihan: '))

        if (pilihan == 1):
            dataPelanggan()
        elif (pilihan == 2):
            dataLaundry()
        elif (pilihan == 3):
            tambahDataPelanggan()
        elif (pilihan == 4):
            tambahDataLaundry()
        elif (pilihan == 5):
            updateDataPelanggan()
        elif (pilihan == 6):
            deleteDataPelanggan()
        elif (pilihan == 7):
            break
        else:
            print('Menu tidak valid!')

    elif (pilihan==2):
        register()
