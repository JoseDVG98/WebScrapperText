from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import re

class Pagina ():

    def __init__(self):
        self.diccionario_links={}

    def getLink(self):
        return self.link

    def setLink(self,l):
        self.link=l
        return True

    def buscarLinks(self, url, caracter, path_absoluto=''):
        pagina = requests.get(path_absoluto)
        html = BeautifulSoup(pagina.text, 'html.parser')
        palabra= self.buscarPalabra(caracter,html)
        links = html.find_all('a')
        #print('------------------------------------------------------------------------------------------------------------------------------------------------------')
        #print(links)
        #print('------------------------------------------------------------------------------------------------------------------------------------------------------')
        for link in links:
            #print(link.get('href'))

            if link.get('href') is None:
                continue
            #print("---------------------->link: "+link.get('href')+"¿hay espacio?"+url)
            cadena = self.manejoCadena(url,link)
            if cadena is not None:
                slug=cadena[0]
                if slug.endswith("/"):
                    slug=slug[0:-1]
                if slug.startswith("/", 0):
                    path_absoluto = url + slug
                    #print("path------>", path_absoluto)
                else:
                    path_absoluto = slug


                try:
                    self.diccionario_links[path_absoluto]

                except:
                    #print(path_absoluto)
                    self.diccionario_links[path_absoluto]=palabra
                    #print(self.diccionario_links)
                    self.buscarLinks(url,caracter,path_absoluto)



        return self.diccionario_links

    def manejoCadena (self, url, link):
        cadena_depurada=re.sub("\+","\+",link.get('href'))
        cadena_depurada = re.sub("\?", "\?", link.get('href'))
        cadena_depurada = re.sub("\|", "\|", link.get('href'))
        #print("cadena depurada:   ", cadena_depurada)
        cadena=re.fullmatch(url + ".+", cadena_depurada)
        if cadena is None:
            cadena = re.fullmatch("/.+", cadena_depurada)
        return cadena

    def buscarPalabra(self,caracter,html):
        texto=html.get_text()
        resultado=re.search(caracter,texto)

        if resultado is not None:
            return True
        else:
            return False













