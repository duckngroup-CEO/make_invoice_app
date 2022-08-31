from flask import Flask,render_template
import config

# 環境変数一覧
# print(config.IMAGE_PATH)
# print(config.ORIGINAL_FILES_PATH)
# print(config.OUTPUT_FILES_PATH)
# print(config.INVOICE_TEMPLATES_PATH)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


# メイン関数
if __name__ == "__main__":
    app.run()