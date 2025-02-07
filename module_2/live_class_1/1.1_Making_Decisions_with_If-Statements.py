# Check if a player has enough coins to buy an item
player_coins = 100
item_cost = 50

# This is like asking: "Do I have enough money?"
if player_coins >= item_cost:
    print("You can buy this item!")
    player_coins = player_coins - item_cost  # Subtract the cost
    print(f"You have {player_coins} coins left")