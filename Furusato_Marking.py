#-------------------------------------
#
#  ふるさとコンテストのニューマルチのマーキング ツール
#
#   作成年月日：2018/09/23
#   バージョン：v0r2
#   作成者：　田中盛一　JI1FLB
#
#   動作概要
#       　form.txtに記述されるコールサインを取得し、
#       コールサイン.txtファイルをオープンする。
#       　その後に、ふるさとコンテストの規約で規定される
#       ニューマルチに印を付ける。
#       　マーキングされたコンテストログは、
#       コールサイン_marking.txtとして出力される
#
#
#   使用方法
#       １） ツールのフォルダに、コンテストログファイル Callsign.txt
#           form.txtが存在することを確認
#       ２）　Furusato_Marking.pyを起動する。
#               ※：python3.7がインストールされていることが必須
#
#


import os
import shutil

fill_in_form = open( "form.txt" ,"r", encoding='utf-8')


#------------------------------------------------------------------------
#
#   コールサイン取得
#   サマリーシート作成
#
   

fill_in = fill_in_form.readlines()

for fill in fill_in :
    fill = fill.rstrip('\n')
    fill = fill.strip()
    fill = fill.split(":")
    if "コールサイン"==fill[0] :
        Callsign = fill[1]
        Callsign = Callsign.lstrip().rstrip()
        break
        
shutil.copy( Callsign + ".txt",  Callsign + "_bak.txt" ) 
logs = open( Callsign + ".txt", 'r', encoding='utf-8')
new_file = open( Callsign + '_marking.txt', 'w', encoding='utf-8' )

#-------------------------------------
#
#  ふるさとコンテストのニューマルチのマーキング
#
#
#


log = logs.readlines()

i=0
okng = True
hit = False
Multi = set()

for row in log :
    
    if  "</LOGSHEET>" in row :
#        print(row)
        hit = False
        
    if hit == False :
        new_file.write(row)
    
    if hit == True :
        row = row.split()        
        if row[2] + row[8] in Multi :
            print( row[0]+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5]+" "+row[6]+" "+row[7]+" "+row[8] )
            new_file.write( row[0]+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5]+" "+row[6]+" "+row[7]+" "+row[8]  +"\n" )
#            print("dup")
        else :
            print( row[0]+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5]+" "+row[6]+" "+row[7]+" "+row[8]+"*" )
            new_file.write( row[0]+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5]+" "+row[6]+" "+row[7]+" "+row[8]+"*"  +"\n" )
#            print("Now Multi")
            
        Multi.add(row[2] + row[8])

    if  "<LOGSHEET" in row :
        hit = True
        
print( "\n" )
print("*** マルチリスト　  凡例）バンド＋マルチ名" )
print( Multi )

logs.close()
new_file.close()
fill_in_form.close()
