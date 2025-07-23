n = int(input("Enter a positive number: ")) # รับค่า n 
sum_even = 0 # กำหนดตัวแปร
for i in range(1, n + 1): # ใช้ for loop เพื่อตรวจเลขคู่และรวมค่า
    if i % 2 == 0:
        sum_even += i
print(sum_even) # แสดงผลลัพธ์
