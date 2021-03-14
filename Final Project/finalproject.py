questions = [
    "Rusya'nın başkenti? ",
    "Türkiye'nin başkenti? ",
    "Italya'nın başkenti? ",
    "3+5? ",
    "Ispanya'nın başkenti? ",
    "6+8? ",
    "Listenin içerisinde bir elemandan kaç tane olduğunu bulmamızı sağlayan fonksiyon? ",
    "x=burcu /n print(x) çıktısı nedir? ",
    "x=5 x'in veri tipi nedir? ",
    "Almanya'nın başkenti? "
]
answers = ["moskova", "ankara", "roma", "8", "madrid" , "14", "count()", "burcu","int", "berlin"]

count = 0
dogrusayi = 0
for i in range(10):
    answer = input(questions[i])
    if answer.lower() == answers[i]:
        count += 10
        dogrusayi += 1
if dogrusayi>5:
    print(f'You are succesful. Your score is {count}')
else:
    print(f'You score is less than 50')



