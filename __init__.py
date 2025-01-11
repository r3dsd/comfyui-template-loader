from .nodes import TemplateLoader
from . import server

NODE_CLASS_MAPPINGS = {
    "TemplateLoader": TemplateLoader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TemplateLoader": "Template Loader"
}

WEB_DIRECTORY = "./js"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']