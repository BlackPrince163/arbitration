import openpyxl

from api.models import Product


def run():
    _PATH = r"D:\PythonProject\arbitration\products.xlsx"
    products = openpyxl.open(_PATH, read_only=True)
    sheet = products.active
    product_list = []

    for row in range(2, sheet.max_row + 1):
        product = {}
        product["product_name"] = sheet[row][0].value
        product["price"] = float(sheet[row][1].value)
        product["quantity"] = float(sheet[row][2].value)

        product_model = Product(name=product["product_name"], price=product["price"], quantity=product["quantity"])

        product_list.append(product_model)

    Product.objects.bulk_create(product_list)
