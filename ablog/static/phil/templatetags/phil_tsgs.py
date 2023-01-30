from django import template
from phil.models import *

@register.inclusion_tag('phil/soft_skills.html')   # this tag create part of HTML-page