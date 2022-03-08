# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Film(models.Model):
    _name = 'opencinema.film'
    _description = "OpenCinema Films"

    name = fields.Char(string="Title", required=True)
<<<<<<< HEAD
    description = fields.Text(string="Description")
    duration = fields.Integer(sting="Duration")
    release_date = fields.Char(string="Release date")
    
    
    
    
    class Director(models.Model):
        _name = 'opencinema.director'
        _description = "OpenCinema Directors"
        
        name = fields.Char(string="Name", required=True)
        nationality = fields.Char(string="Nationality")
=======
    description = fields.Text()
    release_date = fields.Date(string='Release date')
    duration = fields.Integer(string="Duration")
>>>>>>> d21a20e319ed231767b7d7b3ac324d30b9e4e8ba
