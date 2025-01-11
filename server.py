from server import PromptServer
from .template import getKeys
from aiohttp import web

@PromptServer.instance.routes.get("/templates/{file}")
async def get_keys(request):
    filename = request.match_info["file"]
    return web.json_response({ "keys": getKeys(filename) })