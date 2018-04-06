# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 12:42:07 2018
@author: R325100
"""
import os, sys, xlrd
from flask import Flask, request
from utils import wit_response
from chat import *
from pymessenger import Bot

app = Flask(__name__)

class brain():
    def get_response(self,message):
        response = None

        entity, value = wit_response(message)

        
        if entity == 'treballador_rol':
        	response = "Ok, buscaré al {} ".format(str(value));
        elif entity == 'servei_codi':
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

    	nom_servei = "Es correspón a"+sh.cell_value(rowx=row_number, colx=1)+". El seu referent és en "+sh.cell_value(rowx=row_number, colx=3)+", amb correu: "+sh.cell_value(rowx=row_number, colx=4)
    	return nom_servei
    	


    	






    

        
