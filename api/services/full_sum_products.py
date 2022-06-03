from api.models import Product


def full_sum():
    products = list(Product.objects.all())
    total_sum = 0
    for product in products:
        total_sum += product.price * product.quantity

    product_dict = {
        "products": products,
        "total_sum": total_sum
    }
    return product_dict
