from server import PromptServer
from .template import getKeys
from aiohttp import web

@PromptServer.instance.routes.get("/templates")
async def get_keys(request):
    filename = request.query.get("name")
    return web.json_response({ "keys": getKeys(filename) })