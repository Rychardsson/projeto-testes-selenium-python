from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    """Página inicial com link para o formulário."""
    return render_template('index.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    """Página que exibe e processa o formulário."""
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')

        # Validação simples: verifica se os campos não estão vazios
        if not nome:
            return render_template('formulario.html', erro='O campo nome é obrigatório.')
        if not email:
            return render_template('formulario.html', erro='O campo email é obrigatório.')
        
        # Se tudo estiver OK, redireciona para a página de sucesso
        return redirect(url_for('sucesso'))

    return render_template('formulario.html', erro=None)

@app.route('/sucesso')
def sucesso():
    """Página exibida após o envio bem-sucedido do formulário."""
    return render_template('sucesso.html')

if __name__ == '__main__':
    # Roda a aplicação em modo de debug
    app.run(debug=True, port=5001)