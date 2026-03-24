from pydantic import BaseModel

class CustomerData(BaseModel):
    age: int
    gender: str
    income_bracket: str
    loyalty_program: str
    membership_years: int
    marital_status: str
    number_of_children: int
    education_level: str
    occupation: str
    product_category: str
    quantity: int
    unit_price: float
    avg_purchase_value: float
    purchase_frequency: str
    avg_discount_used: float
    online_purchases: int
    in_store_purchases: int
    total_sales: float
    total_transactions: int
    total_items_purchased: int
    promotion_type: str
    promotion_effectiveness: str
    days_since_last_purchase: int