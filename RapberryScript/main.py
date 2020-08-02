import serial  # библеотека для работы с последовательный портом
import time  # библеотека для работы со времянем
from catagram import TelegramBot  # библеотека для работы с telegram API


# port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=3.0)

# Объект последовательного порта
port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=3.0)
# Объект телеграм бота
bot = TelegramBot()


def push_command(cmd):  # отправить команду модулю
    string = 'AT+{}\r\n'.format(cmd)
    port.write(bytes(string, 'ascii'))
    rcv = port.readline()
    print(rcv)


# Настриваем модуль
push_command('ADDRESS=2')
push_command('NETWORKID=1')
push_command('BAND=868500000')
push_command('PARAMETER=10,7,1,7')


while True:
    time.sleep(1)
    rcv = port.readline()             # Читаем буффер
    if(rcv):                          # Если сообщение есть
        print(rcv)
        rcv = rcv.decode("ascii")     # Дешифруем сообщение
        if(rcv.startswith('+RCV')):   # Если сообщение начинается с
            rcv = rcv[5:-2:]          # +RCV, то делим сообщение
            answer = rcv.split(',')   # Именно третий пункт ответа
            print(answer[2])          # содержит текст сообщения
            # Отправляем сообщение в телеграмм
            status = bot.send_text(answer[2])
            print(status)
