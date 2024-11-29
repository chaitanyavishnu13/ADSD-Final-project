from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    print("Home route accessed.")  # Debug log
    return render_template('home.html')

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        print("POST request received for adding a recipe.")  # Debug log
        # Get recipe data from the form
        name = request.form['name']
        ingredients = request.form['ingredients']
        preferences = request.form['preferences']
        calories = request.form['calories']

        # Save the recipe to the database
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO recipes (name, ingredients, dietary_preferences, calories) VALUES (?, ?, ?, ?)",
                (name, ingredients, preferences, calories)
            )
            conn.commit()
            conn.close()
            print("Recipe added successfully.")  # Debug log
        except Exception as e:
            print(f"Error adding recipe: {e}")  # Debug log
        return redirect(url_for('home'))
    return render_template('add_recipe.html')

@app.route('/recommend_recipe', methods=['GET'])
def recommend_recipe():
    print("Recommend route accessed.")  # Debug log
    preferences = request.args.get('preferences', '')
    calories = request.args.get('calories', 0)

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        query = """
            SELECT name, ingredients, calories 
            FROM recipes 
            WHERE dietary_preferences LIKE ? AND calories <= ?
        """
        cursor.execute(query, (f"%{preferences}%", calories))
        recipes = cursor.fetchall()
        conn.close()
        print(f"Recipes fetched: {recipes}")  # Debug log
    except Exception as e:
        print(f"Error fetching recipes: {e}")  # Debug log
        recipes = []
    
    return render_template('recommend_recipe.html', recipes=recipes)

if __name__ == '__main__':
    print("Starting Flask app...")  # Debug log
    app.run(debug=True)
