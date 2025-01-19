```markdown
# Trivia Quiz Game

## Descriere
Trivia Quiz Game este un joc interactiv de tip quiz, în care utilizatorul trebuie să răspundă corect la întrebări din diverse domenii. Jocul oferă opțiuni multiple și calculează scorul pe baza răspunsurilor corecte ale utilizatorului.

## Funcționalități
- Întrebări și răspunsuri multiple
- Verificarea răspunsurilor și afișarea unui mesaj "Corect!" sau "Greșit!"
- Calcularea scorului final
- Validarea răspunsurilor introduse de utilizator
- Mesaje de eroare pentru răspunsuri invalide

## Instalare

1. **Clonează repository-ul** sau descarcă fișierele:
   ```bash
   git clone https://github.com/username/trivia-quiz-game.git
   ```

2. **Instalează Python** (dacă nu ai deja instalat):
   - Descarcă și instalează Python de pe [pagina oficială](https://www.python.org/downloads/).

3. **Instalează dependențele** (dacă sunt necesare):
   Dacă ai nevoie de biblioteci suplimentare, instalează-le folosind pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Fișierul de întrebări JSON**:
   Asigură-te că fișierul `questions.json` conține întrebările și opțiunile corespunzătoare.

## Cum se joacă
1. Deschide terminalul și navighează către directorul proiectului.
2. Rulează jocul:
   ```bash
   python trivia_game.py
   ```

3. Jocul va începe și vei fi ghidat prin întrebările din quiz. Trebuie să alegi un răspuns valid (un număr între 1 și opțiunile disponibile).

4. După finalizarea jocului, scorul final va fi afișat.

## Structura fișierelor
- **triviaGame.py** - Fișierul principal al jocului, care conține logica jocului și implementarea întrebărilor.
- **questions.json** - Fișierul care conține întrebările și opțiunile de răspuns, în format JSON.
```

