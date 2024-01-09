import os
from flask import Flask
from flask import jsonify
import requests

app = Flask(__name__)


@app.route("/")
def todos():
    # jsonplacefolderからデータを取得
    response = requests.get("https://jsonplaceholder.typicode.com/todos")

    # json形式に変換
    todos = response.json()

    # レスポンスを返す
    return jsonify(data=todos, success=True), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
