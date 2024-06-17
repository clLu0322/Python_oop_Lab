import re

def main():
    with open('log.txt') as data:
        vip_dict = {}
        mems_dict = {}
        product_sales = {}
        vip_pattern = re.compile(r'^\[VIP\] (\w+) buys (\w+) for \$(\d+)')
        member_pattern = re.compile(r'^(\w+) buys (\w+) for \$(\d+)')

        for line in data:
            vip_match = vip_pattern.search(line)
            if vip_match:
                name, product, price = vip_match.groups()
                price = int(price)
                if name not in vip_dict:
                    vip_dict[name] = {}
                if product not in vip_dict[name]:
                    vip_dict[name][product] = 0
                vip_dict[name][product] += price

                if product not in product_sales:
                    product_sales[product] = 0
                product_sales[product] += price
            else:
                mems_match = member_pattern.search(line)
                if mems_match:
                    name, product, price = mems_match.groups()
                    price = int(price)
                    if name not in mems_dict:
                        mems_dict[name] = {}
                    if product not in mems_dict[name]:
                        mems_dict[name][product] = 0
                    mems_dict[name][product] += price

                    if product not in product_sales:
                        product_sales[product] = 0
                    product_sales[product] += price

    print("[VIP]")
    for name, purchases in vip_dict.items():
        purchases_str = ", ".join([f"{product}: {price}" for product, price in purchases.items()])
        print(f"{name} buys {purchases_str}")

    print("\n[MEMBERS]")
    for name, purchases in mems_dict.items():
        purchases_str = ", ".join([f"{product}: {price}" for product, price in purchases.items()])
        print(f"{name} buys {purchases_str}")

    print("\nTotal sales:")
    for product, total in product_sales.items():
        print(f"Total {product} sales: {total}")

if __name__ == "__main__":
    main()

