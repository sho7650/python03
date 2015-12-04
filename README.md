# python code school (examples)

ほとんどの人には役に立たない、django on Python on Bluemix で SoftLayer の APIを Kickしてみるテストです

# 使い方

試し切れていないので、できないケースがあればご連絡ください

## ソースコードの入手

次のコマンドでローカルへ

`git clone https://github.com/sho7650/python03.git`

gitが使えない場合は、https://github.com/sho7650/python03/archive/master.zip をダウンロードしてください

## DB を作成しよう

./python3 ディレクトリで、次のとおり

`./manage.py makemigrations`

`./manage.py migrate`

これで DB が作成できます。標準だと、sqlite3 ですので、特にDBを意識する必要はないでしょう。

## ユーザをつくろう

"/admin" で操作、および、当アプリを操作するためにユーザを作りましょう

`./manage.py createsuperuser`

後は質問に答えておきます。このユーザで、"/admin" へアクセスします

## ローカルで起動してみよう

このとおり実行すると、http://localhost:8000/ でアクセスできるようになります

`./manage.py runserver`

## データをつくろう

http://localhost:8000/admin へアクセスすると、Django管理画面になります。先ほど作成したユーザでログインします。

### Django 管理サイトでSoftlayer APIを登録する

モデル定義に失敗していなければ、"Soflayer_apis" があるはずです。「追加」をしましょう。

「username」「api key」「endpoint url」の入力項目があります。SoftLayerユーザの username と apikey を入力します。endpoint には https://api.softlayer.com/xmlrpc/v3 を入れておきます(今はまだ使っていません)

一つ目から自動的に ID = 1 が割り振られます。

### Django 管理サイトでユーザとAPIを連携する

Django 管理サイトから「ユーザー」へアクセスします。これまでに作成したユーザーの一覧がでてきます。先ほどのAPIと連携したいユーザーをクリックします。

ユーザ項目一覧の一番下に「Softlayer id:」という部分があります。ここで、先ほど作成したAPIのIDを入力します。一つ目であれば「1」となります。2つ目以降は順番に2,3,...と増えていきます。

# ログインしてみよう

後は http://localhost:8000/login/ へアクセスして試してみましょう
