from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, time, db
import pandas as pd

#region FrontEnd
class Ui_MainWindow(object):
    """Клас який відповідає за графічний інтерфейс"""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")  #Назва вікна
        MainWindow.resize(633, 465)             #Розміри вікна
        font = QtGui.QFont()
        font.setKerning(True)
        #Підключаємо шрифти
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        #Задаємо позиції елементів і назви кнопок
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 280, 241, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_char_minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_char_minus.setObjectName("pushButton_char_minus")
        self.gridLayout.addWidget(self.pushButton_char_minus, 3, 0, 1, 1)
        self.pushButton_num_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_num_8.setObjectName("pushButton_num_8")
        self.gridLayout.addWidget(self.pushButton_num_8, 2, 1, 1, 1)
        self.pushButton_num_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_num_5.setObjectName("pushButton_num_5")
        self.gridLayout.addWidget(self.pushButton_num_5, 1, 1, 1, 1)
        self.pushButton_num_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_num_0.setObjectName("pushButton_num_0")
        self.gridLayout.addWidget(self.pushButton_num_0, 3, 1, 1, 1)
        self.pushButton_char_plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_char_plus.setObjectName("pushButton_char_plus")
        self.gridLayout.addWidget(self.pushButton_char_plus, 3, 2, 1, 1)
        self.pushButton_num_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_num_2.setObjectName("pushButton_num_2")
        self.gridLayout.addWidget(self.pushButton_num_2, 0, 1, 1, 1)
        self.pushButton_num_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_num_1.setObjectName("pushButton_num_1")
        self.gridLayout.addWidget(self.pushButton_num_1, 0, 2, 1, 1)
        self.pushButton_num_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_num_4.setObjectName("pushButton_num_4")
        self.gridLayout.addWidget(self.pushButton_num_4, 1, 2, 1, 1)
        self.pushButton_num_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_num_7.setObjectName("pushButton_num_7")
        self.gridLayout.addWidget(self.pushButton_num_7, 2, 2, 1, 1)
        self.pushButton_num_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_num_3.setObjectName("pushButton_num_3")
        self.gridLayout.addWidget(self.pushButton_num_3, 0, 0, 1, 1)
        self.pushButton_num_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_num_6.setObjectName("pushButton_num_6")
        self.gridLayout.addWidget(self.pushButton_num_6, 1, 0, 1, 1)
        self.pushButton_num_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_num_9.setObjectName("pushButton_num_9")
        self.gridLayout.addWidget(self.pushButton_num_9, 2, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(450, 280, 171, 112))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_cansel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_cansel.setObjectName("pushButton_cansel")
        self.verticalLayout.addWidget(self.pushButton_cansel)
        self.pushButton_clear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.verticalLayout.addWidget(self.pushButton_clear)
        self.pushButton_ok = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.verticalLayout.addWidget(self.pushButton_ok)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 280, 181, 71))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_get_money = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_get_money.setObjectName("pushButton_get_money")
        self.verticalLayout_2.addWidget(self.pushButton_get_money)
        self.pushButton_send_money = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_send_money.setObjectName("pushButton_send_money")
        self.verticalLayout_2.addWidget(self.pushButton_send_money)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(80, 70, 471, 161))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setEnabled(True)
        self.label.setMaximumSize(QtCore.QSize(16777215, 500))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 633, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        ''' підписуємо кнопки'''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ATM"))#
        self.pushButton_char_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_num_8.setText(_translate("MainWindow", "8"))
        self.pushButton_num_5.setText(_translate("MainWindow", "5"))
        self.pushButton_num_0.setText(_translate("MainWindow", "0"))
        self.pushButton_char_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_num_2.setText(_translate("MainWindow", "2"))
        self.pushButton_num_1.setText(_translate("MainWindow", "1"))
        self.pushButton_num_4.setText(_translate("MainWindow", "4"))
        self.pushButton_num_7.setText(_translate("MainWindow", "7"))
        self.pushButton_num_3.setText(_translate("MainWindow", "3"))
        self.pushButton_num_6.setText(_translate("MainWindow", "6"))
        self.pushButton_num_9.setText(_translate("MainWindow", "9"))
        self.pushButton_cansel.setText(_translate("MainWindow", "Відміна"))
        self.pushButton_clear.setText(_translate("MainWindow", "Редагувати"))
        self.pushButton_ok.setText(_translate("MainWindow", "Підтвердити"))
        self.pushButton_get_money.setText(_translate("MainWindow", "Видача готівки"))
        self.pushButton_send_money.setText(_translate("MainWindow", "Поповнити карту"))
        self.label.setText(_translate("MainWindow", "ВВедіть пін-код"))
