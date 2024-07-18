import os


def get_option(cmd):
    commands_opt = {
        'food': 'food',
        'health': 'health',
        'transport': 'transport',
        'education': 'education',
        'leisure': 'leisure',
        'remove': 'remove',
    }
    return commands_opt.get(cmd, 'Invalid option')


class FinanceManager:
    def __init__(self, act_money=0):
        self.money = act_money


class UserData(FinanceManager):
    def __init__(self, act_money=0):
        super().__init__(act_money)

        self.expenses = {
            'food': 0,
            'health': 0,
            'transport': 0,
            'education': 0,
            'leisure': 0,
            'remove': 0
        }

    def add_money(self):
        try:
            insert_money = float(input('How much money do you want to add?: '))
            self.money += insert_money
            print(f'Current balance: ${self.money:.2f}')
        except ValueError:
            print('Enter only numbers')

    def spent(self):
        try:
            insert_spent = float(input('How much money has been spent?: '))
            self.money -= insert_spent
            print('Options: \n 1. Food \n 2. Health \n 3. Transport \n 4. Education \n 5. Leisure \n 6. Remove money')
            commands_spent = {
                '1': 'food',
                '2': 'health',
                '3': 'transport',
                '4': 'education',
                '5': 'leisure',
                '6': 'remove',
            }
            insert_opt = input('Select an option: ').strip()
            if insert_opt not in commands_spent:
                print('Unknown option')
            else:
                self.expenses[commands_spent[insert_opt]
                              ] += insert_spent  # type: ignore
                print('Expense added to the selected category')

        except ValueError:
            print('Invalid value, please enter a number')
        except Exception as e:
            print(f'An error occurred: {e}')

    def generate_report(self):
        print('Expense Report:')
        total_spent = sum(self.expenses.values())

        for category, amount in self.expenses.items():
            print(f'{category.capitalize()}: ${amount:.2f}')

        print(f'Total: ${total_spent:.2f}')

    def calculate_deficit_or_profit(self):
        total_spent = sum(self.expenses.values())

        if self.money < total_spent:
            deficit = total_spent - self.money
            print(f'Deficit: ${deficit:.2f}')

        else:
            profit = self.money - total_spent
            print(f'Profit: ${profit:.2f}')


def main():
    user = UserData()

    while True:
        commands = {
            '1': lambda: user.add_money(),
            '2': lambda: user.spent(),
            '3': lambda: user.generate_report(),
            '4': lambda: user.calculate_deficit_or_profit(),
            '5': lambda: exit()
        }

        print('Options: \n 1. Add money \n 2. Add expense \n 3. View report \n 4. View profit \n 5. Exit')

        user_cmd = input('Choose an option: ')
        if user_cmd not in commands:
            print('Unknown option')
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            commands[user_cmd]()


if __name__ == '__main__':
    main()
