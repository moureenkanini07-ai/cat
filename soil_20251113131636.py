soil_ph=float(input("enter soil ph(0-14):"))
if 0< soil_ph<14:
    print("invalid soil ph value")
    if soil_ph<5.5:
        soil_type="acidic"
        ai_advice="add agricultural lime:suitable for crops like potatoes and pineapples"
    elif  5.6<soil_ph<7.5:
          soil_type="neutral"
          ai_advice="ideal for most crops such as maize,beans and vegetables"
    else:
         soil_type="alkaline"
         ai_advice="add organic matter or sulphuirt,suitable for barley and cabbage"
print("soil ph:",soil_ph)
print("soil type:",soil_type)
print("ai advice:",ai_advice)
        
        

    