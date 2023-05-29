#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import models, fields, api
from datetime import datetime
import re
from odoo.exceptions import ValidationError

class modulo_clase(models.Model):
    _name = 'modulo.clase'
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
    #Relaciones con profesor
    profesor_id = fields.Many2one(
        comodel_name="modulo.profesor",
        string="Profesor",
        ondelete = "restrict"
    )
    #Relaciones con alumno
    alumno_ids = fields.Many2many(
        comodel_name="modulo.alumno",
        relation="clase_alumno_rel",
        column1="clase_id",
        column2="alumno_id",
        string="Alumnos",
        ondelete="cascade"
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
    email = fields.Char(string="Email")
    telefono = fields.Char(string="Teléfono")

    #Relaciones con clases
    clase_ids = fields.One2many(
        comodel_name="modulo.clase", 
        inverse_name="profesor_id",
        string="Clases",
        ondelete="set null")
    
    #Relaciones con alumno
    alumno_ids = fields.Many2many(
        comodel_name="modulo.alumno",
        relation="profesor_alumno_rel",
        column1="profesor_id",
        column2="alumno_id",
        string="Alumnos",
        ondelete="cascade"
    )
    
    #constrain
    @api.constrains('fecha_nacimiento')
    def _check_fecha_nacimiento(self):
        for record in self:
            if record.fecha_nacimiento > datetime.now().strftime("%Y-%m-%d"):
                raise ValidationError("La fecha de nacimiento debe ser anterior a la fecha actual")

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if not re.match(r'[^@]+@[^@]+\.[^@]+', record.email):
                raise ValidationError("El email debe ser válido")
    
    @api.constrains('telefono')
    def _check_telefono(self):
        for record in self:
            if not re.match(r'^\d{9}$', record.telefono):
                raise ValidationError("El teléfono debe ser válido")

class modulo_alumno(models.Model):
    _name = "modulo.alumno"
    _description = "Alumno"

    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    email = fields.Char(string="Email")
    dni = fields.Char(string="DNI")
    telefono = fields.Char(string="Teléfono")
    #Relaciones con clases
    clase_ids = fields.Many2many(
        comodel_name="modulo.clase",
        relation="clase_alumno_rel",
        column1="clase_id",
        column2="alumno_id",
        string="Clases",
        ondelete="restrict")
    #Relaciones con profesor
    profesor_ids = fields.Many2many(
        comodel_name="modulo.profesor",
        relation="profesor_alumno_rel",
        column1="alumno_id",
        column2="profesor_id",
        string="Profesores",
        ondelete = "restrict"
    )
    
    #constrain
    @api.constrains('fecha_nacimiento')
    def _check_fecha_nacimiento(self):
        for record in self:
            if record.fecha_nacimiento > datetime.now().strftime("%Y-%m-%d"):
                raise ValidationError("La fecha de nacimiento debe ser anterior a la fecha actual")
    
    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if not re.match(r'[^@]+@[^@]+\.[^@]+', record.email):
                raise ValidationError("El email debe ser válido")

    @api.constrains('dni')
    def _check_dni(self):
        for record in self:
            if not re.match(r'^\d{8}[a-zA-Z]$', record.dni):
                raise ValidationError("El DNI debe ser válido")
    
    @api.constrains('telefono')
    def _check_telefono(self):
        for record in self:
            if not re.match(r'^\d{9}$', record.telefono):
                raise ValidationError("El teléfono debe ser válido")
    
  

    