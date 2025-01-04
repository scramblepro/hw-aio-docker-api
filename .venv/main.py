from aiohttp import web
import json
from datetime import datetime

# Хранилище для объявлений
ads = {}
ad_id_counter = 1

async def create_ad(request):
    global ad_id_counter
    data = await request.json()

    # Проверка обязательных полей
    required_fields = ["title", "description", "owner"]
    if not all(field in data for field in required_fields):
        return web.json_response({"error": "Missing required fields"}, status=400)

    ad = {
        "id": ad_id_counter,
        "title": data["title"],
        "description": data["description"],
        "created_at": datetime.now().isoformat(),
        "owner": data["owner"]
    }
    ads[ad_id_counter] = ad
    ad_id_counter += 1
    return web.json_response(ad, status=201)

async def get_ad(request):
    ad_id = int(request.match_info["ad_id"])
    ad = ads.get(ad_id)
    if not ad:
        return web.json_response({"error": "Ad not found"}, status=404)
    return web.json_response(ad)

async def delete_ad(request):
    ad_id = int(request.match_info["ad_id"])
    if ad_id not in ads:
        return web.json_response({"error": "Ad not found"}, status=404)
    del ads[ad_id]
    return web.json_response({"message": "Ad deleted"}, status=200)

app = web.Application()
app.add_routes([
    web.post("/ads", create_ad),
    web.get("/ads/{ad_id}", get_ad),
    web.delete("/ads/{ad_id}", delete_ad)
])

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8080)
