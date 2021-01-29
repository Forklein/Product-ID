import time
import sys

variant_1 = "00000001"
variant_2 = "00000002"
variant_3 = "00000004"
variant_4 = "00000005"
variant_5 = "00000006"
variant_6 = "00000007"
variant_7 = "00000008"
variant_8 = "000000010"
variant_9 = "000000011"

gang = True
while gang == True:
     try:
         pid = int(input('Inserisci il pid: '))
         answer = input('Vuoi visualizzare i load?: ')
         if answer == ('si'):
             print(f'{pid}{variant_1}')
             print(f'{pid}{variant_2}')
             print(f'{pid}{variant_3}')
             print(f'{pid}{variant_4}')
             print(f'{pid}{variant_5}')
             print(f'{pid}{variant_6}')
             print(f'{pid}{variant_7}')
             print(f'{pid}{variant_8}')
             print(f'{pid}{variant_9}')
             time.sleep(10)
             break
         else:
             print("Risposta non valida!")
             sys.exit()
     except ValueError:    
         print('Non hai inserito un numero,riprova!')
         continue
