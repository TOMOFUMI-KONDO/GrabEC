# GrabEC

## 構成
- backend (Flask)
- requirements.txt (pipのパッケージ一覧)
- frontend (Vue)
- dist (公開ファイル)
- manage.py (サーバー起動)

## 最初にすること
- ルート直下で "pip install -r requirements.txt" (pipのパッケージがインストールされる)
- frontend直下で "npm install" (npmのパッケージがインストールされる)

## その他使うコマンド
- ルート直下で "python manage.py" (バックエンドのコード書くとき、ローカルサーバー立てる)
- frontend直下で "npm run serve" (フロントエンドのコード書くとき、ローカルサーバー立てる。backendのAPIを使うときには、別途Flaskのサーバーを立てる。)
- frontend直下で "npm run build" (ルート直下のdistファイルにbuildする。バックエンドのサーバーはこのdist配下のファイルを使うため、pythonで立てたサーバーから見たフロントエンドのコードを更新する時はbuildする必要がある。)