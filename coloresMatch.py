from difflib import Match


color=input("digite codigo de color: ")

match color:
    case 'FF0000':
        print('🔴')
        
    case '00FF00':
        print('🟢')
        
    case '0000FF':
        print('🔵')
        
    case _:
        print('unknow color')
        
        #'#AF549B'