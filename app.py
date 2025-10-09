from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'barber_secret_key'  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/galeria')
def galeria():
    imagens = [
        {'url': url_for('static', filename='img/FOTO1.jpg'), 'alt': 'Foto de um corte de cabelo'},
        {'url': url_for('static', filename='img/FOTO2.jpg'), 'alt': 'Foto de um corte de cabelo'},
        {'url': url_for('static', filename='img/FOTO3.jpg'), 'alt': 'Foto de uma barba estilizada'},
        {'url': url_for('static', filename='img/FOTO7.jpg'), 'alt': 'Foto de um corte de cabelo'},
        {'url': url_for('static', filename='img/FOTO9.jpg'), 'alt': 'Foto de um corte de cabelo'},
        {'url': url_for('static', filename='img/FOTO11.jpg'), 'alt': 'Foto de um corte de cabelo'},
        {'url': url_for('static', filename='img/FOTO5.jpg'), 'alt': 'Foto de um corte de cabelo'},
        {'url': url_for('static', filename='img/FOTO4.jpg'), 'alt': 'Foto de um corte de cabelo'},
        {'url': url_for('static', filename='img/FOTO13.jpg'), 'alt': 'Foto de um corte de cabelo'},
    ]
    return render_template('galeria.html', imagens=imagens)

@app.route('/sobre')
def sobre():
    info = {
        'nome': 'Gustavo',
        'apelido': 'GM',
        'idade': 21,
        'local': 'zona sul de São Paulo',
        'tempo_experiencia': '7 meses',
        'missao': 'Acredito que um bom corte vai além da técnica é sobre conexão, atenção aos detalhes e fazer o cliente se sentir especial. Por isso, cada atendimento é único e personalizado.'
    }
    return render_template('sobre.html', info=info)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.context_processor
def inject_globals():
    return {
        'ano_atual': datetime.now().year,
        'whatsapp': '5521971585158',
        'instagram': '@gustavomiguelofc',
        'endereco': 'São Paulo, SP'  
    }

if __name__ == '__main__':
    app.run(debug=True)