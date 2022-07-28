# metric or imperial
choose=(input("Choose imperial or metric system by writing its name: "))

# calculations

def m_bmi(height, weight):
    global m_calc
    if height and weight>0:
        print("Your BMI score is: ", round(m_calc,2))

def i_bmi(height, weight):
    global i_calc
    if height and weight>0:
        print("Your BMI score is: ", round(i_calc,2))        

# execution of code

if choose =='metric' or choose=='imperial':
    hight=int(input("Type in your height: "))
    weight=int(input("Type in your weight: "))
    m_calc=((weight/hight**2)*10000)
    i_calc=(((weight/hight**2))*703)
    if choose=='metric':
        m_bmi(hight,weight)
# sections - underweight/optimum/overweight/obesity
        if m_calc<=18.5:
            print("You are underweight.")
        elif m_calc>18.5 and m_calc<25:
            print("Your BMI is optimal.")
        elif m_calc>=25 and m_calc<30:
            print("You are overwieght.")
        elif m_calc>=30:
            print("You are obese.")
    else:
        i_bmi(hight,weight)
        if i_calc<=18.5:
            print("You are underweight.")
        elif i_calc>18.5 and i_calc<25:
            print("Your BMI is optimal.")
        elif i_calc>=25 and i_calc<30:
            print("You are overwieght.")
        elif i_calc>=30:
            print("You are obese.")
else:
    print("Seems like you didn't type in the right system...")
