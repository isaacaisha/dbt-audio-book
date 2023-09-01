from flask import Flask, render_template, Response
from dictionary import (el_principito, el_principito_book_1, el_principito_book_2, el_principito_book_3,
                        el_principito_book_4, el_principito_book_5, el_principito_book_6, el_principito_book_7,
                        stella, stella_book, les_miserables, les_miserables_book)
from gtts import gTTS
import io
from datetime import datetime

app = Flask(__name__)


def generate_speech(text, lang='fr'):  # Set lang='fr' for French
    try:
        # Synthesize speech
        tts = gTTS(text=text, lang=lang)
        # Save speech to an in-memory BytesIO object
        speech_buffer = io.BytesIO()
        tts.write_to_fp(speech_buffer)
        speech_buffer.seek(0)  # Reset buffer position to the beginning
        return speech_buffer
    except Exception as e:
        print(f"Error synthesizing speech with gTTS: {e}")
        return None


@app.route('/', methods=['GET', 'POST'])
def home():
    el_principito_speech = el_principito  # Pass the text content directly
    stella_speech = stella
    les_miserables_speech = les_miserables

    return render_template('index.html',
                           el_principito_speech=el_principito_speech,
                           stella_speech=stella_speech,
                           les_miserables_speech=les_miserables_speech,
                           date=datetime.now().strftime("%a %d %B %Y"))


@app.route('/p-book-1', methods=['GET', 'POST'])
def principito_1():
    el_principito_book_speech_1 = el_principito_book_1  # Pass the text content directly

    return render_template('principito1.html',
                           el_principito_book_speech_1=el_principito_book_speech_1,
                           date=datetime.now().strftime("%a %d %B %Y"))


@app.route('/p-book-2', methods=['GET', 'POST'])
def principito_2():
    el_principito_book_speech_2 = el_principito_book_2  # Pass the text content directly

    return render_template('principito2.html',
                           el_principito_book_speech_2=el_principito_book_speech_2,
                           date=datetime.now().strftime("%a %d %B %Y"))


@app.route('/p-book-3', methods=['GET', 'POST'])
def principito_3():
    el_principito_book_speech_3 = el_principito_book_3  # Pass the text content directly

    return render_template('principito3.html',
                           el_principito_book_speech_3=el_principito_book_speech_3,
                           date=datetime.now().strftime("%a %d %B %Y"))


@app.route('/p-book-4', methods=['GET', 'POST'])
def principito_4():
    el_principito_book_speech_4 = el_principito_book_4  # Pass the text content directly

    return render_template('principito4.html',
                           el_principito_book_speech_4=el_principito_book_speech_4,
                           date=datetime.now().strftime("%a %d %B %Y"))


@app.route('/p-book-5', methods=['GET', 'POST'])
def principito_5():
    el_principito_book_speech_5 = el_principito_book_5  # Pass the text content directly

    return render_template('principito5.html',
                           el_principito_book_speech_5=el_principito_book_speech_5,
                           date=datetime.now().strftime("%a %d %B %Y"))


@app.route('/p-book-6', methods=['GET', 'POST'])
def principito_6():
    el_principito_book_speech_6 = el_principito_book_6  # Pass the text content directly

    return render_template('principito6.html',
                           el_principito_book_speech_6=el_principito_book_speech_6,
                           date=datetime.now().strftime("%a %d %B %Y"))


@app.route('/p-book-7', methods=['GET', 'POST'])
def principito():
    el_principito_book_speech_7 = el_principito_book_7  # Pass the text content directly

    return render_template('principito7.html',
                           el_principito_book_speech_7=el_principito_book_speech_7,
                           date=datetime.now().strftime("%a %d %B %Y"))


@app.route('/stella-audio-book', methods=['GET', 'POST'])
def stella_():
    stella_book_speech = stella_book

    return render_template('stella-book.html',
                           stella_book_speech=stella_book_speech,
                           date=datetime.now().strftime("%a %d %B %Y"))


@app.route('/les-m-book', methods=['GET', 'POST'])
def miserables():
    les_miserables_book_speech = les_miserables_book

    return render_template('les-m-book.html',
                           les_miserables_book_speech=les_miserables_book_speech,
                           date=datetime.now().strftime("%a %d %B %Y"))


@app.route('/synthesize/<lang>/<text>')
def synthesize(lang, text):
    speech_buffer = generate_speech(text, lang=lang)
    if speech_buffer:
        response = Response(speech_buffer, content_type='audio/mpeg')
        response.headers['Content-Length'] = len(speech_buffer.getvalue())
        return Response(speech_buffer, content_type='audio/mpeg')
    return "Error synthesizing speech with gTTS"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
