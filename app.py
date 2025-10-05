from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui_mude_isso'  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/galeria')
def galeria():
    
    imagens = [
        {'url': 'https://via.placeholder.com/400x400.png?text=Corte+1', 'alt': 'Corte degradê moderno'},
        {'url': 'https://via.placeholder.com/400x400.png?text=Corte+2', 'alt': 'Corte social elegante'},
        {'url': 'https://via.placeholder.com/400x400.png?text=Corte+3', 'alt': 'Barba estilizada'},
        {'url': 'https://via.placeholder.com/400x400.png?text=Corte+4', 'alt': 'Corte fade premium'},
        {'url': 'https://via.placeholder.com/400x400.png?text=Corte+5', 'alt': 'Corte undercut'},
        {'url': 'https://via.placeholder.com/400x400.png?text=Corte+6', 'alt': 'Barba e bigode'},
    ]
    return render_template('galeria.html', imagens=imagens)

@app.route('/sobre')
def sobre():
    # Informações do barbeiro
    info = {
        'nome': 'Gustavo (Guh)',
        'experiencia': 'Iniciante com muita dedicação',
        'especialidade': 'Cortes modernos e degradês',
        'missao': 'Transformar o visual dos clientes com técnica e estilo único'
    }
    return render_template('sobre.html', info=info)

@app.route('/servicos')
def servicos():
    # Lista de serviços oferecidos
    lista_servicos = [
        {'nome': 'Corte Tradicional', 'preco': 40.00, 'duracao': '30min'},
        {'nome': 'Corte + Barba', 'preco': 65.00, 'duracao': '50min'},
        {'nome': 'Barba Completa', 'preco': 30.00, 'duracao': '25min'},
        {'nome': 'Degradê', 'preco': 45.00, 'duracao': '35min'},
        {'nome': 'Pigmentação', 'preco': 50.00, 'duracao': '40min'},
        {'nome': 'Corte Infantil', 'preco': 30.00, 'duracao': '25min'},
    ]
    return render_template('servicos.html', servicos=lista_servicos)

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        # Receber dados do formulário
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        telefone = request.form.get('telefone', '').strip()
        mensagem = request.form.get('mensagem', '').strip()

        # Validação básica
        if not nome or not email or not mensagem:
            flash('Por favor, preencha todos os campos obrigatórios.', 'error')
            return redirect(url_for('contato'))

        if len(nome) < 3:
            flash('Nome deve ter pelo menos 3 caracteres.', 'error')
            return redirect(url_for('contato'))

        if '@' not in email or '.' not in email:
            flash('Por favor, insira um e-mail válido.', 'error')
            return redirect(url_for('contato'))

        # Log da mensagem (em produção, salve em banco de dados ou envie por email)
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        print(f"\n{'='*50}")
        print(f"NOVA MENSAGEM RECEBIDA - {timestamp}")
        print(f"{'='*50}")
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"Telefone: {telefone if telefone else 'Não informado'}")
        print(f"Mensagem: {mensagem}")
        print(f"{'='*50}\n")

        # Aqui você pode adicionar:
        # - Salvar no banco de dados
        # - Enviar email de notificação
        # - Integrar com CRM
        
        flash('Mensagem enviada com sucesso! Entraremos em contato em breve.', 'success')
        return redirect(url_for('contato')) 

    return render_template('contato.html')

# Tratamento de erro 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Contexto global para templates
@app.context_processor
def inject_globals():
    return {
        'ano_atual': datetime.now().year,
        'whatsapp': '5521971585158',
        'instagram': '@gustavomiguelofc',  
        'endereco': 'São Paulo, SP'  
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)