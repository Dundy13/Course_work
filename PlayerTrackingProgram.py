import sqlite3

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.rebounds = 0
        self.assists = 0
        self.blocks = 0
        self.steals = 0
        self.turnovers = 0
        self.three_pointers_made = 0
        self.two_pointers_made = 0
        self.free_throws_made = 0

    def display_stats(self):
        print(f"\nPlayer: {self.name}")
        print(f"Points: {self.points}")
        print(f"Rebounds: {self.rebounds}")
        print(f"Assists: {self.assists}")
        print(f"Blocks: {self.blocks}")
        print(f"Steals: {self.steals}")
        print(f"Turnovers: {self.turnovers}")
        print(f"3PT Made: {self.three_pointers_made}")
        print(f"2PT Made: {self.two_pointers_made}")
        print(f"Free Throws Made: {self.free_throws_made}")

def create_table():
    conn = sqlite3.connect('basketball_performance.db')
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS PlayerPerformance (
        id INTEGER PRIMARY KEY,
        name TEXT,
        points INTEGER,
        rebounds INTEGER,
        assists INTEGER,
        blocks INTEGER,
        steals INTEGER,
        turnovers INTEGER,
        three_pointers_made INTEGER,
        two_pointers_made INTEGER,
        free_throws_made INTEGER
    );
    '''

    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

def select_all():
    conn = sqlite3.connect('basketball_performance.db')
    cursor = conn.cursor()

    select_query = 'SELECT * FROM PlayerPerformance;'
    cursor.execute(select_query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def track_performance(player):
    print(f"\nEnter performance for {player.name}")
    player.points = int(input("Points: "))
    player.rebounds = int(input("Rebounds: "))
    player.assists = int(input("Assists: "))
    player.blocks = int(input("Blocks: "))
    player.steals = int(input("Steals: "))
    player.turnovers = int(input("Turnovers: "))
    player.three_pointers_made = int(input("3PT Made: "))
    player.two_pointers_made = int(input("2PT Made: "))
    player.free_throws_made = int(input("Free Throws Made: "))
    print("Performance tracked successfully!\n")

    conn = sqlite3.connect('basketball_performance.db')
    cursor = conn.cursor()

    insert_query = '''
    INSERT INTO PlayerPerformance (name, points, rebounds, assists, blocks, steals, turnovers, three_pointers_made, two_pointers_made, free_throws_made)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    '''

    cursor.execute(insert_query, (player.name, player.points, player.rebounds, player.assists, player.blocks, player.steals,
                                  player.turnovers, player.three_pointers_made, player.two_pointers_made, player.free_throws_made))

    conn.commit()
    conn.close()

def main():
    create_table()
    # select_all()  # Uncomment if you want to display all records before starting to track performance
    players = []
    for i in range(1, 12):
        player_name = input(f"Enter name for Player {i}: ")
        players.append(Player(player_name))

    while True:
        print("\nBasketball Performance Tracker")
        print("1. Track Performance")
        print("2. Display Stats")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            player_choice = int(input("Select player (1-9): "))
            if 1 <= player_choice <= len(players):
                track_performance(players[player_choice - 1])
            else:
                print("Invalid player selection. Try again.")

        elif choice == "2":
            for player in players:
                player.display_stats()

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()