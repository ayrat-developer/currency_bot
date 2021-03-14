class Data():
    """Обработка данных для вывода"""
    def __init__(self, values):
        self.names = values[::3]

        del values[::3]

        self.buys = values[::2]
        self.sells = values[1::2]

        self.best_buy_value = max(self.buys)
        self.best_sell_value = min(self.sells)

    def get_all_list(self):
        message = ''
        i = 0
        while i < len(self.names):
            message += f'{self.names[i]}: \nПродажа: {self.buys[i]} \nПокупка: {self.sells[i]} \n\n'
            i+=1

        message = message.rstrip()

        return message

    def __get_best_values(self, values, best_value):
        message = ''

        i = 0
        while i < len(values):
            if values[i] == best_value:
                message += f'{self.names[i]}: {best_value}\n'
            i += 1 
        
        message = message.rstrip()
        return message

    def get_best_buy_value(self):
        return self.__get_best_values(self.buys, self.best_buy_value)
        
    def get_best_sell_value(self):
        return self.__get_best_values(self.sells, self.best_sell_value)