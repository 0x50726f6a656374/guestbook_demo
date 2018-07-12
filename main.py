import os
import time
import database

from prettytable import PrettyTable


class GuestBook:
    def __init__(self, data):
        self.data = data
        self.user_list = []

    def start(self):
        option = self.menu()
        if option is '1':
            self.create()
        elif option is '2':
            self.read()
        elif option is '3':
            self.update()
        elif option is '4':
            self.delete()
        elif option is '0':
            exit(0)
        else:
            print("Oops ! Invalid option")
            time.sleep(2)

    @staticmethod
    def menu():
        while True:
            print("Welcome to guest book\r")
            print("Functions :")
            print("1. Create new user")
            print("2. Read all users")
            print("3. Update user")
            print("4. Delete users")
            option = input("Select Function to Start：")
            return option

    def create(self):
        name = input("Name：")
        birthday = input("Birthday：")
        phone = input("Phone:")
        user_dict = dict(name=name, birthday=birthday, phone=phone)
        self.data.create(user_dict)
        # self.user_list.append(user_dict)
        self.read()

    def read(self):
        table = PrettyTable(['No.', 'ID', "Name", "Birthday", "Phone"])
        count = 1
        for user in self.dump():
            table.add_row([count, user[0], user[1], user[2], user[3]])
            count += 1
        print(table)

    def dump(self):
        rows = self.data.read()
        return rows

    def update(self):
        self.read()
        data_row = self.dump()
        print("Input ID to Update")
        option = input("Select ID to Update：")
        print("=============================================")
        print("|| data with empty field's will be reserved ||")
        print("=============================================")
        uid = data_row[int(option) - 1][0]
        o_name = data_row[int(option) - 1][1]
        o_birthday = data_row[int(option) - 1][2]
        o_phone = data_row[int(option) - 1][3]

        n_name = input("Name：")
        n_birthday = input("Birthday：")
        n_phone = input("Phone:")
        if n_name is '':
            n_name = o_name
        if n_birthday is '':
            n_birthday = o_birthday
        if n_phone is '':
            n_phone = o_phone
        self.data.update(int(uid), str(n_name), str(n_birthday), str(n_phone))
        self.read()

    def delete(self):
        self.read()
        data_row = self.dump()
        print("Input ID to delete")
        option = input("Select ID to Delete：")
        # print(data_row[int(option)-1][0])
        uid = data_row[int(option) - 1][0]
        self.data.delete(int(uid))
        self.read()


def main():
    # create database and table
    db = database.DatabaseCheck()
    # pre check
    db.pre_check()
    # init database connection and utils
    data = database.Database()
    # pass ref
    guest = GuestBook(data)
    while True:
        guest.start()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
