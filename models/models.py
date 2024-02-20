# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LisaPacientes(models.Model):
    _name = 'hospital_module.lista_pacientes'
    _description = 'Modulo que gestiona los pacientes del hospital'
    _rec_name='nombrePaciente'

    nombrePaciente = fields.Char(
        string="Nombre del paciente: "
    )
    sintomas = fields.Text(
        string="Sintomas: "
    )
    diagnostico = fields.One2many(
        string="Diagnostico: ",
        comodel_name='hospital_module.lista_diagnosticos',
        inverse_name='paciente',
    )
    
class ListaMedicos(models.Model):
    _name = 'hospital_module.lista_medicos'
    _description = 'Vista que gestiona los medicos del hospital'   
    _rec_name='identidadMedico'
    
    identidadMedico = fields.Char(
        string="Nombre y apellidos del medico: "
    )
    numeroMedico = fields.Integer(
        string="ID"
    )
    diagnosticos = fields.One2many(
        string='Diagnosticos: ',
        comodel_name='hospital_module.lista_diagnosticos',
        inverse_name='medico'
    )
    
class ListaDiagnosticos(models.Model):
    _name = 'hospital_module.lista_diagnosticos'    
    _description = 'Vista que gestiona los diagnosticos'
    
    paciente = fields.Many2one(
        string='Paciente: ',
        comodel_name='hospital_module.lista_pacientes',
        ondelete='cascade',
    )
    medico = fields.Many2one(
        string="Medico: ",
        comodel_name='hospital_module.lista_medicos',
        
        ondelete='cascade',
        
    )
    diagnostico = fields.Text(
        string="Descripcion del diagnostico"
    )