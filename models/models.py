# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Film(models.Model):
    _name = 'opencinema.film'
    _description = "OpenCinema Films"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
