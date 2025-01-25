
customer = {
"id": 101,
"name": "Alice Johnson",
"phone": "123-321",
"premium_member": True
}

print(customer["id"])



customers = [
    {
        "id": 101,
        "name": "Alice Johnson",
        "phone": "123-321",
        "premium_member": True
    },
    {
        "id": 102,
        "name": "Balice Bohnson",
        "phone": "555-444",
        "premium_member": False
    }
]

for customer in customers:
    print(customer["name"])
    print("___________________")
