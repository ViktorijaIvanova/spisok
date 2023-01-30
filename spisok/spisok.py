spisok=[]
print("выбери более понравившейся вариант от 1 до 7")
while True:
     print("1-добавить букву в список")
     print("2-склеить списки\n3-добавить букву на i- позиции")
     print("3-удалить элемент")
     print("4-очистить список")
     print("5-развернуть список")
     print("6-считает количество элементов со значением x ")
     print("7-изменяет на нижний регистр весь лист")
     valik=int(input())
     if valik==1:
         a=input("введи букву")
         spisok.append(a)
         print(f"добавили {a} новый список", spisok)
     elif valik==2:
         spisok.extend(a)
         print(spisok)
     elif valik==3:
         a=(input("введи бкуву, которую хочешь удалить "))
         a=a.lower()
         spisok=[]
         for t in (spisok):
             spisok.append(t.lower())
             n=spisok.count(a)
         if n>0:
             for i in range(n):
                 spisok.remove(a)
         else:
             print("искомой буквы нет")
     elif valik==4:
        spisok.clean()
     elif valik==5:
         spisok.reverse()
     elif valik==6:
         h=input("введите искомую букву ")
         g=spisok.count(h)
         print(g)
     elif valik==7:
         spisok=[]
         for t in (spisok):
             spisok.append(t.lower())
         print(spisok)





#
spisok=[]
print("выбери более понравившейся вариант от 1 до 6")
while True:
    print("1-слово большими")
    print("2-слово маленькими")
    print("3-разбиение строки по разделителю")
    print("4-переводит первый символ строки в верхней регистр, а все остальные в нижний")
    print("5-переводит символы нижнего регистра в верхний, а верхнего- в нижний")
    print("6-первую букву каждого слова переводит в верхний регистр,а все остальные в нижний")
    print("7-КОНЕЦ")
    pan_Am=float(input())
    if pan_Am==1:
        a=input("введи букву/слово: ")
        print(a.upper())
        print(f"добавили {a}",spisok)
    elif pan_Am==2:
        b=input("введи букву: ")
        print(b.lower())
        print(f"добавили {b}",spisok)
    elif pan_Am==3:
        c=input("введи букву: ")
        print(c.split())
        print(f"добавили {c}",spisok)
    elif pan_Am==4:
        d=input("введи букву: ")
        print(d.capitalize())
        print(f"добавили {d}",spisok)
    elif pan_Am==5:
        v=input("введи букву: ")
        print(v.swapcase())
        print(f"добавили {v}",spisok)
    elif pan_Am==6:
        b=input("введи букву: ")
        print(b.lower())
        print(f"добавили {b}",spisok)
    elif pan_Am==7:
        break












spisok=[] #пустой список
numbers=[1,2,3,4,5]
abc=["abc","B","C"]
slovo="programmeerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
    print("1-добавить букву в список")
    print("2-склеить списки\n3-добавить букву на i-позицию")
    valik=int(input())
    if valik==1:
        a=input("введи букву")
        slovo_list.append(a)
        print(f"ДОбавили {a} новый список",slovo_list)
    elif valik==2:
      slovo_list.extend(abc)
      print(slovo_list)
    elif valik==3:
      a=input("введи букву, которую хочешь добавить")
      i=int(input("введи номер позиции, куда хочешь добавить букву"))
      slovo_list.insert(i-1,a) #0,1,2...
      print(slovo_list)
    elif valik==4:
        a=input("введи букву, которую хочешь удалить")
        n=slovo_list.count(a)
        if n>0:
            for i in range(n):
                slovo_list.remove(a)
    else:
     print("искомой буквы нет")
     print(slovo_list)





