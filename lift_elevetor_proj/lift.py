from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Ground Floor = 0, Top Floor = 4
current_floor = 0

# Truth Table for 7-Segment Display (A, B, C, D, E, F, G)
truth_table = {
    0: [1, 1, 1, 1, 1, 1, 0],  # Ground (0)
    1: [0, 1, 1, 0, 0, 0, 0],  # Floor 1
    2: [1, 1, 0, 1, 1, 0, 1],  # Floor 2
    3: [1, 1, 1, 1, 0, 0, 1],  # Floor 3
    4: [0, 1, 1, 0, 0, 1, 1]   # Floor 4
}

@app.route('/')
def home():
    raw_segments = truth_table[current_floor]
    # Python me hi 'on' class calculate kar li taaki HTML clean rahe
    segments = ['on' if s == 1 else '' for s in raw_segments]
    return render_template('index.html', floor=current_floor, segments=segments)

@app.route('/move/<int:target_floor>', methods=['POST'])
def move_lift(target_floor):
    global current_floor
    if 0 <= target_floor <= 4:
        current_floor = target_floor
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)