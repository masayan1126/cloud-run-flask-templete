# Pythonのベースイメージを指定
FROM python:3.11

ENV PORT 8080

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN pip install flask gunicorn requests

# アプリケーションのソースコードをコピー
COPY . /app

# gunicornを使用してアプリケーションを実行
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app