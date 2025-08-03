from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    req = request.get_json(force=True)

    parameters = req.get("queryResult", {}).get("parameters", {})
    genre = parameters.get("book_genre", "").lower()

    BOOK_RECOMMENDATIONS = {
        "fantasy": [
            "Harry Potter by J.K. Rowling",
            "The Hobbit by J.R.R. Tolkien",
            "Percy Jackson by Rick Riordan"
        ],
        "sci-fi": [
            "Dune by Frank Herbert",
            "Ender’s Game by Orson Scott Card",
            "The Martian by Andy Weir"
        ],
        "self-help": [
            "Atomic Habits by James Clear",
            "The 7 Habits of Highly Effective People by Stephen Covey",
            "Think Like a Monk by Jay Shetty"
        ],
        "non-fiction": [
            "Sapiens by Yuval Noah Harari",
            "Educated by Tara Westover",
            "The Immortal Life of Henrietta Lacks by Rebecca Skloot"
        ],
        "biography": [
            "Becoming by Michelle Obama",
            "Steve Jobs by Walter Isaacson",
            "Long Walk to Freedom by Nelson Mandela"
        ],
        "fiction": [
            "The Great Gatsby by F. Scott Fitzgerald",
            "To Kill a Mockingbird by Harper Lee",
            "The Catcher in the Rye by J.D. Salinger"
        ],
        "romance": [
            "The Fault in Our Stars by John Green",
            "Pride and Prejudice by Jane Austen",
            "Me Before You by Jojo Moyes"
        ]
    }

    if genre in BOOK_RECOMMENDATIONS:
        book_list = BOOK_RECOMMENDATIONS[genre]
        response_text = f"Here are some popular {genre.title()} books:\\n- " + "\\n- ".join(book_list)
    else:
        response_text = "Sorry, I don’t have recommendations for that genre right now."

    return jsonify({"fulfillmentText": response_text})

if __name__ == "__main__":
    app.run()
