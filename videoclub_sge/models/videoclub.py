from odoo import models, fields

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
