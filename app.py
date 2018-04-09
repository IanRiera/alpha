# Author: Ian Riera Smolinska
import os, sys, xlrd
from flask import Flask, request
from utils import wit_response
from chat import *
from pymessenger import Bot

app = Flask(__name__)
categories = {'intent':None,'salutacio':None,'servei_codi':None, 'servei_nom':None,'treballador_nom':None,'treballador_cognomos':None,'treballador_rol':None}

class brain():

    def get_response(self,message):
        response = None
        categories['intent'] = None
        
        resp = wit_response(message)
        entities = list(resp['entities'])

        for entity in entities:
        	categories[entity] =  resp['entities'][entity][0]['value']
        	
        if categories['intent'] == 'get_servei_worker':
        	response = "Ok, buscaré al "+categories['treballador_rol']+" de "+categories['servei_nom']

        elif categories['intent'] == 'get_servei_nom':
        	response = self.get_servei(str(categories['servei_codi']))#"Ok, buscaré el servei {} ".format(str(value));

        elif categories['intent'] == 'get_servei_tipus':
        	response = self.get_servei(str(value))#"Ok, buscaré el servei {} ".format(str(value));

        elif categories['intent'] == 'get_treballador_rol':
        	response = self.get_servei(str(value))#"Ok, buscaré el servei {} ".format(str(value));

        elif categories['intent'] == 'get_treballador_correu':
        	response = self.get_servei(str(value))#"Ok, buscaré el servei {} ".format(str(value));

        elif categories['intent'] == 'get_treballador_telefon':
        	response = self.get_servei(str(value))#"Ok, buscaré el servei {} ".format(str(value));

        elif categories['intent'] == 'get_treballador_contacte':
        	response = self.get_servei(str(value))#"Ok, buscaré el servei {} ".format(str(value));

        else:
        	response = "No ho he entés";
            
        return response

    def get_servei(self,codi):
    	nom_servei = None

    	book = xlrd.open_workbook("bbdd_pilot.xls")
    	sh = book.sheet_by_name("Cataleg_de_serveis")

    	row_number = 0
    	row_num = 0

    	for row_num in range(sh.nrows):
    		if sh.cell_value(rowx=row_num, colx=0) == codi:
    			row_number = row_num

    	nom_servei = "Es correspón a "+sh.cell_value(rowx=row_number, colx=1)+". El seu referent és en "+sh.cell_value(rowx=row_number, colx=3)+", amb correu: "+sh.cell_value(rowx=row_number, colx=4)
    	return nom_servei
    	

    def get_worker(self, rol_treballador, nom_servei):
    	worker = None

    	book = xlrd.open_workbook("bbdd_pilot.xls")
    	sh = book.sheet_by_name("Cataleg_de_serveis")

    	row_number = 0
    	row_num = 0

    	for row_num in range(sh.nrows):
    		if sh.cell_value(rowx=row_num, colx=1) == nom_servei:
    			row_number = row_num

    	nom_servei = "Es correspón a "+sh.cell_value(rowx=row_number, colx=1)+". El seu referent és en "+sh.cell_value(rowx=row_number, colx=3)+", amb correu: "+sh.cell_value(rowx=row_number, colx=4)
    	return nom_servei


    	






    

        
