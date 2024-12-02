from fastapi import APIRouter

router = APIRouter()

@router.get("")
def get_products():
    return [{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Phone"}]

@router.post("")
def create_product(product: dict):
    return {"message": f"Product {product['name']} created!"}