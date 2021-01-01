import sqlite3

class data_manager():
    def __init__(self):
        self.con = sqlite3.connect("laundry.sqlite")
        self.cursor = self.con.cursor() #mengeksekusi perintah sql pd basisdata sqllite
    def exe_query(self, query):
        self.cursor.execute(query)
        self.con.commit()

class table(data_manager):
    def create_table_pelanggan(self):
        self.query = """CREATE TABLE "pelanggan"(
            "id" INTEGER NOT NULL UNIQUE,
            "nama_pelanggan" TEXT NOT NULL,
            "alamat" TEXT NOT NULL,
            "no_hp" TEXT NOT NULL,
            PRIMARY KEY ("id" AUTOINCREMENT))"""
        self.exe_query(self.query)

    def create_table_work_order(self):
        self.query = """CREATE TABLE "work_order"(
            "id" INTEGER NOT NULL UNIQUE,
            "pelanggan" TEXT NOT NULL,
            "work" TEXT NOT NULL,
            "tanggal" TEXT NOT NULL,
            "pembayaran" TEXT NOT NULL,
            "status" TEXT NOT NULL,
            "id_pelanggan" INTEGER NOT NULL,
            "id_pembayaran" INTEGER NOT NULL,
            "id_status" INTEGER NOT NULL,
            FOREIGN KEY ("id_pelanggan") REFERENCES "pelanggan"("id"),
            FOREIGN KEY ("id_pembayaran") REFERENCES "pembayaran"("id"),
            FOREIGN KEY ("id_status") REFERENCES "status_pekerjaan"("id"),
            PRIMARY KEY ("id" AUTOINCREMENT))"""
        self.exe_query(self.query)

    def create_table_work(self):
        self.query = """CREATE TABLE "work"(
            "id" INTEGER NOT NULL UNIQUE,
            "total_harga" INTEGER NOT NULL,
            "item_pakaian" TEXT NOT NULL,
            "jenis_work" TEXT NOT NULL,
            "kategori" TEXT NOT NULL,
            "id_pelanggan" INTEGER NOT NULL,
            "id_pakaian" INTEGER NOT NULL,
            "id_kategori" INTEGER NOT NULL,
            "id_jenis_work" INTEGER NOT NULL,
            FOREIGN KEY ("id_pelanggan") REFERENCES "pelanggan"("id"),
            FOREIGN KEY ("id_pakaian") REFERENCES "pakaian"("id"),
            FOREIGN KEY ("id_kategori") REFERENCES "kategori"("id"),
            FOREIGN KEY ("id_jenis_work") REFERENCES "jenis_work"("id"),
            PRIMARY KEY ("id" AUTOINCREMENT))"""
        self.exe_query(self.query)
    
    def create_table_jenis_work(self):
        self.query = """CREATE TABLE "jenis_work"(
            "id" INTEGER NOT NULL UNIQUE,
            "express" BO0LEAN NOT NULL,
            "slow" BOOLEAN NOT NULL,
            PRIMARY KEY ("id" AUTOINCREMENT))"""
        self.exe_query(self.query)
    
    def create_table_pakaian(self):
        self.query = """CREATE TABLE "pakaian"(
            "id" INTEGER NOT NULL UNIQUE,
            "total_berat" INTEGER NOT NULL,
            PRIMARY KEY ("id" AUTOINCREMENT))"""
        self.exe_query(self.query)

    def create_table_kategori(self):
        self.query = """CREATE TABLE "kategori"(
            "id" INTEGER NOT NULL UNIQUE,
            "cuci_basah" BOOLEAN NOT NULL,
            "cuci_kering" BOOLEAN NOT NULL,
            PRIMARY KEY ("id" AUTOINCREMENT))"""
        self.exe_query(self.query)

    def create_table_pembayaran(self):
        self.query = """CREATE TABLE "pembayaran"(
            "id" INTEGER NOT NULL UNIQUE,
            "total_harga" INTEGER NOT NULL,
            "tanggal" TEXT NOT NULL,
            "id_pelanggan" INTEGER NOT NULL,
            "id_work" INTEGER NOT NULL,
            "nomor_kartu" INTEGER NOT NULL,
            "id_cash" INTEGER NOT NULL,
            FOREIGN KEY ("id_pelanggan") REFERENCES "pelanggan"("id"),
            FOREIGN KEY ("id_work") REFERENCES "work"("id"),
            FOREIGN KEY ("nomor_kartu") REFERENCES "pembayaran_kredit"("id"),
            FOREIGN KEY ("id_cash") REFERENCES "pembayaran_cash"("id"),
            PRIMARY KEY ("id" AUTOINCREMENT))"""
        self.exe_query(self.query)

    def create_table_pembayaran_cash(self):
        self.query = """CREATE TABLE "pembayaran_cash"(
            "id" INTEGER NOT NULL UNIQUE,
            PRIMARY KEY ("id" AUTOINCREMENT))"""
        self.exe_query(self.query)

    def create_table_pembayaran_kredit(self):
        self.query = """CREATE TABLE "pembayaran_kredit"(
            "nomor_kartu" INTEGER NOT NULL UNIQUE,
            PRIMARY KEY ("nomor_kartu" AUTOINCREMENT))"""
        self.exe_query(self.query)
    
    def create_table_status_pekerjaan(self):
        self.query = """CREATE TABLE "status_pekerjaan"(
            "id" INTEGER NOT NULL UNIQUE,
            "diterima" BOOLEAN NOT NULL,
            "dicuci" BOOLEAN NOT NULL,
            "selesai" BOOLEAN NOT NULL,
            "diambil" BOOLEAN NOT NULL,
            PRIMARY KEY ("id" AUTOINCREMENT))"""
        self.exe_query(self.query)

create_table = table()