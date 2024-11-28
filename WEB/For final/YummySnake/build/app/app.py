from flask import Flask, render_template, jsonify, request, session, redirect, url_for
import random
import sqlite3
import time

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'SeCr37_k3y_f0R_XsCtF'

class Emoji:
    def __init__(self):
        self.yummy = '😋'
        self.happy = '😊'
        self.sad = '😢'
        self.love = '❤️'
        self.thumbs_up = '👍'
        self.party = '🎉'

emojis = Emoji()

class User:
    def __init__(self, user_id, username, best_time, declaration):
        self.user_id = user_id
        self.username = username
        self.best_time = best_time
        self.declaration = declaration

    def __repr__(self):
        return f"User(id={self.user_id}, username='{self.username}', best_time={self.best_time}, declaration='{self.declaration}')"

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            best_time REAL DEFAULT 0,
            declaration TEXT DEFAULT ''
        )
    ''')
    conn.commit()
    conn.close()

def get_user(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user_data = c.fetchone()
    conn.close()
    if user_data:
        return User(*user_data)  # 返回 User 对象
    return None

def add_or_update_user(username, best_time=None, declaration=None):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    user = get_user(username)
    if user:
        if best_time is not None and (user.best_time == 0 or best_time < user.best_time):
            c.execute('UPDATE users SET best_time = ? WHERE username = ?', (best_time, username))
        if declaration is not None:
            c.execute('UPDATE users SET declaration = ? WHERE username = ?', (declaration, username))
    else:
        c.execute('INSERT INTO users (username, best_time, declaration) VALUES (?, ?, ?)', (username, best_time or 0, declaration or ''))
    conn.commit()
    conn.close()

def reset_game():
    global snake, direction, food, score, start_time
    snake = [(10, 10)]
    direction = 'RIGHT'
    food = (random.randint(0, 19), random.randint(0, 19))
    score = 0
    start_time = time.time()

init_db()

@app.route('/')
def index():
    if 'username' not in session:
        return render_template('index.html')
    reset_game()
    return render_template('game.html', username=session['username'])

@app.route('/set_username', methods=['POST'])
def set_username():
    username = request.form.get('username')
    add_or_update_user(username)
    session['username'] = username
    return jsonify({'status': 'success'})

@app.route('/move', methods=['POST'])
def move():
    global snake, direction, food, score, start_time
    new_direction = request.json.get('direction')
    if new_direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
        direction = new_direction
    head_x, head_y = snake[0]
    if direction == 'UP':
        head_y -= 1
    elif direction == 'DOWN':
        head_y += 1
    elif direction == 'LEFT':
        head_x -= 1
    elif direction == 'RIGHT':
        head_x += 1
    if head_x < 0 or head_x >= 20 or head_y < 0 or head_y >= 20 or (head_x, head_y) in snake:
        reset_game()
        return jsonify({'status': 'game_over', 'score': score})
    snake.insert(0, (head_x, head_y))
    if (head_x, head_y) == food:
        score += 1
        while True:
            food = (random.randint(0, 19), random.randint(0, 19))
            if food not in snake:
                break
    else:
        snake.pop()
    if score >= 18:
        elapsed_time = time.time() - start_time
        add_or_update_user(session['username'], elapsed_time)
        return jsonify({'status': 'win', 'url': f"/snake_winwinwin?username={session['username']}"})
    return jsonify({'status': 'ok', 'snake': snake, 'food': food, 'score': score})

@app.route('/edit_declaration', methods=['GET', 'POST'])
def edit_declaration():
    if request.method == 'POST':
        emoji_selection = request.form.get('emoji_selection')
        username = request.form.get('username')
        declaration = request.form.get('declaration')
        if username:
            add_or_update_user(username, declaration=declaration)
            return redirect(url_for('win', emoji_selection=emoji_selection, username=username))
        else:
            return jsonify({'status': 'error', 'message': 'Username is required.'}), 400

    username = request.args.get('username')
    user = get_user(username)
    declaration = user.declaration if user else ''
    return render_template('edit_declaration.html', username=username, declaration=declaration)

@app.route('/snake_winwinwin')
def win():
    username = request.args.get('username')
    user = get_user(username)
    emoji_selection = request.args.get('emoji_selection', 'yummy')
    if emoji_selection == 'yummy':
        emoji = u"{emojis.yummy}"
    elif emoji_selection == 'happy':
        emoji = u"{emojis.happy}"
    elif emoji_selection == 'sad':
        emoji = u"{emojis.sad}"
    elif emoji_selection == 'love':
        emoji = u"{emojis.love}"
    elif emoji_selection == 'thumbs_up':
        emoji = u"{emojis.thumbs_up}"
    elif emoji_selection == 'party':
        emoji = u"{emojis.party}"

    declaration = u"{user.declaration}".format(user=user)
    final_declaration = (emoji+declaration).format(emojis=emojis)
    return render_template('win.html', best_time=user.best_time, username=username, declaration=final_declaration)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
