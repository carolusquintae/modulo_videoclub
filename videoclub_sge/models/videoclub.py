# -*- coding: utf-8 -*-
from odoo import models, fields, api

class videoclub_pelis(models.Model):
    _name = 'videoclub.pelis'
    _description = 'Película'

    titulo = fields.Char('Título', size=30, required=True, 
                         help='Nombre de la película')
    director = fields.Char('Director', size=30, required=False, 
                          help='Director de la película', default='')
    clasificacion = fields.Selection([
        ('TP', 'Todos los Públicos'),
        ('men12', 'Menores de 12 años'),
        ('may18', 'Mayores 18 años')
    ], string='Clasificación', default='TP')
    presupuesto = fields.Integer('Presupuesto')
    fechaestreno = fields.Date('Fecha de estreno')
    categoria_id = fields.Many2one('videoclub.categoria', string='Categoría')
    compania_id = fields.Many2one('res.partner', string='Compañía',
                                   domain=[('is_cine', '=', True)])
    imagen = fields.Binary('Imagen', attachment=True)
    
    # Campo calculado
    millonario = fields.Boolean('¿Millonaria?', 
                                compute='_compute_millonario',
                                store=True)

    @api.depends('presupuesto')
    def _compute_millonario(self):
        for record in self:
            record.millonario = record.presupuesto > 1000000

class videoclub_categoria(models.Model):
    _name = 'videoclub.categoria'
    _description = 'Categoría de Película'

    name = fields.Char('Nombre', required=True)
    descripcion = fields.Text('Descripción')
    pelicula_ids = fields.One2many('videoclub.pelis', 'categoria_id', string='Películas')

class compania_cinematografica(models.Model):
    _inherit = 'res.partner'
    
    premiada = fields.Boolean('Compañía premiada', default=False)
    is_cine = fields.Boolean('Es compañía de cine', default=False)
