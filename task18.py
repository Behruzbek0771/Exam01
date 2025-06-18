vazn = float(input("Vazningixni kriting 'kg': "))
boy = float(input("Bo'yinggizni kriting 'm' "))
BMI = vazn/pow(boy,2)

if BMI < 18.5: 
    print("Kam vazn")
elif 18.5 <= BMI < 25:
    print("Normal vazn")
elif 25 <= BMI < 30:
    print("Ortiqcha vazn")
elif 30<= BMI:
    print("Semizlik")