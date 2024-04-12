from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


class AbrirPaginas():

    palabraClave=''

    def buscarPalabraHTML(self, diccionarioPaginas, palabra, dominio):
        c=0
        self.palabraClave=palabra
        print("En las siguientes paginas del dominio: " + dominio + '  Existe la palabra --> ' + self.palabraClave)
        print("Escoger el numero para abrir la pagina y visualizar donde se encuentra la palabra:")
        for link, valor in diccionarioPaginas:
            if valor:
                print(c+1 + 'Link: ' + link)

        indice=input()
        service = Service(r"C:\Users\jose.velasquez\Desktop\Drivers\geckodriver.exe")
        driver = webdriver.Firefox(service=service)

        link=list(diccionarioPaginas.keys)[indice]

        driver.get(link)










