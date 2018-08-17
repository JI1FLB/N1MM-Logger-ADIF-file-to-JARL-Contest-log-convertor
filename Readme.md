18/08/17 10:58:28

N1MM-adif-JARLcontestLog-convertor

JI1FLB/ Seiichi Tanaka

1.はじめに

このツールは、N1MM Logger+で国内コンテストに参加した場合、JARLコンテスト委員会が指定するサマリー、ログ仕様Ver2.0に変換する必要がある。JARLもN1MM Logger+を利用した場合には、N1MM Logger+の時刻をずらして運用することと、Web上のログ作成ツールでCarlbroファイルで、ログを提出すること進めている。
このツールは、コンテスト終了後、簡単に提出ログを作成することができるものです。


２．目的

このツールは、N1MM Logger+で国内コンテストに参加した場合、JARL仕様でコンテスト主催者にログを迅速に提出可能とするものです。


３．使い方

3.1　python3.62をインストール


3.2　作業用のフォルダを作成。


3.2　Githubからダウンロードした3.2項のフォルダに保存。


3.3　N1MM Logger+でADIFファイルを3.2項のフォルダに保存。


3.4　form.txtに必要事項を記入し、3.2項のフォルダに保存。


3.5　main.pyを起動する。起動後は、ガイダンスに従い、必要事項を選択、入力する。




4．免責

このツール仕様にあたっては、自己責任でご利用ください。


5．ライセンス

GNU GENERAL PUBLIC LICENSEに従うフリーウェアです。


6．最後に

このツールは、初めてpythonを使って作ったもの、オブジェクト指向の知識、pythonの知識があれば、よりスマートなものが作れたと思います。今後も、よりスマートなツール作れるように努力してゆきたいと考えています。
加えて、今回のツールは、思いつくままに作っていったので、モジュール化も全くできていません。
