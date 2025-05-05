from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService

import io_utils
import text_generator

import time

import csv

mensagens = {}
contatos = []

def read_contacts(filename):
    csvlist = []

    with open('./_res/'+filename, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                csvlist.append([row[0], row[1]])
    return csvlist

def read_types(filename):
    csvlist = {}

    with open('./_res/'+filename, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                #csvlist.append([row[0], ])
                csvlist[row[1]] = row[0]
                line_count += 1

    return csvlist

mensagens = read_types('lista_tipos.csv')
contatos = read_contacts('lista2.csv')

browser = webdriver.Chrome()
browser.get('https://web.whatsapp.com/')


is_sending = True

def buscar_contato(contato):
    campo_pesquisa = browser.find_element(By.XPATH, '//p[@class="selectable-text copyable-text iq0m558w"]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = browser.find_elements(By.XPATH, '//p[@class="selectable-text copyable-text iq0m558w"]')

    if len(campo_mensagem) >= 2:
        #time.sleep(3)
        print(campo_mensagem)
        campo_mensagem[1].click()
        # campo_mensagem[1].send_keys(mensagem)
        campo_mensagem[1].send_keys(Keys.ENTER)
        #print('SEND',contato)

time.sleep(30)

while(True):
    if is_sending:
        for contato in contatos:
            mensagem = mensagens[contato[1]]

            browser.get('https://web.whatsapp.com/send/?phone='+contato[0]+'&text='+mensagem+'&type=phone_number&app_absent=1')

            time.sleep(7)
            enviar_mensagem(mensagem)
            time.sleep(1)
        exit()