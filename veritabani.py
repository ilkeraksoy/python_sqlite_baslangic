import sqlite3
 
#Veri tabanı dosyası ve tablo oluşturuldu
conn = sqlite3.connect('Futbol.db')
c = conn.cursor()
c.execute('''CREATE TABLE Futbolcu
             (isim text, soyisim text, kulup text, yas integer)''')
 
 
#Tabloya veriler eklendi
c.execute("INSERT INTO Futbolcu VALUES ('Lionel','MESSI','Barcelona',29)")
c.execute("INSERT INTO Futbolcu VALUES ('Arjen','ROBBEN','Bayern',32)")
conn.commit()
conn.close()
 
 
#Tekrar bağlanıldı, kursör oluşturuldu veriler ekrana yazıldı ve bağlantı sonlandırıldı
conn = sqlite3.connect('Futbol.db')   
c = conn.cursor()                      
c.execute('SELECT * FROM Futbolcu')    
veriler = c.fetchall()
for veri in veriler:
    print(veri)
conn.close()                 