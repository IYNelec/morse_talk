# morse_talk ゆっくりホレトーク

IchigoJam BASIC Applications

Contents

1. About this app
2. Example
   1. photo image
   2. source code
3. TODO
4. References

## 1. About this app

　このアプリケーションは、電鍵で入力した和文モールス信号をカナ文字として一文字ずつ解釈し、音声として出力するものです。遊戯用途以外での動作保証はありません。またモールス信号の厳密な取り決めに準拠してはおりません。

　このアプリケーションは以下のような構成で動作します。

* MPU : IchigoJam BASIC ver1.4 以降が動作するもの
* Talk IC : Aques Talk
* Audio : Amp & Speaker

## 2. Example

### 2.1 photo image

<img src=./img/IMG_20220509_150147.jpg width=50%>

これは「福生 de はむハムフェア」において展示を行ったときに作成した構成例の写真です。液晶モニタはコンポジット出力のものは使用しませんでした。

### 2.2 source codes

　src フォルダに IchigoJam BASIC 言語で書かれたソースコードがあります。FILE0_INIT.BAS、FILE1_MAIN.BAS をそれぞれ入力し、FILE 0, FILE 1 に SAVE コマンドによって保存してください。

　実行は IchigoJam の電源を入れなおすか LRUN0 コマンドです

　IchigoJam BASIC のソースコードは一般的な Windows パソコンで表示するとカナ文字が化けてしまいますが、IJUtilities などの IchigoJam 専用ターミナルソフトで開くことによって正確に表示することができます。画像でソースコードを表示した場合の例を img/FILE0_INIT.jpg, FILE1_MAIN.jpg に示します

## 3. TODO

　修正・改善の予定はありませんが、お問い合わせは github を通じてお願いします。

* readme.md の改善
* このアプリケーションの詳細について頒布予定の薄い本を執筆中
* 一緒に遊びたい人の募集

## 4. References

　作成の参考になる参照文献です

* IchigoJam 全般 : [https://ichigojam.net/](https://ichigojam.net/)
* IchigoJam プログラミング技術 : [https://fukuno.jig.jp/IchigoJam](https://fukuno.jig.jp/IchigoJam)
* AquesTalk 音声合成IC : [https://www.a-quest.com/products/aquestalk.html](https://www.a-quest.com/products/aquestalk.html)
* 電子部品入手先 : [https://akizukidenshi.com/catalog/](https://akizukidenshi.com/catalog/)
