from flask import Flask, render_template, request

app = Flask(__name__)

# --- Python Functions ---
def get_string_operations(name):
    return {
        "Uppercase": name.upper(),
        "Lowercase": name.lower(),
        "Reversed": name[::-1],
        "Length": len(name)
    }

def add_language(language_list, new_lang):
    if new_lang and new_lang not in language_list:
        language_list.append(new_lang.capitalize())
        return f"{new_lang.capitalize()} added successfully!"
    return "Invalid or duplicate language."

def delete_language(language_list, lang_to_delete):
    if lang_to_delete in language_list:
        language_list.remove(lang_to_delete)
        return f"{lang_to_delete} removed successfully!"
    return f"{lang_to_delete} not found."

def clear_languages(language_list):
    language_list.clear()
    return "All languages cleared!"

def sort_languages(language_list):
    language_list.sort()
    return "Languages sorted alphabetically!"

# --- Routes ---
@app.route('/')
def home():
    return render_template("index.html", title="Home")

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    message, string_ops = None, None
    if request.method == 'POST':
        name = request.form.get('name')
        if name.strip():
            message = f"Hello, {name.title()}!"
            string_ops = get_string_operations(name)
        else:
            message = "Please enter a valid name."
    return render_template("greet.html", title="Greet", message=message, string_ops=string_ops)

@app.route('/favorites', methods=['GET', 'POST'])
def favorites():
    global languages
    if 'languages' not in globals():
        languages = ["Python", "C++", "JavaScript", "Go"]

    message = None
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            new_lang = request.form.get('language')
            message = add_language(languages, new_lang)
        elif action == 'delete':
            lang_to_delete = request.form.get('language')
            message = delete_language(languages, lang_to_delete)
        elif action == 'clear':
            message = clear_languages(languages)
        elif action == 'sort':
            message = sort_languages(languages)

    return render_template("favorites.html", title="Favorites", languages=languages, message=message)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

# --- Python Helper Functions ---
def add_language(language_list, new_lang):
    if new_lang:
        new_lang = new_lang.strip().capitalize()
        if new_lang not in language_list:
            language_list.append(new_lang)
            return f"{new_lang} added successfully!"
        else:
            return f"{new_lang} already exists."
    return "Please enter a language name."

def clear_languages(language_list):
    if language_list:
        language_list.clear()
        return "All languages cleared."
    return "No languages to clear."

def sort_languages(language_list):
    if language_list:
        language_list.sort()
        return "Languages sorted alphabetically."
    return "No languages to sort."

def delete_selected_languages(language_list, selected):
    if not selected:
        return "No languages selected for deletion."
    deleted = []
    for lang in selected:
        if lang in language_list:
            language_list.remove(lang)
            deleted.append(lang)
    if deleted:
        return f"Deleted {', '.join(deleted)} successfully!"
    return "No matching languages found."

# --- Flask Route ---
@app.route('/favorites', methods=['GET', 'POST'])
def favorites():
    global languages
    if 'languages' not in globals():
        languages = ["Python", "C++", "JavaScript", "Go"]

    message = None
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add':
            new_lang = request.form.get('language')
            message = add_language(languages, new_lang)
        elif action == 'delete_selected':
            selected = request.form.getlist('selected_languages')
            message = delete_selected_languages(languages, selected)
        elif action == 'clear':
            message = clear_languages(languages)
        elif action == 'sort':
            message = sort_languages(languages)

    return render_template("favorites.html", title="Favorites", languages=languages, message=message)

if __name__ == '__main__':
    app.run(debug=True)
