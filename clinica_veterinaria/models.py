# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class default_data_demo(models.Model):
#    _name = 'demo.default.data'
#    _description = 'Demo default data'
#    name = fields.Char('Name', required=True)
#    description = fields.Html('Description')
class gato_veterinaria(models.Model):
    _name = 'gato.veterinaria'
    _description = 'Datos de un gato'
    nombre = fields.Char('Nombre', required=True)
    raza = fields.Char('Raza')
    propietario = fields.Char('Propietario')
	vacunado = fields.Boolean('Vacunado?')
	fecha_ingreso = fields.Date('Fecha ingreso')
	coste_tratamiento = fields.Double('Coste tratamiento')
