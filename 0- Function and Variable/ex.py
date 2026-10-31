def main():
    cau=int(input("chọn câu: "))
    if cau==1:
        name=input("Tên của bro là gì: ")
        age=input("Tuổi của bro là bao nhiêu: ")
        print(greet(name,age))
    elif cau==2:
        c=input("Nhập độ C: ")
        print(f"Độ F là {c_to_f(c)}")
    elif cau==3:
        string=input("Nhập câu: ")
        so_kytu, so_tu = count(string)
        print(f"Có {so_kytu} ký tự, {so_tu} từ")
    elif cau==4:
        dai=input("Nhập chiều dài: ")
        rong=input("Nhập chiều rộng: ")
        dien_tich=area(dai,rong)
        gia=input("Nhập giá mỗi m²")
        prices=round(price(dien_tich,gia))
        print(f"Diện tích: {dien_tich} m² - Giá: {prices:,} đ. ")
    else:
        print("chọn câu từ 1 đền 4") 





def greet(name, age):
    name=name.title()
    age=int(age)
    return f"Chào {name}, năm sau ông {age+1} tuổi"
def c_to_f(c):
    f=float(c)*(9/5)+32
    return f
def count(a):
    nOfCharacter=len(a.strip())
    nOfWord=len(a.strip().split())
    return nOfCharacter, nOfWord
def area(dai,rong):
    area=float(dai)*float(rong)
    return area
def price(dien_tich,gia):
    price=dien_tich*float(gia)
    return price


main()