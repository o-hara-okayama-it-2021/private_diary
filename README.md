# private_diary
クラウドネイティブ開発（Django）授業サンプルPG


# ユニットテスト
## 1. VSCode実行構成設定（初回のみ実行）
##### 1-1. ` Ctrl + shift + p ` で、コマンドパレットを開く

##### 1-2. コマンドパレットに ` python test `と入力

##### 1-3. ` Python:テストを構成する `を選択

<img width="644" alt="image" src="https://user-images.githubusercontent.com/91407264/188579718-2764e55d-33de-4c27-8953-ec85e4e84137.png">

##### 1-4. 仮想環境フォルダを選択

<img width="654" alt="image" src="https://user-images.githubusercontent.com/91407264/188580068-a86dfb1e-f5dd-4feb-a095-708e058d1006.png">

##### 1-5. ` unittest ` を選択

<img width="643" alt="image" src="https://user-images.githubusercontent.com/91407264/188580493-aa502c2a-ea2d-4256-953b-5a9c0d46028b.png">

##### 1-6. ` private_diary ` を選択

<img width="629" alt="image" src="https://user-images.githubusercontent.com/91407264/188581046-d4b37c35-6f05-42ea-a708-28389a275f29.png">

##### 1-7. ` test_*.py ` を選択

<img width="659" alt="image" src="https://user-images.githubusercontent.com/91407264/188581172-8e69fa70-d45f-4de8-bfa2-111582736322.png">


##### 1-8. VSCodeのエクスプローラからsettings.jsonを開く

<img width="411" alt="image" src="https://user-images.githubusercontent.com/91407264/188582046-f738bff9-6f63-4e2f-9940-b8f57515841b.png">

##### 1-9. settings.jsonが、以下のような設定となっていることを確認
	
	{
	    "python.testing.unittestArgs": [
		"-v",
		"-s",
		"./private_diary",
		"-p",
		"test_*.py"
	    ],
	    "python.testing.pytestEnabled": false,
	    "python.testing.unittestEnabled": true,
	    "python.testing.pytestArgs": [
		"private_diary"
	    ]
	}

##### 1-10. 活性化（Activate）した仮想環境にて、Seleniumをインストール

	pip install selenium==4.1.0


## 2. テストコードの実行方法
以下の手順で、ターミナル（コマンドプロンプト）より実行する。

#### 2-1. VSCodeで開発サーバー(runserver)を起動

#### 2-2. 別のターミナルを開き、仮想環境を活性化（Activate）

#### 2-3. 以下のコマンドで、データベースのユーザ／パスワードを環境変数（一時的）にセット

	set DB_USER=postgres
	set DB_PASSWORD=password

#### 2-4. 「manage.py」のあるディレクトリに移動
	
#### 2-5. 以下のコマンドで、テストコードを実行

	python manage.py test --settings private_diary.settings_dev
	
	
