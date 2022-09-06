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


# DBバックアップバッチ（backup_diary）

## 1. VScode実行構成設定

##### 1-1. ` Ctrl + shift + p ` で、コマンドパレットを開く

##### 1-2. コマンドパレットに ` launch `と入力し、launch.jsonを開く

<img width="657" alt="image" src="https://user-images.githubusercontent.com/91407264/188609082-4979dd10-5ead-4172-bb2c-0482a6bea2c1.png">

##### 1-3. ` 構成の追加 `を選択


##### 1-4. ` python ` を選択

<img width="478" alt="image" src="https://user-images.githubusercontent.com/91407264/188609538-f0250865-953d-4ced-8305-5bd2206ba210.png">

##### 1-5. ` Django ` を選択

<img width="668" alt="image" src="https://user-images.githubusercontent.com/91407264/188609723-0e52e67c-d831-40cf-b99a-bafee59582cc.png">

##### 1-6. manage.py のパスを入力

<img width="660" alt="image" src="https://user-images.githubusercontent.com/91407264/188610050-7c20053f-35f7-4bb2-a103-f70917e54327.png">


##### 1-7. 開いた launch.json の"configurations" に以下の実行構成を追加  ※カンマのうち忘れに注意。
	
	"configurations": [
		：（省略）
	       {
		    "name": "backup_diary",
		    "type": "python",
		    "request": "launch",
		    "program": "${workspaceFolder}/private_diary/manage.py",
		    "args": [
			"backup_diary"
		    ],
		    "django": true,
		    "justMyCode": true,
		    "env": {
			"DB_USER": "postgres",
			"DB_PASSWORD": "password",
			"DJANGO_SETTINGS_MODULE": "private_diary.settings_dev",
		    }
		},
	    ]
	    


## 2. バッチの手動実行（開発環境）

##### 2-1. VSCodeの左下にある実行/デバッグの構成を示す表示をクリック

<img width="375" alt="image" src="https://user-images.githubusercontent.com/91407264/188626471-61abeeff-ff10-4588-ac9b-f42e2265fc62.png">

##### 2-2. ` backup_diary `　を選択し、バッチを実行

<img width="640" alt="image" src="https://user-images.githubusercontent.com/91407264/188626751-0071919f-6383-4f8d-b37e-d8d1842da6f5.png">

→実行後はワークスペースフォルダの　backupフォルダにcsv形式で出力されます。

<img width="347" alt="image" src="https://user-images.githubusercontent.com/91407264/188627821-7815a574-cdb3-44a7-a0b2-94f11a955a75.png">

## ■バックアップファイルの保存先および保存ファイル数の設定
` private_diary/private_diary/settings_common.py `　のBACKUP_PATH、NUM_SAVED_BACKUPにて以下のように設定。

<img width="269" alt="image" src="https://user-images.githubusercontent.com/91407264/188628205-3202076b-0149-49b7-8e76-17cc7c4b3a2b.png">
