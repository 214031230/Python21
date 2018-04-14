goods = [{"name": "电脑", "price": 1999},
           {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998},]

shopping_car = []
flag = True
while flag:
    print("商品列表".center(30, "-"))
    for i in range(len(goods)):
        print("%s.%s %s" % (i, goods[i]["name"], goods[i]["price"]))
    money = input("请输入你要充值的金额：").strip()
    if money.isdigit():
        money = int(money)
        while flag:
            choice = input("请输入您要购买的商品ID（Q退出）：").strip()
            if choice.isdigit():
                choice = int(choice)
                if choice < len(goods):
                    choice_num = input("请输入你要购买的数量：").strip()
                    if choice_num.isdigit():
                        choice_num = int(choice_num)
                        if (goods[choice]["price"] * choice_num) < money:
                            shopping_car.append({"name": goods[choice]["name"],
                                                 "price": goods[choice]["price"],
                                                 "个数": choice_num})
                            money = money - (goods[choice]["price"] * choice_num)
                            print("余额：%s" % (money,))
                            go_no = input("是否继续购买Y/N：").strip().upper()
                            if go_no == "Y":
                                continue
                            else:
                                print("购物车".center(30, "-"))
                                for i in range(len(shopping_car)):
                                    print("%s.%s %s￥ %s个" % (i, shopping_car[i]["name"],
                                                             shopping_car[i]["price"],
                                                             shopping_car[i]["个数"]))
                                flag = False
                        else:
                            print("余额不足！")

                    else:
                        print("请输入正确的金额！")

                else:
                    print("你输入的商品ID不存在！")
            elif choice == "q" or choice == "Q":
                print("购物车".center(30, "-"))
                for i in range(len(shopping_car)):
                    print("%s.%s %s￥ %s个" % (i, shopping_car[i]["name"],
                                                shopping_car[i]["price"],
                                                shopping_car[i]["个数"]))
                    flag = False
            else:
                print("请输入正确的商品ID！")
    else:
        print("请输入正确的金额！")
shopping_car = []
salry = int(input("请输入你的金额：").strip())
while True:
    print("商品列表！")
    for i in range(len(goods)):
        print(i, goods[i]["name"], goods[i]["price"])
    buy = input("请输入你要购买的商品ID  退出：Q：").strip()
    if not buy:continue
    if buy.isdigit():
        buy = int(buy)
        buy_num = input("请输入你购买的数量：").strip()
        if not buy_num: continue
        if buy_num.isdigit():
            buy_num = int(buy_num)
            if (goods[buy]["price"] * buy_num) < salry:
                print("购买成功")
                count = 1
                while count <= buy_num:
                    shopping_car.append({"name": goods[buy]["name"], "price": goods[buy]["price"]})
                    count += 1
                salry = salry - (goods[buy]["price"] * buy_num)
                print("余额：%s" % (salry))
                choice_goon = input("是否继续购买：")
                if choice_goon == "y" or choice_goon == "Y":
                    continue
                else:
                    price = 0
                    for i in range(len(shopping_car)):
                        print(i)
                        print("订单%s： %s  %s￥" % (i, shopping_car[i]["name"], shopping_car[i]["price"]))
                        price = price + shopping_car[i]["price"]
                    print("一共消费:%s" % (price,))
                    break
            else:
                print("金额不够！")
    if buy == "q" or buy == "Q":
        for i in range(len(shopping_car)):
            print("订单%s： %s  %s￥" % (i, shopping_car[i]["name"], shopping_car[i]["price"]))
        break



