import json


class Question:
    def __init__(self, text, options, correct_index):
        self.text = text
        self.options = options
        self.correct_index = correct_index

    def check_answer(self, answer_index):
        return answer_index == self.correct_index


class TriviaGame:
    def __init__(self):
        self.questions = []
        self.score = 0

    def load_questions(self):
        try:
            with open('questions.json', 'r') as file:
                data = json.load(file)
                for item in data:
                    question = Question(item['question'], item['options'], item['correct'])
                    self.questions.append(question)
        except FileNotFoundError:
            print("Eroare: Fișierul nu a fost găsit.")
            exit()

    def start_game(self):
        print("Bine ai venit la jocul Trivia!")
        print("Va trebui să răspunzi la întrebări, încearcă să obții cât mai multe răspunsuri corecte!\n")

        for index, question in enumerate(self.questions):
            print(f"Întrebarea {index + 1}) {question.text}")
            for i, option in enumerate(question.options):
                print(f"{i + 1}) {option}")

            while True:
                try:
                    user_answer = int(input("Răspunsul tău? (introduceți numărul) -> ")) - 1
                    if 0 <= user_answer < len(question.options):
                        if question.check_answer(user_answer):
                            print("Corect!\n")
                            self.score += 1
                        else:
                            print("Greșit!\n")
                        break
                    else:
                        print("Răspuns invalid. Alege un număr valid din opțiuni.\n")

                except ValueError:
                    print("Te rog să introduci un număr valid.\n")

    def show_score(self):
        print(f"Jocul s-a încheiat. Scorul tău: {self.score} din {len(self.questions)}.")


if __name__ == '__main__':
    game = TriviaGame()
    game.load_questions()
    game.start_game()
    game.show_score()
