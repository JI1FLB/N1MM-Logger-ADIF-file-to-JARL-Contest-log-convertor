
    #--------------------------------------------------------
    #   
    #   コンテスト名抽出ルーチン
    #
    #


def phase0_1( a:str ):
    
    import os
    
    log = ""
    filename = ""

    c = 0

    Contest_name = ""
    
    Callsign = a

    filename = Callsign + ".adi"

 #--------------------------------------

    output_log = open( Callsign + ".adi" ,'r',encoding='utf-8')


#--------------------------------------

    logs = output_log.readlines()

    for log in logs:
            
        log = log.replace(' "','')
        log = log.rstrip('\n')
        log = log.rstrip()
        log = log.lstrip()
        log = log.split()

        c = c + 1

        for i in log:
                
            if 'Contest' in i:
                Contest_name = log[2]

        if c == 4 :
            break

#    print('*****************************')
#    print( Contest_name )
#    print('*****************************')

    output_log.close()


    return Contest_name

