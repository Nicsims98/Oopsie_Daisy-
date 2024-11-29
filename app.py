from flask import Flask, jsonify, request 
from flask_cors import CORS
import random
# Create the Flask app
app = Flask(__name__)
CORS(app)  # This enables CORS for all routes
# Define greetings
greetings = [
    "Welcome to Oopsie Daisy!",
    "Ready to make some excuses?",
]
# Define excuses dictionary
excuses = {
    "Work": [
        "I'm sorry, but I have to fight our company's competitors.",
        "I'm sorry, but I have to help HR with the recruitment process of the new Sigmas.",
        "I'm sorry, but I have to help the company with the new product launch for the Grimace Shake.",
        "No can do, boss that is real Unc behavior and the chat is going to hear about this.",
        "I will have to miss the meeting because Roblox just released a new update that is baby gronk."
    ],
    "Family": [
        "Chat is this real?",
        "Bro thinks he's Carti.",
        "Bruh, I will have to flake on the plans because it's cringe.",
        "Hear me out, my day is full as I have to Mew today.",
        "I have to serve at my Nana's funeral because if I don't who will?"
    ],
    "Chaos": [
        "Mercury is in retrograde and my chakras are misaligned.",
        "My crytals warned me about you and I'm telling everyone what they said.",
        "I'm too cooked for this.",
        "Crazy? I was crazy once. They locked me in a room. A rubber room. A rubber room with rats. And rats make me crazy.",
        "The gyatt is too crazy for me to be around anymore."
    ],
    "School": [
        "Teach I'm just an Ipad Kid how do you expect me to get this assignment done?",
        "I have to help Roblox with a new level no cap",
        "I got the ick from your assignment I will have to pass fam.",
        "I know you popped off with giving this assignment but I got stuck in a virtual reality game and couldn't log out until I defeated the final boss. It took longer than expected!",
        "I was on a social media detox, and I accidentally deleted my homework instead of my TikTok app. It's gone forever!"
    ],
    "Creep that won't stop texting you": [
        "I'm in a serious Don Pollo crisis—my chicken just escaped and is roaming the neighborhood like it owns the place! Gotta catch it before it starts a whole TikTok trend!",
        "I'm in full sigma grindset mode right now—gotta focus on my goals! Texting is a distraction I can't afford!",
        "I'm currently dealing with a sussy baka situation over here! Until I figure it out, my texting skills are on lockdown!",
        "I'm experiencing a glitchy reality check where everything feels like a meme! Can't text while trying to figure out what's real!",
        "I've got so much rizz right now that I can't focus on anything else! My charisma is off the charts—sorry, can't chat!"
    ]
}
# Define routes
@app.route('/')
def welcome():
    return random.choice(greetings)
@app.route('/api/test')
def test():
    return jsonify({"message": "Hello from Flask!"})
@app.route("/api/excuse", methods=["POST"])
def get_excuse_post():
    try:
        data = request.json
        category = data.get("category", "Work")
        
        # Check if category exists
        if category not in excuses:
            return jsonify({"error": "Oops! That category doesn't exist"}), 400
        excuse = random.choice(excuses[category])
        return jsonify({"excuse": excuse})
    except:
        return jsonify({"error": "Something went wrong!"}), 500
@app.route("/api/categories", methods=["GET"])
def get_categories():
    return jsonify({"categories": list(excuses.keys())})
if __name__ == '__main__':
    app.run()
