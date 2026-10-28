import datetime

class WarrantyItem:

    def __init__(self, item_name,purchase_date_str,warranty_days):
        self.item_name = item_name
        self.purchase_date_str=datetime.datetime.strptime(purchase_date_str, "%Y-%m-%d")
        self.expiration_date= datetime.timedelta(days=warranty_days)+ self.purchase_date_str


    def days_remaining(self, current_date=None):
        current_date= self.current_date.datetime.datetime.now()
        diff= self.expiration_date-self.current_date
        return diff.days


item = WarrantyItem("Laptop", "2026-01-01", 365)
print("Days remaining:", item.days_remaining())