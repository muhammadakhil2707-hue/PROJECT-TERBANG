print("===   TYRE PRODUCTION SYSTEM   ===")
type_tyre =input(    "Tyre Type(S/P)  :").upper()
quantity = int(input("Quantity        :"))
inspection = input(  "Inspection(E/B) :").upper()
if type_tyre == "S":
    tyre_name = "Standard"
    price = 180
    if quantity >= 80:
        discount = 0.15
    elif quantity >= 40:
        discount = 0.07
    else:
        discount = 0    
elif type_tyre == "P":
    tyre_name = "Premium"
    price = 320
    if quantity >= 60:
        discount = 0.18
    elif quantity >= 25:
        discount = 0.10
    else:
        discount = 0
else:
    print("Invalid tyre type.")  

original_cost = price * quantity
discount_amount = original_cost * discount
cost_after_discount = original_cost - discount_amount
if inspection == "E":
    inspection_name = "Enhanced Inspection"
    inspection_charge = cost_after_discount * 0.06
elif inspection == "B":
    inspection_name = "Basic Inspection"
    inspection_charge = 0
adjusted_cost = cost_after_discount + inspection_charge
if adjusted_cost >= 10000:
    packaging_fee = 0
else:
    packaging_fee = 150
final_cost = adjusted_cost + packaging_fee
print("-"*35)
print("Tyre Type            : ",tyre_name)
print(f"Original Cost        : RM{original_cost:.2f}")
print(f"Discount             : RM{discount_amount:.2f}")
print(f"Inspection Charge    : RM{inspection_charge:.2f}")
print(f"Delivery             : RM{packaging_fee:.2f}")
print(f"Final Payment        : RM{final_cost:.2f}")