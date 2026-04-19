from flask import Flask, request

app = Flask(__name__)

def save_note(note):
    with open("notes.txt", "a") as f:
        f.write(note + "\n")

def get_notes():
    try:
        with open("notes.txt", "r") as f:
            return f.readlines()
    except:
        return []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        save_note(note)

    notes = get_notes()
    output = """
    <h2>My Notes App 📝</h2>
    <form method="post">
        <input type="text" name="note" placeholder="Enter note">
        <button type="submit">Add</button>
    </form>
    <h3>All Notes:</h3>
    """

    for n in notes:
        output += f"<p>• {n}</p>"

    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
