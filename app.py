from flask import Flask, render_template, request

app = Flask(__name__)

profile = {
    "name": "Frans Itumeleng Makhafola",
    "title": "Software Developer | Python | Linux",
    "about": """
    I am a passionate Software Developer from South Africa with a National
    Diploma in IT: Software Development from Tshwane University of Technology.
    I enjoy building automation tools, configuration software and Linux systems.
    """,
    "skills": {
        "Python":90,
        "Linux":85,
        "Networking":70,
        "Tkinter":80,
        "SSH Automation":85
    },
    "projects":[
        {
            "name":"Site Configurator Software",
            "description":"Python Tkinter application used to configure remote sites through SSH."
        },
        {
            "name":"Camera + LED Control System",
            "description":"Linux Python system controlling USB camera and LED night vision."
        },
        {
            "name":"Computer Hardware Sales System",
            "description":"Final year project for managing computer sales across multiple stores."
        }
    ],
    "linkedin":"https://www.linkedin.com/in/frans-itumeleng-makhafola-5b4aa4194"
}

@app.route("/")
def home():
    return render_template("index.html", profile=profile)

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    message = request.form.get("message")
    print(name, message)
    return "Message sent!"

if __name__ == "__main__":
    app.run(debug=True)
