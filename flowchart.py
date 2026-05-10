total_purchase_amount = int(input("Enter total purchase amount: "))
if total_purchase_amount >= 5000:
    membership_status = input("Enter membership status (Yes, No): ")
    membership_status.lower()
    if membership_status == "yes":
        discount = total_purchase_amount * 0.30
        final_price = total_purchase_amount - discount 
        print(f'Total Saved: {int(discount)}')
        print(f'Final Price: {int(final_price)}')
    else:
        print(f'Total: {int(total_purchase_amount)}')
else:
    print(f'Total: {int(total_purchase_amount)}')
