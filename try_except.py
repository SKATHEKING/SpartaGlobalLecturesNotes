

phone_brands = ('Samsung', 'Apple', 'Google', 'Xiaomi', 'Huawei')

try:
    phone_brands.append('Nokia')
except:
    print('This a non mutable data structure you cannot append to it ')
else:
    print('This a mutable data structure')
finally:
    print('This a tupple which is a non mutable data structure containing the top phone brands at the moment')