from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import random

class Selenium:
	def __init__(self, url):
		self._url=url
		self._drive=None
			
	def conexion(self):
		self._drive = webdriver.Chrome()
		self._drive.get((self._url))

	def ejecutarScript(self,script):
		self._drive.execute_script(script)
		

	def obtenerId(self,idt,mensaje,tipo):
		part=self._drive.find_element_by_id(idt)
		if tipo==1:
			part.send_keys(mensaje)
		else:
			part.click()

	def obtenerName(self,nombre,mensaje,tipo):
		part=self._drive.find_element_by_name(nombre)
		if tipo==1:
			part.send_keys(mensaje)
		else:
			part.click()

	def enviarKey(self,texto):
		self._drive.send_keys(texto)
	def esperar(self,tiempo):
		time.sleep(tiempo)
		
		
def main():
 seccion=random.randint(100, 999) 
 i=Selenium('https://soft2.herokuapp.com/')
 i.conexion()
 i.ejecutarScript("ingresar();")
 i.obtenerName("codigou","1111",1)
 i.obtenerName("clave","admin",1)
 i.obtenerId("a1","fake",2)
 i.obtenerName("crearsession",seccion,1)
 i.obtenerName("bseccion","fake",2)
 i.esperar(1)
 i.obtenerName("selectedsecc","fake",2)
 i.esperar(2)
 i.obtenerName("salir","fake",2)
 i.esperar(3)
 i.ejecutarScript("ingresar();")
 i.obtenerName("codigou","2555555",1)
 i.obtenerName("clave","gg",1)
 i.obtenerId("a1","fake",2)
 i.obtenerId("1","fake",2)
 i.esperar(1)
 i.obtenerName("curso","fake",2)
 i.esperar(1)
 i.obtenerName("prof","fake",2)
 i.esperar(1)
 i.obtenerName("aseso","fake",2)
 i.esperar(1)
 i.obtenerName("aseso","fake",2)
 i.esperar(3)
 i.obtenerName("aseso","fake",2)
 i.esperar(3)
 i.obtenerName("cance","fake",2)
 i.esperar(4)
 i.obtenerName("salir","fake",2)
 i.esperar(3)
 i.ejecutarScript("ingresar();")
 i.obtenerName("codigou","20132670",1)
 i.obtenerName("clave","gg",1)
 i.obtenerId("a1","fake",2)
 i.esperar(1)
 i.obtenerName("a1","fake",2)
 i.esperar(1)
 i.obtenerId("botonera","fake",2)
 i.esperar(1)
 i.obtenerId("botonera","fake",2)
 i.esperar(1)
 i.obtenerName("pisocu","w-23",1)
 i.esperar(2)
 i.obtenerName("crearase","fake",2)
 i.esperar(2)
 i.obtenerName("a2","fake",2)
 i.esperar(1)
 i.obtenerName("a1","fake",2)
 i.esperar(1)
 i.obtenerName("button","fake",2)
 i.esperar(4)








 


	
	
	
	
if __name__ == "__main__":
    main()
    