# -*- coding: utf-8 -*-

from odoo import models, fields, api

 class Course(models.Model):
     _name = 'openacademy.course'
     _description='Open Academy Courses'

     name = fields.char(string="Title", required=true)
     description = fields.Text()