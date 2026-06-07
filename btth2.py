product_list = [
"P01-Tai Nghe Bluetooth-550000-4.5",
"P02-Chuột Không Dây-250000-4.8",
"P03-Bàn Phím Cơ-850000-4.5"
]

def display_list(products):
    if not products:
        print("Danh sách trống")
        return
    print("--- DANH SÁCH TEM NHÃN ---")
    for product in products:
        product = product.split("-")
        print(f"Mã: {product[0]:<6}| Tên: {product[1]:<20}| Giá: {f'{int(product[2]):,} VND':<10}| Rating: {product[3]}*")


def sort_list(products):
    if not products:
        print("Danh sách trống")
        return
    print("--- SẮP XẾP SẢN PHẨM ---")
    print("Đã sắp xếp thành công! Cập nhật danh sách:")
    list_after_sort = sorted(products, key = lambda product: (-float(product.split("-")[3]), int(product.split("-")[2])))
    for index, product in enumerate(list_after_sort, start=1):
        print(f"{index}. {product}")


def calculate_total(products):
    total_sum = sum([int(product.split("-")[2]) for product in products])
    return total_sum



def main():
    while True:
        choice = input("""
============= E-COMMERCE ANALYTICS =============
1. Hiển thị tem nhãn sản phẩm (format_map & F-String)
2. Sắp xếp sản phẩm thông minh (sort key)
3. Tính tổng giá trị kho hàng (reduce)
4. Đóng hệ thống
================================================
    Chọn chức năng (1-4): """)
        if choice.isdigit():
            choice = int(choice)
        else:
            print("Vui lòng nhập số nguyên 1-5")
            continue
        
        match choice:
            case 1:
                display_list(product_list)
            
            case 2:
                sort_list(product_list)
                
            case 3:
                if not product_list:
                    print("Danh sách trống")
                    continue
                print("--- TỔNG GIÁ TRỊ KHO ---")
                print(f"Tổng giá trị các mặt hàng hiện tại là: {calculate_total(product_list):,} VND.")                
                
            case 4:
                print("Thoát chương trình.")
                break
        
            case _:
                print("Lỗi cú pháp")
                
    
main()
