def phase0():


#------------------------------
#
#   JARLサマリーシート作成
#
#   仕様：記入フォームから、summaryフォーマットに変換


    import os

    fill_in_form = open( "form.txt" ,"r", encoding='utf-8')

    Callsign =""
    GestOP_Callsign =""
    GestOP_flag = "N"
    Multi_OP_flag = "N"
    FD_flag ="N"
    yesno = "N"
    okng = True
    FD_coe = 1
    Ph0 = []


#----------------------------------------------------------------------
    print("\n")
    print("***　サマリーシート必要事項選択")
    print("\n")
    
#------------------------------------------------------------------------
#
#   ゲストオペ（コールサイン）の入力
#
#

    while okng :
        print('\n')
        print('ゲストオペ運用ですか？。')
        yesno = input("[Y or N] >> ")
        if yesno == "Y":
            okng = False
        
            print('ゲストオペレータのコールサインを入力してください。')
            GestOP_Callsign = input('>> ').upper()
            print('入力したコールサイン --> ' + GestOP_Callsign )
            print('このコールサインで良いですか? [Y or N]')
            yesno = input("[Y or N] >> ")
        
            if yesno == "Y":
                okng = False
                GestOP_flag = "Y"
            else:
                okng = True
        else:
            okng = False
            GestOP_flag = "N"


#------------------------------------------------------------------------
#
#   フィールドデーコンテストの入力
#
#

    print('\n')

    okng = True
    while okng :
        print('FDコンテストですか？')
        yesno = input("[Y or N] >> ")
        if yesno == "Y":
            FD_flag ="Y"
            FD_coe = 2
            Ph0.append(str(FD_coe))
            okng = False

        elif yesno == "N":
            FD_flag ="N"
            FD_coe = 1
            Ph0.append(str(FD_coe))
            okng = False
            
        else:
           okng = True
        
#------------------------------------------------------------------------
#
#   マルチオペの入力
#
#

    print('\n')
        
    okng = True
    while okng :
        print('マルチオペ運用ですか？')
        yesno = input("[Y or N] >> ")
        if yesno == "Y":
            Multi_OP_flag = "Y"        
            okng = False
        elif yesno == "N":
            Multi_OP_flag = "N"       
            okng = False
        else:
            okng = True

    print('\n')

    fill_in = fill_in_form.readlines()

    for fill in fill_in :
        fill = fill.rstrip('\n')
        fill = fill.strip()
        fill = fill.split(":")
        if "コールサイン"==fill[0] :
            Callsign = fill[1]
            Callsign = Callsign.lstrip().rstrip()
            Ph0.append(Callsign)
            break

    summary = open( Callsign + "_summary.txt" ,"w" , encoding='utf-8')

    summary.write( "<SUMMARYSHEET VERSION=R2.0>" + "\n")

    fill_in_form.seek(0)

    for fill in fill_in :
        fill = fill.rstrip('\n')
        fill = fill.strip()
        fill = fill.split(":")
    
        if "コンテストの名称" == fill[0] :
            summary.write( "<CONTESTNAME>" + fill[1]+ "</CONTESTNAME>" + "\n" )
    
        if "参加部門種目コードナンバー" == fill[0] :
            summary.write( "<CATEGORYCODE>" + fill[1] + "</CATEGORYCODE>"  + "\n")

        if "コールサイン" == fill[0] :
            summary.write( "<CALLSIGN>" + fill[1] + "</CALLSIGN>"  + "\n")


        if "ゲストオペ運用者のコールサイン" == fill[0] and GestOP_flag == "Y":
            summary.write( "<CALLSIGN>" + GestOP_Callsign + "</CALLSIGN>"  + "\n")
        
        if "連絡先住所" == fill[0] :
            summary.write( "<ADDRESS>" + fill[1] + "</ADDRESS>"  + "\n")

            summary.write( "<TOTALSCORE></TOTALSCORE>" + "\n")
        
        if "氏名(クラブ局の名称)" == fill[0] :
            summary.write( "<NAME>" + fill[1] + "</NAME>"  + "\n")
        
        if "電話番号" == fill[0] :
            summary.write( "<TEL>" + fill[1] + "</TEL>"  + "\n")
        
        if "E-mailアドレス" == fill[0] :
            summary.write( "<EMAIL>" + fill[1] + "</EMAIL>"  + "\n")

        if "コンテスト中使用した最大空中線電力(W)" == fill[0] :
            summary.write( "<POWER>" + fill[1] + "</POWER>"  + "\n")

        if "フィールドデーコンテストの場合の局種係数" == fill[0] and FD_flag == "Y" :
            summary.write( "<FDCOEFF>" + fill[1] + "</FDCOEFF>"  + "\n")        

        if "運用地" == fill[0] and FD_flag == "Y"  :
            summary.write( "<OPPLACE>" + fill[1] + "</OPPLACE>"  + "\n")

        if "使用電源" == fill[0] and FD_flag == "Y"  :
            summary.write( "<POWERSUPPLY>" + fill[1] + "</POWERSUPPLY>"  + "\n")

        if "意見" == fill[0] :
            summary.write( "<COMMENTS>" + fill[1] + "</COMMENTS>"  + "\n")

#    if "マルチオペ種目運用者のコールサインまたは氏名" == fill[0] and Multi_OP_flag == "Y" :
        if Multi_OP_flag == "Y" :
            summary.write( "<MULTIOPLIST>" + fill[1] + "</MULTIOPLIST>"  + "\n")

        if "登録クラブ番号" == fill[0] :
            summary.write( "<REGCLUBNUMBER>" + fill[1] + "</REGCLUBNUMBER>"  + "\n")        

        if "宣誓文" == fill[0] :
            summary.write( "<OATH>" + fill[1] + "</OATH>"  + "\n")
        
        if "日付" == fill[0] :
            summary.write( "<DATE>" + fill[1] + "</DATE>"  + "\n")
        
        if "署名" == fill[0] :
            summary.write( "<SIGNATURE>" + fill[1] + "</SIGNATURE>"  + "\n")

        
    summary.write( "</SUMMARYSHEET>"+"\n")        
    fill_in_form.close()
    summary.close()
    
   
    
    return Ph0
