# -*- coding: utf-8 -*-

from openerp import models, fields, api

class gato_veterinaria(models.Model):
    _name = 'gato.gato'
    _description = 'Gato de veterinaria'
    name = fields.Char('Nombre', required=True)
    descripcion = fields.Char('Descripcion')
    edad = fields.Integer('Edad')
    nacimiento = fields.Date('Fecha de nacimiento')
    foto = fields.Binary('Foto')
    
class perro_veterinaria(models.Model):
    _name = 'perro.perro'
    _description = 'Perro de veterinaria'
    name = fields.Char('Nombre', required=True)
    descripcion = fields.Char('Descripcion')
    edad = fields.Integer('Edad')
    nacimiento = fields.Date('Fecha de nacimiento')
    foto = fields.Binary('Foto')
