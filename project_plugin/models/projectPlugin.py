from odoo import models, fields, api

class ProjectPlugin(models.Model):

	"""This class extends Project class and provides implements the projects statuses
	
	Attributes:
	    m_description (str): A manual description about the project
	    m_typologie (selection): Describe the type of business
	    m_status (selection): Task status
	"""
	
	_inherit = 'project.project'
	m_description = fields.Text(string="Description du projet")
	m_typology = fields.Selection(	[('4', 'Services Développement'), ('1', 'Services Intégration ServiceNow'), ('191', 'Services Intégration Odoo'), ('0', 'Autres')], string="Business Unit Service")

	#stage
	m_status = fields.Selection([
		("waiting","En attente"), 
		("inProgress","En cours"), 
		("done","Terminé"), 
		("cancelled","Annulé")], 
		string="Etat d'avancement", 
		default="waiting", 
		group_expand="_read_group_stage_ids", 
		store=True, 
		track_visibility='onchange')


	@api.model
	def _read_group_stage_ids(self, stages, domain, order):
		"""This function allows the kanban view to get all the known file status (even if the status doesn't contain any task)
		"""
		return (["waiting", "inProgress", "done", "cancelled"])
