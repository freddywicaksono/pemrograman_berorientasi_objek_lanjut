from db import DBConnection as mydb

class Dosen:
   def __init__(self):
       self.__id = None
       self.__nidn = None
       self.__nama_lengkap = None
       self.__jk = None
       self.__telpon = None
       self.__email = None
       self.__prodi = None
       self.__info = None
       self.conn = None
       self.affected = None
       self.result = None

   @property
   def nidn(self):
       return self.__nidn

   @nidn.setter
   def nidn(self, value):
       self.__nidn = value


   @property
   def nama_lengkap(self):
       return self.__nama_lengkap

   @nama_lengkap.setter
   def nama_lengkap(self, value):
       self.__nama_lengkap = value


   @property
   def jk(self):
       return self.__jk

   @jk.setter
   def jk(self, value):
       self.__jk = value


   @property
   def telpon(self):
       return self.__telpon

   @telpon.setter
   def telpon(self, value):
       self.__telpon = value


   @property
   def email(self):
       return self.__email

   @email.setter
   def email(self, value):
       self.__email = value


   @property
   def prodi(self):
       return self.__prodi

   @prodi.setter
   def prodi(self, value):
       self.__prodi = value


   def simpan(self):
       self.conn = mydb()
       val = (self.__nidn,self.__nama_lengkap,self.__jk,self.__telpon,self.__email,self.__prodi)
       sql = "INSERT INTO dosen(nidn,nama_lengkap,jk,telpon,email,prodi) values " + str(val)
       self.affected = self.conn.insert(sql)
       self.conn.disconnect
       return self.affected

   def update(self, id):
       self.conn = mydb()
       val = (self.__nidn,self.__nama_lengkap,self.__jk,self.__telpon,self.__email,self.__prodi, id)
       sql = "UPDATE dosen SET nidn = %s, nama_lengkap = %s, jk = %s, telpon = %s, email = %s, prodi = %s WHERE iddosen = %s"
       self.affected = self.conn.update(sql)
       self.conn.disconnect
       return self.affected

   def updateByNIDN(self, nidn):
       self.conn = mydb()
       val = (self.__nidn,self.__nama_lengkap,self.__jk,self.__telpon,self.__email,self.__prodi, nidn)
       sql = "UPDATE dosen SET nidn = %s, nama_lengkap = %s, jk = %s, telpon = %s, email = %s, prodi = %s WHERE nidn = %s"
       self.affected = self.conn.update(sql, val)
       self.conn.disconnect
       return self.affected

   def getByID(self, id):
       self.conn = mydb()
       sql="SELECT * FROM dosen WHERE iddosen='" + str(id) + "'"
       self.result = self.conn.findOne(sql)
       if(self.result!=None):
           self.__nidn = self.result[1]
           self.__nama_lengkap = self.result[2]
           self.__jk = self.result[3]
           self.__telpon = self.result[4]
           self.__email = self.result[5]
           self.__prodi = self.result[6]
           self.affected = self.conn.cursor.rowcount
       else:
           self.__nidn = ''
           self.__nama_lengkap = ''
           self.__jk = ''
           self.__telpon = ''
           self.__email = ''
           self.__prodi = ''
           self.affected = 0
       self.conn.disconnect
       return self.result

   def getByNIDN(self, nidn):
       a=str(nidn)
       b=a.strip()
       self.conn = mydb()
       sql="SELECT * FROM dosen WHERE nidn='" + b + "'"
       self.result = self.conn.findOne(sql)
       if(self.result!=None):
           self.__nidn = self.result[1]
           self.__nama_lengkap = self.result[2]
           self.__jk = self.result[3]
           self.__telpon = self.result[4]
           self.__email = self.result[5]
           self.__prodi = self.result[6]
           self.affected = self.conn.cursor.rowcount
       else:
           self.__nidn = ''
           self.__nama_lengkap = ''
           self.__jk = ''
           self.__telpon = ''
           self.__email = ''
           self.__prodi = ''
           self.affected = 0
       self.conn.disconnect
       return self.result

   def delete(self, id):
       self.conn = mydb()
       sql="DELETE FROM dosen WHERE iddosen ='"+ str(id) + "'"
       self.affected = self.conn.delete(sql)
       self.conn.disconnect
       return self.affected

   def deleteByNIDN(self, nidn):
       self.conn = mydb()
       sql="DELETE FROM dosen WHERE nidn ='"+ str(nidn) + "'"
       self.affected = self.conn.delete(sql)
       self.conn.disconnect
       return self.affected

   def getAllData(self):
       self.conn = mydb()
       sql="SELECT * FROM dosen limit 100"
       self.result = self.conn.findAll(sql)
       return self.result

A = Dosen()
nidn = '6005'
A.nidn = nidn
A.nama_lengkap = 'Vega Kusuma'
A.email = 'vega@gmail.com'
A.jk = 'L'
A.prodi = 'IND'
A.telpon = '089456123456'
A.updateByNIDN(nidn)
B = A.getAllData()
print(B)