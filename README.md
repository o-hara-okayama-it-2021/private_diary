# private_diary
クラウドネイティブ開発（Django）授業サンプルPG

## テストコードの実行方法
以下の手順で、ターミナル（コマンドプロンプト）より実行する。

#### 1. VSCodeで開発サーバー(runserver)を起動

#### 2. 別のターミナルを開き、仮想環境を活性化（Activate）

#### 3. （初回のみ実行）以下のコマンドで、Seleniumをインストール
※バージョンが異なると動かなくなるので注意

	pip install selenium==4.1.0

#### 4. 以下のコマンドで、データベースのユーザ／パスワードを環境変数（一時的）にセット

	set DB_USER=postgres
	set DB_PASSWORD=password

#### 5. 「manage.py」のあるディレクトリに移動
	
#### 6. 以下のコマンドで、テストコードを実行

	python manage.py test --settings private_diary.settings_dev
	
	
