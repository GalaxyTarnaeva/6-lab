two_dict = {"Шенфельд","Алёхин","Тарнаева","Хохлов","Сидорова"}
chi_dict = {"Щукина","Киркоров","Балдина","Щербаков","Гумеров"}
cutr_dict = {"Австрия":"Вена","Азербайджан":"Баку","Армения":"Ереван","Бельгия":"Брюссель","Великобритания":"Лондон","Франция":"Париж","Белоруссия":"Минск",
"Болгария":"София","Сербия":"Белград","Польша":"Варшава","Ирландия":"Дублин","Чехия":"Прага","США":"Вашингтон",}
print("Люди, знающие несколько языков",two_dict)
print("Люди, знающие китайский язык",chi_dict)
for a in sorted (cutr_dict):
    print (a,"-", cutr_dict[a])