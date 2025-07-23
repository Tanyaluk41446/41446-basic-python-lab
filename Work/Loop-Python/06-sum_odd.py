n = int(input("Enter a positive number: ")) # รับค่า n
sum_odd = 0 # กำหนดตัวแปร
for i in range(1, n + 1): # ใช้ for loop ตรวจเลขคี่และรวมค่า
    if i % 2 != 0:
        sum_odd += i
print(sum_odd) # แสดงผลลัพธ์
