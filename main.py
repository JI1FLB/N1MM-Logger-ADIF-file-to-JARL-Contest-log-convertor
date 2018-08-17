#import subprocess as sb
from Phase0 import phase0
from Phase1 import phase1
from Phase2 import phase2
from Phase3 import phase3


#--------------------
Callsign = ""
FD_coe = 1
okng = True
Ph0_data = []


#----------------------------------------------------------------------------------
print("+-------------------------------------------------------------------------+")
print("|                                                                         |")
print("|                                                                         |")
print("|  N1MM logger+ ADIFファイルからJARLコンテストログ仕様ver2.0変換ツール    |")
print("|                                                                         |")
print("|                        v.01.rev00                                       |")
print("|                                                                         |")
print("|            2018/08/16 Copyright JI1FLB Seiichi Tanaka                   |")
print("|                                                                         |")
print("|   仕様                                                                  |")
print("|    1.入力条件                                                           |")
print("|       form.txtにコンテストに関する参加条件を記入したものを用意          |")
print("|       NtMM Logger+ でADIFファイルをExport　                             |")
print("|          ※ ファイル名は自分のコールサイン.adi                          |")
print("|       ソフトウェアの入力ガイダンスに合わせて、必要情報を入力            |")
print("|                                                                         |")
print("|                                                                         |")
print("|    2.出力ファイル 　                                                    |")
print("|       2.1　JARLコンテスト委員会仕様のVer2.0ファイル　                   |")
print("|       2.2　ハムログ用のＣＳＶファイル                                   |")
print("|       2.3　コンテストスコアーンファイル 　　　　　                      |")
print("|       2.4　ログシート部分のファイル                                     |")
print("|       2.5　ADIFファイルを成型したADIFファイル                           |")
print("|       2.6　CalcファイルでADIFファイルを見るためのファイル               |")
print("|                                                                         |")
print("|                                                                         |")
print("|     3. 注意事項                                                         |")
print("|        3.1　2018FDコンテストはこのファイルを使って提出                  |")
print("|        3.2　ハムログへのデータ結合は未実施                              |")
print("|                                                                         |")
print("+-------------------------------------------------------------------------+")
print("+-------------------------------------------------------------------------+")
#------------------------------------------

#Phase0を起動
Ph0_data = phase0()

#print(Ph0_data)
#print(Ph0_data[0])
FD_coe = int(Ph0_data[0])
#print(Ph0_data[1])
Callsign = Ph0_data[1]

print("*** Completed the phase0 process"+"\n")


#Phase1を起動
phase1( Callsign )
print("*** Completed the phase1 process"+"\n")


#Phase2を起動
phase2( Callsign,FD_coe )
print("*** Completed the phase2 process"+"\n")


#Phase3を起動
phase3(Callsign)
print("*** Completed the phase3 process"+"\n")
