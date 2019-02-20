# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PluginSale(models.Model):

	"""This class extends Sale class and provides some features
	"""
	
	_inherit = 'sale.order'

	m_type = fields.Selection([('fx', 'Forfait'), ('at', 'Assistante technique')], string = "Type d'offre", required=True)
	m_payment_method = fields.Text(string = "Modalité de facturation")

	@api.one
	def generate_payment_method(self):
		text = ""
		if self.m_type == "fx":
			text = "<strong>Modalité de paiement :</strong><br>\n30% à la commande<br>\n50% à la livraison des devs<br>\n20% à la mise en production"
		else:
			text = "<strong>Modalité de paiement :</strong><br>\nFin de mois, payable à 30 jours"

		self.write({'m_payment_method': text})