from django.contrib import admin
from django.utils.html import format_html
from .models import Produit


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
	list_display = ("nom", "prix", "disponible", "image_tag")
	list_editable = ("prix", "disponible")
	search_fields = ("nom", "description")
	list_filter = ("disponible",)
	readonly_fields = ("image_tag",)
	ordering = ("nom",)

	fieldsets = (
		(None, {
			"fields": ("nom", "description", "prix", "disponible")
		}),
		("Image", {
			"fields": ("image", "image_tag")
		}),
	)

	def image_tag(self, obj):
		if obj.image:
			return format_html('<img src="{}" style="max-height: 100px;"/>', obj.image.url)
		return ""

	image_tag.short_description = "Aperçu"
