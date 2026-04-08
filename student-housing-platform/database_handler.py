listings = [
    {"id": 1, "title": "VIT Boys Hostel", "location": "Bhopal", "lat": 23.2599, "lng": 77.4126, "price": 6500, "trust": 85, "image": "hostel1.jpg", "phone": "1234567890", "description": "Comfortable hostel near VIT"},
    {"id": 2, "title": "Green Valley PG", "location": "Sehore", "lat": 23.2, "lng": 77.08, "price": 5500, "trust": 78, "image": "pg1.jpg", "phone": "0987654321", "description": "Peaceful PG with amenities"}
]

reviews = []
reports = []

def get_listings():
    return listings

def get_listing_by_id(id):
    return next((l for l in listings if l['id'] == id), None)

def add_review(data):
    reviews.append({"rating": data.get("rating"), "comment": data.get("comment")})

def add_listing(data):
    new_id = max([l['id'] for l in listings]) + 1 if listings else 1
    listing = {
        "id": new_id,
        "title": data.get("title"),
        "location": data.get("location"),
        "price": int(data.get("price", 0)),
        "trust": int(data.get("trust", 0)),
        "lat": float(data.get("lat", 0)),
        "lng": float(data.get("lng", 0)),
        "image": data.get("image"),
        "phone": data.get("phone"),
        "description": data.get("description")
    }
    listings.append(listing)
    return new_id

def report_listing(data):
    reports.append({"reason": data.get("reason")})