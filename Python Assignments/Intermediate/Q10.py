def stone_piles(pile_number):
    pile_list =[]
    for n in range (pile_number):
        pile_list.append(pile_number)
        pile_number+=2

    print(f"Stones in a single pile: {pile_list}")
        



pile_number = int(input("Enter the pile number:"))
stone_piles(pile_number)
