import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create the 'recipes' table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    ingredients TEXT NOT NULL,
    dietary_preferences TEXT NOT NULL,
    calories INTEGER NOT NULL
)
''')

# Insert some sample recipes into the database
sample_recipes = [
    ('Vegetarian Stir Fry', 'Broccoli, Bell Peppers, Soy Sauce, Garlic, Ginger', 'vegetarian', 250),
    ('Grilled Chicken Salad', 'Grilled Chicken, Romaine Lettuce, Cherry Tomatoes, Parmesan, Caesar Dressing', 'high-protein', 400),
    ('Avocado Toast', 'Avocado, Whole Grain Bread, Olive Oil, Salt, Pepper', 'vegan', 150),
    ('Keto Omelette', 'Eggs, Cheese, Spinach, Bacon', 'low-carb', 300),
    ('Greek Salad', 'Tomato, Cucumber, Feta Cheese, Olives, Olive Oil', 'vegetarian', 200)
]

# Insert the sample recipes if the table is empty
cursor.executemany('''
INSERT INTO recipes (name, ingredients, dietary_preferences, calories)
VALUES (?, ?, ?, ?)
''', sample_recipes)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database setup complete with sample recipes.")
