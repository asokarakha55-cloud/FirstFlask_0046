from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil_nama = None
    hasil_pesan = None
    is_submitted = False

    if request.method == 'POST':
        hasil_nama = request.form.get('nama', '').strip()
        hasil_pesan = request.form.get('pesan', '').strip()
        is_submitted = True

    return render_template(
        'index.html',
        nama=hasil_nama,
        pesan=hasil_pesan,
        is_submitted=is_submitted
    )

if __name__ == '__main__':
    app.run(debug=True)