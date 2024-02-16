from openerp import models, fields, api, _


class GalleryProject(models.Model):
	_name = 'gallery.project'

	site_images = fields.One2many('ir.attachment','gallery_img')


	@api.multi
	def add_image(self):
		view_ref = self.env['ir.model.data'].get_object_reference('hiworth_project_management', 'viewgallery_ir_attachment_form_view')
		view_id = view_ref[1] if view_ref else False
		res = {
		   'type': 'ir.actions.act_window',
		   'name': _('Add Image'),
		   'res_model': 'ir.attachment',
		   'view_type': 'form',
		   'view_mode': 'form',
		   'view_id': view_id,
		   'target': 'new',
		   'context': {'default_gallery_img':self.id}
	   }
	 
		return res