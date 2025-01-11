from .template import get_all_source, getData, getKeys

class ContainsAnyDict(dict):
    def __contains__(self, key):
        return True

class TemplateLoader:
    CATEGORY = 'TemplateLoader'
    RETURN_TYPES = ("STRING",)
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls):
        sources = get_all_source()
        all_keys = [key for source in sources for key in getKeys(source)]
        return {
            "required": {
                "source": (sources, { "default": sources[0] if sources else "" }),
                "template": (all_keys, {}),
            }
        }
    
    def run(self, source, template):
        return (getData(source, template),)