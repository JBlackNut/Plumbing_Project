from django import template
register = template.Library()

@register.filter(is_safe=True)
def mod(value):
	"""
	"""
	if value % 2:	return True
	else:	return False