#endregion

#region BackEnd
class ATM(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.finished = False
        #Якщо True - вводимо пін-код і виводимо зірочки
        self.pin_code = True
        #Правильний пін код
        self.correct_pin = '1234'
        #Змінна що відповідає за вивід на монітор
        self.monitor_input_value = ''
        #змінна що зберігає введені данні
        self.input_line_data = ''

        #Обробка натискання кнопок з цифрами
        #region num_keyboard
        self.pushButton_num_0.clicked.connect(lambda: self.click_number(num=0))
        self.pushButton_num_1.clicked.connect(lambda: self.click_number(num=1))
        self.pushButton_num_2.clicked.connect(lambda: self.click_number(num=2))
        self.pushButton_num_3.clicked.connect(lambda: self.click_number(num=3))
        self.pushButton_num_4.clicked.connect(lambda: self.click_number(num=4))
        self.pushButton_num_5.clicked.connect(lambda: self.click_number(num=5))
        self.pushButton_num_6.clicked.connect(lambda: self.click_number(num=6))
        self.pushButton_num_7.clicked.connect(lambda: self.click_number(num=7))
        self.pushButton_num_8.clicked.connect(lambda: self.click_number(num=8))
        self.pushButton_num_9.clicked.connect(lambda: self.click_number(num=9))
        #endregion
        self.pushButton_cansel.clicked.connect(self.cansel_operation)
        self.pushButton_clear.clicked.connect(self.clear_operation)

        #Кнопка обробки команди "Підтвердити". Якщо змінна pin_code == True -
        # виконається команда перевірки пін-коду, False - видачі готівки
        self.pushButton_ok.clicked.connect(lambda: self.button_ok(operation=self.pin_code))
        #Обробка кнопок "видача готівки" і "поповнити"
        self.pushButton_send_money.clicked.connect(self.send_money)
        self.pushButton_get_money.clicked.connect(self.get_money_button)

    def send_money(self):
        '''Логіка поповнення балансу: відкривається діалогове вікно, обираємо файл.
        Далі читаємо файл, перевіряємо чи банкноти існують, якщо так - додаємо в бд
        потрібну к-сть, якщо ні - виводимо помилку'''
        self.file_path = ''                             #шлях до файлу по замовчуванню
        self.browserfile()                              #Відкрити діалогове вікно
        df = pd.read_excel(self.file_path).values       #Відкити вибраний файл
        for data in df:
            #Проходимося по даних з вибраного файлу
            try:
                currency = data[0]                      #клітинка i 0 - де і - номер рядка - номінал
                count = data[1]                         #клітинка i 1 - де і - номер рядка - кількість
                if int(currency) in [1000, 500, 200, 100, 50, 20, 10]:
                    #Якщо номінал існує - додаємо вказану кількість в базу даних
                    db.update_count(currency, count, operation='plus')
                else:
                    #якщо номінал не існує - виводимо повідомлення про помилки і перериваємо операцію
                    QMessageBox.about(self, 'Помилка', 'В файлі вигрузки є помики')
                    break
                print('Внесено {0} гривневу купюру в кількості {1} шт.'.format(currency, count))
            except Exception as e:
                print(e)

    def browserfile(self):

        filedirectory = QtWidgets.QFileDialog.getOpenFileName(self, 'Вибрати файл',
                                              filter='(*.csv *.xls *.xlsx)')
        filepatch = filedirectory[0]
        if filedirectory:
            #Якщо файл вказаний - зберігаємо його в змінну file_path
            self.file_path = filepatch

    def clear_operation(self):
        '''Очищуємо дисплей'''
        self.lineEdit.clear()
        self.input_line_data = ''
        self.monitor_input_value = ''

    def cansel_operation(self):
        '''Скасовуємо операції з картою і повертаємося до вводу пін-коду'''
        self.label.setText('Введіть пін-код:')
        self.pin_code = True
        self.input_line_data = ''
        self.monitor_input_value = ''
        self.lineEdit.clear()

    def click_number(self, num):
        '''Опрацювання натискань на цифрову клавіатуру.
        Якщо пін-код ще не введено - цифри які натискаються це пін-код
        В протилежному випадку - це сума до зняття'''
        if self.pin_code == True and len(self.monitor_input_value) < 4:
            #Якщо пін код раніше не був введений, а кількість натискань менше 4
            self.monitor_input_value += '*'                 #Додаємо до змінної яка виводить на дисплей - *
            self.input_line_data += str(num)                #Введене чисо запам'ятовуємо
            self.lineEdit.setText(self.monitor_input_value) #Виводимо все на диспей
        elif self.pin_code == True and len(self.monitor_input_value) == 4:
            #Якщо пін введено пін-код розміром 4 символи - відправляємо його на перевірку
            self.button_ok(operation='pincode')
        else:
            #Якщо пін-код було введено раніше, значить це сума до зняття.
            # Відповідно на екран виводимо не зірочки а цифри, данні запам'ятовуємо
            self.monitor_input_value += str(num)                #Те що буде відображатися на екрані
            self.input_line_data += str(num)                    #Те що запам'ятаємо для обробки
            self.lineEdit.setText(self.monitor_input_value)     #Вивід на екран

    def button_ok(self, operation):
        '''Обробка кнопки "підтвердити" та її логіка.'''
        try:
            if operation:
                #Якщо пін-код
                self.lineEdit.clear()               #Очищуємо дисплей
                if str(self.input_line_data) == str(self.correct_pin):
                    self.input_line_data = ''  # Обнуляємо зміну пам'яті введеного
                    self.monitor_input_value = ''  # Обнуляємо змінну виводу на екран
                    self.pin_code = False               #Пін-код ставимо в положення "вірно"
                    get_currency_atm = db.get_data()    #Отримуємо перелік доступних банкнот
                    message_display = 'Введіть суму:\nДоступні банкноти: '  #Повідомлення для виводу
                    for currency in get_currency_atm:
                        #Проходимося по всіх банкнотах і додаємо їх в змінну з повідомленням для виводу
                        message_display += str(currency[0]) + ', '
                    self.label.setText(message_display[:-2])        #Виводимо данні на екран
                else:
                    print(self.input_line_data)
                    message_display = 'Не правильний пін-код, повторіть спробу:'
                    self.label.setText(message_display)
                    self.input_line_data = ''  # Обнуляємо зміну пам'яті введеного
                    self.monitor_input_value = ''  # Обнуляємо змінну виводу на екран
                    self.lineEdit.clear()

            elif not operation:
                #Якщо сума до зняття
                summ = self.input_line_data                 #Отримуємо суму до зняття
                message_display = 'Видано:\n'               #Підготовуємо змінну для запису даних про видачу (якої валюти і скільки)
                min_balance = int(summ)                     #Заишок до видачі (в подальшому будемо використовувати для пошуку найменшої к-сті банкнот
                get_currency_atm = db.get_data()            #Отримуємо список доступних банкнот
                atm_summ = 0                                #Оголошуємо змінну яка відповідає за загальну суму грошей в банкоматі
                currency_list = []                          #Список з номіналом і кількістю
                for currency in get_currency_atm:
                    #Проходимося по всіх банкнотах
                    atm_summ += (currency[0] * currency[1]) #Множимо кількість на номінал і додаємо до все щоб отримати загальну суму грошей в банкоматі

                if int(summ) > atm_summ:
                    #Якщо сума до видачі перевищує загальну суму грошей в банкоматі
                    self.label.setText('В банкоматі недостатньо коштів.\nМаксимальна сума ' +
                                       'до зняття - {0} UAH'.format(atm_summ))
                    #Виводимо повідомлення скільки максимум можна зняти
                else:
                    #Якщо сума до видачі менша за максимальну в банкоматі
                    for currency in get_currency_atm:
                        #Проходимося по всіх валютах
                        nominal = currency[0]           #Номіна
                        count = currency[1]             #Кількість
                        if int(count) != 0:
                            #Якщо кількість банкнот даного номіналу більше 0
                            need_to = int(int(min_balance) / int(nominal))      #Вирааховуємо скільки банкнот потрібно видати
                            if min_balance != 0:
                                #Перевіряємо чи залишок до видачі не 0
                                if need_to < count:
                                    #Якщо потрібно видати менше банкнот ніж є в наявності
                                    min_balance = min_balance - (need_to * nominal)             #Відімаємо від залишку до видачі суму яку можемо видати банкнотами в ітерації
                                    message_display += '{0} по {1}\n'.format(need_to, nominal)  #Додаємо це до змінної яка виводить смс з інформцією чого і скільки видано
                                    currency_list.append([need_to, nominal])                    #Додаємо кількість і номінал для подальшого опрацювання базою даних
                                else:
                                    #Якщо потрібно видати більше банкнот ніж є в наявності
                                    min_balance = min_balance - (count * nominal)               #Віднімаємо від залишку до видачі максимальну кількість банкнот яку ми можемо видати
                                    message_display += '{0} по {1}\n'.format(count, nominal)    #Додаємо інформацію до змінної яка виводить в кінці скільки видано і чого
                                    currency_list.append([count, nominal])                      #Додаємо кількість і номінал для подальшого опрацювання базою данних
                            else:
                                #Якщо залишок до видачі рівний нулю - перериваємо цикл, якщо ні - продовжуємо до останньої банкноти
                                break

                    if min_balance == 0:
                        #Якщо заишок до видачі нуль - опрацювуємо видані банкноти.
                        #Проходимося по всіх виданих банкнотах
                        for data in currency_list:
                            count = data[0]                                 #Кількість
                            nominal = data[1]                               #Номінал
                            db.update_count(nominal, count, 'minus')        #Обновлюємо залишок в бд
                        currency_list.clear()                               #Після завершення циклу обнуляємо список
                        self.label.setText('Вивдаю {0} UAH'.format(summ))   #Виводимо інформацію про суму яка видана
                        QMessageBox.about(self, 'Успішно', message_display) #Виводимо інформацію про номінали і кількість
                    else:
                        '''Якщо заишок більше нуля - віднімаємо від суми до виводу - залишок і отримуємо максимальну суму
                        до видачі, яка не перевищує введену користувачем. Виводимо дані про це на екран.'''
                        currency_list.clear()
                        self.label.setText('Не вистачає банкнот.\nМаксимальна сума'
                                                           ' для зняття доступна вам: {0}'.format(int(summ)-int(min_balance)))
                self.input_line_data = ''           #Очищуємо пам'ять вводу
                self.monitor_input_value = ''       #Очищуємо змінну яка виводить інформацію на дисплей
        except Exception as e:
            print(e)

    def get_money_button(self):
        '''Опрацювання кнопки "вивести кошти"
        Якщо пін-код введено - виводить повідомлення про доступні банкноти, і просить ввести суму
        Якщо не введено - виводить інформацію про це на екран.'''
        if self.pin_code == False:
            get_currency_atm = db.get_data()
            message_display = 'Введіть суму:\nДоступні банкноти: '
            for currency in get_currency_atm:
                message_display += str(currency[0]) + ', '
            self.label.setText(message_display[:-2])
        else:
            self.label.setText('Спочатку введіть пін-код')

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ATM()
    window.show()
    app.exec_()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)