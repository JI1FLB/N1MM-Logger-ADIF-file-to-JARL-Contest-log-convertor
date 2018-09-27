#--------------------------------------------------------
#
#   ADIFファイル　正常性確認ルーチン
#
#	作成年月日：18/09/27 9:46:16
#
#   概要
#       　ADIFファイルを出力すると、コンテスト中にログを
#       強制入力した場合に、Forced QSOとコメントに入力される。
#       この場合には、マルチが正しく入力されていなを生じる。
#       　このルーチンは、Forced QSOを検出するものである。
#
#
#   使い方
#       1)  form.txt, xxxxxx.adiファイルをフォルダに入れる
#       　注意：form.txtのコールサインとxxxxxx.adiファイルの
#           xxxxxxが同じであること
#
#       2)  このルーチンをダブルクリックし、起動する。
#
#       3)  エラーがAdif_file_error.txtに出力される
#
#


#--------------------------------------------------------

import os


#------------------------------------------
#
#   変数宣言
#
#


l=""

log = ""

a = ""
b = ""
c = ""

BAND = ""
Contest_name = ""

filename = ""

cnt = 0
Ln = 0

log_error_flag = False


#--------------------------------------------------------

fill_in_form = open( "form.txt" ,"r", encoding='utf-8')

fill_in = fill_in_form.readlines()

for fill in fill_in :
    fill = fill.rstrip('\n')
    fill = fill.strip()
    fill = fill.split(":")
    if "コールサイン"==fill[0] :
        Callsign = fill[1]
        Callsign = Callsign.lstrip().rstrip()
        break

filename = Callsign + '.adi'

adif_log = open( filename ,'r',encoding='utf-8')
output_log = open( 'Adif_file_error.txt' ,'w',encoding='utf-8')


#--------------------------------------
#
#
#

logs = adif_log.readlines()

for log in logs:

    log = log.replace(' "','')
    log = log.rstrip('\n')
    log = log.rstrip()
    log = log.lstrip()
    log = log.split("<")

    Ln = Ln + 1


#--------------------------------------
#

    for i in log:    
        if "COMMENT:" in i:
            a = i
            b = a[8:10]
            b1= b.rstrip(">")
            b2 = len(b1)
            COMMENT = a[9+b2:10+b2+int(b1)]
            COMMENT = COMMENT.rstrip()
            COMMENT = COMMENT.upper()
            print ( 'COMMENT-> ' + COMMENT )

            if 'FORCED QSO' == COMMENT :
                log_error_flag = True
                break

    if log_error_flag == True :
        print( '*** Error ****    in  Ln: ' + str( Ln ) )
        output_log.write( '*** Error ****    in  Ln: ' + str( Ln ) + '\n' )
        log_error_flag = False


output_log.close()





        
              
