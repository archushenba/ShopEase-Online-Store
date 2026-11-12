from products.models import Product

products = [
    {
        "name": "Wireless Earbuds",
        "description": "Compact wireless earbuds with clear audio.",
        "price": 999,
        "category": "Electronics",
        "stock": 25,
        "image": "https://gizmore.in/cdn/shop/files/0_15_02f25afa-a445-4923-8538-0b0785f587c7.jpg?v=1756883463&width=4001"
    },
    {
        "name": "Smart Watch",
        "description": "Modern smartwatch with useful smart features.",
        "price": 2499,
        "category": "Electronics",
        "stock": 15,
        "image": "https://www.fastrack.in/dw/image/v2/BKDD_PRD/on/demandware.static/-/Sites-titan-master-catalog/default/dw472776ec/images/Fastrack/Catalog/38184PP02K_1.jpg?sw=600&sh=600"
    },
    {
        "name": "Bluetooth Speaker",
        "description": "Portable Bluetooth speaker with powerful sound.",
        "price": 1299,
        "category": "Electronics",
        "stock": 20,
        "image": "https://m.media-amazon.com/images/I/7101mxxpNPL.jpg"
    },
    {
        "name": "Smartphone",
        "description": "Smartphone with modern features and design.",
        "price": 14999,
        "category": "Electronics",
        "stock": 10,
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJ-hEqrpWKkRE355WgdL0SjHX3aJ8MIznCtRvnR12QCg&s=10"
    },
    {
        "name": "Laptop",
        "description": "High performance laptop for work and study.",
        "price": 55999,
        "category": "Electronics",
        "stock": 8,
        "image": "https://media.wired.com/photos/6849bc049ce5751a283a2465/4:3/w_640%2Cc_limit/Yoga%25209i%2520(14-inch%2C%25202025)%2520Luke%2520Larsen.png"
    },
    {
        "name": "Running Shoes",
        "description": "Stylish and comfortable sports running shoes.",
        "price": 1499,
        "category": "Fashion",
        "stock": 20,
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNAK3sAeKAVMb31C5nknUin29pH7IFRGEPITHC-eI6Hw&s=10"
    },
    {
        "name": "Wireless Mouse",
        "description": "Smooth and responsive wireless mouse.",
        "price": 599,
        "category": "Electronics",
        "stock": 25,
        "image": "https://foxin.in/cdn/shop/files/Flow_2_1.png?v=1774699572"
    },
    {
        "name": "Power Bank",
        "description": "Portable power bank for charging devices.",
        "price": 899,
        "category": "Electronics",
        "stock": 20,
        "image": "https://sharpi.in/wp-content/uploads/2025/08/f15c67eb68984d8792a8bb5051946f4e-product-assets.jpg"
    },
    {
        "name": "USB Flash Drive",
        "description": "Compact USB flash drive for data storage.",
        "price": 399,
        "category": "Accessories",
        "stock": 30,
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRwOcc5TwFWyMS7clNABeKeiajoZRC7LQIwX5-iGDAsw&s=10"
    },
    {
        "name": "Laptop Backpack",
        "description": "Durable backpack with laptop storage space.",
        "price": 1199,
        "category": "Accessories",
        "stock": 15,
        "image": "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcQh0Cvi1StmQ9QTubJ40qTRZFl3U8hwKgSfyFuSrxUAcVsgOub9Z0E3i7RApAzi2X6zvpbFBx6p5IB1Xylr3LMqN7eHpXjZ_yyJPjaVtg5hZiqDqIYBRdz7OTj43-iKitROtZTrV1jZUw&usqp=CAc"
    }
]

Product.objects.filter(name__icontains="headphone").delete()

for item in products:
    Product.objects.update_or_create(
        name=item["name"],
        defaults=item
    )

print("10 products updated successfully!")