from graphviz import Digraph

erd = Digraph('ERD_Online_Store', filename='online_store_erd', format='png')
erd.attr(rankdir='LR', size='8')

entities = {
    "Customers": [
        "+customer_id (PK)",
        "first_name",
        "last_name",
        "email (unique)",
        "password",
        "created_at"
    ],
    "Products": [
        "+product_id (PK)",
        "name",
        "description",
        "price",
        "stock_quantity"
    ],
    "Orders": [
        "+order_id (PK)",
        "customer_id (FK)",
        "order_date",
        "total_amount"
    ],
    "Order_Items": [
        "+order_id (PK, FK)",
        "+product_id (PK, FK)",
        "quantity",
        "price_each"
    ],
    "Payments": [
        "+payment_id (PK)",
        "order_id (FK)",
        "payment_date",
        "amount",
        "payment_method"
    ]
}

for entity, attributes in entities.items():
    label = f"<<TABLE BORDER='1' CELLBORDER='0' CELLSPACING='0'>"
    label += f"<TR><TD BGCOLOR='lightblue'><B>{entity}</B></TD></TR>"
    for attr in attributes:
        label += f"<TR><TD ALIGN='LEFT'>{attr}</TD></TR>"
    label += "</TABLE>>"
    erd.node(entity, shape='plaintext', label=label)

erd.edge("Customers", "Orders", label="1:N")
erd.edge("Orders", "Order_Items", label="1:N")
erd.edge("Products", "Order_Items", label="1:N")
erd.edge("Orders", "Payments", label="1:1")

erd.render(cleanup=True)
