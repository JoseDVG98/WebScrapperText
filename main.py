from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import requests
from bs4 import BeautifulSoup
import re
import paginas
import manejo_paginas
from selenium import webdriver


if __name__ == '__main__':
    url='https://www.bancodebogota.com'
    scraping= paginas.Pagina()
    dicLinks= scraping.buscarLinks(url,"software",url)
    busqueda=manejo_paginas.AbrirPaginas().buscarPalabraHTML(dicLinks,'software','https://www.delftstack.com')



















