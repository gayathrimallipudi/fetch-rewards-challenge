from fastapi import FastAPI  #for web API
from pydantic import BaseModel #used for req validation
import uuid #to generate unique ids
import math

app = FastAPI()

receipts_db = {}

#Item data types
class Item(BaseModel):
    shortDescription: str
    price: str

class Receipt(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    total: str
    items: list[Item]

@app.post("/receipts/process")
def process_receipt(receipt: Receipt):
    receipt_id = str(uuid.uuid4())  #generate a unique id
    points = calculate_points(receipt)  #calculate points
    receipts_db[receipt_id] = points  # store points
    return {"id": receipt_id}

@app.get("/receipts/{receipt_id}/points") #takes receipt id
def get_points(receipt_id: str):
    if receipt_id in receipts_db:
        return {"points": receipts_db[receipt_id]}
    return {"error": "Receipt not found"}, 404

def calculate_points(receipt: Receipt):
    points = 0
    points += sum(c.isalnum() for c in receipt.retailer) #rule-1:alphanumeric characters
    
    total=float(receipt.total)
    if total.is_integer(): #rule-2:round dollar amount with no cents
        points += 50

    if total % 0.25 == 0: #rule-3:if total is multiple of 0.25
        points += 25

    points += (len(receipt.items) //2) * 5 #rule-4:item count

    for item in receipt.items: #rule-5:trimmed desc multiple of 3
        description = item.shortDescription.strip()
        if len(description) % 3 == 0:
            points += math.ceil(float(item.price) * 0.2)

    purchase_day=int(receipt.purchaseDate.split("-")[2]) #rule-6:extract date and if date is odd
    if purchase_day%2==1:
        points+=6

    hour, minute = map(int, receipt.purchaseTime.split(":")) #rule-7:timeof purchase
    if 14 <= hour < 16:
        points += 10

    return points
