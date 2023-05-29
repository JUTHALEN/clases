#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import models, fields, api
from datetime import datetime
import re
from odoo.exceptions import ValidationError

class modulo_clase(models.Model):
    _name = 'modulo.modulo'
    _description = 'clases'

    name = fields.Char(string="Nombre", required=True)
    fecha = fields.Date(string="Fecha", required=True)
    hora_inicio = fields.Float(string="Hora de inicio", widget="time")
    hora_fin = fields.Float(string="Hora de fin", widget="time")
    clases = fields.Selection(
        [('1',"Sistema de Gestión empresarial"),
        ('2',"Lenguaje de Marcas"),
        ('3',"Entornos de Desarrollo"),
        ('4',"Programación"),
        ('5',"Bases de Datos"),
        ('6',"Formación y Orientación Laboral")],
        string="Clases"
    )

    @api.constrains('hora_inicio', 'hora_fin')
    def _check_hora(self):
        for record in self:
            hora_inicio = record.hora_inicio.strip()
            hora_fin = record.hora_fin.strip()
            # verificar que el formato sea HH:MM
            if not re.match(r'^\d{1,2}:\d{2}$', hora_inicio) or not re.match(r'^\d{1,2}:\d{2}$', hora_fin):
                raise ValidationError("La hora debe estar en formato HH:MM")
            # verificar que las horas y minutos sean válidos
            hi, mi = map(int, hora_inicio.split(':'))
            hf, mf = map(int, hora_fin.split(':'))
            if hi < 0 or hi > 23 or mi < 0 or mi > 59 or hf < 0 or hf > 23 or mf < 0 or mf > 59:
                raise ValidationError("La hora debe ser válida")
            # verificar que la hora de inicio sea menor que la hora de fin
            if record.hora_inicio > record.hora_fin:
                raise ValidationError("La hora de inicio debe ser menor que la hora de fin")


class modulo_profesor(models.Model):
    _name = "modulo.profesor"
    _description = "Profesor"

    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    