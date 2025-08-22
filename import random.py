from player import Player
from building import Building
from battle import Battle

def main():
    print("Welcome to Clash Warriors!")
    player = Player("Player1")
    while True:
        action = input("Choose action: [build, upgrade, collect, battle, quit]: ").lower()
        if action == 'build':
            player.build_structure()
        elif action == 'upgrade':
            player.upgrade_structure()
        elif action == 'collect':
            player.collect_resources()
        elif action == 'battle':
            Battle.fight(player)
        elif action == 'quit':
            print("Thanks for playing!")
            break
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()
