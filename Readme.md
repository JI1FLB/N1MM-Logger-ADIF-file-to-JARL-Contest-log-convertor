　　　　　　　　　　　　　　　　　　　　　　　　　　　　　18/08/17 10:58:28

　　　　　　　N1MM Logger+ adifファイル-JARLcontestLog-コンバータについて

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



7.変更履歴

2018-08-20

*UTC　JST変換で時間の変換が正常に行われない。

->時分に変更することで解消

*タイム表示が時分であるところ、時分秒と表示していた。

->時分と表示するように時分秒の文字列から、秒を削除

*ハムログCSVファイルにRST情報が欠落しているBugを修正


2018-08-21

入力ガイダンス時に判断処理を強化


2018-09-27

プログラム構造の見直し。ADIFファイルからコンテスト名を抽出。サマリーシートのマルチ数カウント方法の見直し。NTTコンテストのマルチ数をカウント可能とする。


2018-09-27
Birthdayコンテストのマルチ計算対応



8.既知の不具合について

2019/09/24

SCC-RTTYコンテストのADIファイルをこのツールにかけると、エラーを生じる。

-> 原因は、N1MM Logger+が生成するADIファイルの情報要素の並びが異なる。

->  ワークアラウンドはコンテスト主催者にCarlbroファイルで提出可能。プログラム構造を見直して、Bug Fixed。


2019/09/24

WPX,WAEコンテストのシリアル番号が表示できない。得点計算ができない。

※：ハムログ用のCSVファイルは生成可能


-> ワークアラウンドはコンテスト主催者にCarlbroファイルで提出可能。現在、プログラム構造の抜本的な見直して、シリアル番号をログに記載することを検討中。但し、得点計算はプログラム規模が大きくなるために対処するか不明。

