from flask import Flask, render_template, request, redirect, url_for
import json
import os
import random

app = Flask(__name__)

QUESTIONS_PER_QUIZ = int(os.environ.get("QUESTIONS_PER_QUIZ", "20"))
QUIZ_TIME_MINUTES = int(os.environ.get("QUIZ_TIME_MINUTES", "20"))

with open("questions.json", "r", encoding="utf-8") as f:
    ALL_QUESTIONS = json.load(f)


def choose_questions():
    count = min(QUESTIONS_PER_QUIZ, len(ALL_QUESTIONS))
    return random.sample(ALL_QUESTIONS, count)


@app.route("/")
def index():
    return render_template(
        "index.html",
        total_available=len(ALL_QUESTIONS),
        quiz_size=min(QUESTIONS_PER_QUIZ, len(ALL_QUESTIONS)),
        time_minutes=QUIZ_TIME_MINUTES
    )


@app.route("/quiz", methods=["GET", "POST"])
def quiz():

    # Quand l'utilisateur termine le quiz
    if request.method == "POST":

        name = request.form.get("name", "").strip()
        ids_raw = request.form.get("question_ids", "")

        if not name or not ids_raw:
            return redirect(url_for("index"))

        try:
            ids = [
                int(x)
                for x in ids_raw.split(",")
                if x.strip()
            ]
        except ValueError:
            return redirect(url_for("index"))

        # Retrouver les questions
        by_id = {q["id"]: q for q in ALL_QUESTIONS}

        selected = [
            by_id[i]
            for i in ids
            if i in by_id
        ]

        if not selected:
            return redirect(url_for("index"))

        # Calcul du score
        answers = {}
        score = 0

        for q in selected:

            user_answer = request.form.get(
                f"q{q['id']}",
                ""
            )

            answers[str(q["id"])] = user_answer

            if user_answer == q["answer"]:
                score += 1

        total = len(selected)

        percentage = round(
            score / total * 100,
            2
        )

        # Informations nécessaires pour la correction
        review_questions = [
            {
                "id": q["id"],
                "page": q.get("page"),
                "image": q["image"],
                "answer": q["answer"]
            }
            for q in selected
        ]

        # IMPORTANT :
        # Rien n'est enregistré dans une base de données.
        # Le résultat est envoyé directement à la page result.html.

        return render_template(
            "result.html",
            name=name,
            score=score,
            total=total,
            percentage=percentage,
            answers=answers,
            questions=review_questions
        )

    # Affichage du quiz
    name = request.args.get("name", "").strip()

    if not name:
        return redirect(url_for("index"))

    selected = choose_questions()

    return render_template(
        "quiz.html",
        name=name,
        questions=selected,
        time_minutes=QUIZ_TIME_MINUTES
    )


if __name__ == "__main__":
    app.run(debug=True)