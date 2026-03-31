from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Simple in-memory data store
poll_data = {
    "question": "Which DevOps tool is your favorite?",
    "options": ["Docker", "Kubernetes", "Terraform", "Jenkins"],
    "votes": {"Docker": 0, "Kubernetes": 0, "Terraform": 0, "Jenkins": 0}
}

@app.route('/')
def index():
    return render_template('index.html', data=poll_data)

@app.route('/vote', methods=['POST'])
def vote():
    selection = request.form.get('quiz_option')
    if selection in poll_data['votes']:
        poll_data['votes'][selection] += 1
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)