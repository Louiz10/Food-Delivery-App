
import json
from pprint import pprint
from datetime import datetime

user_details = {
    "lucifer@gmail.com": {
        "password": "1234",
        "access": "admin",
        "name": "Lucifer MorningStar"
    }
}

login_details = {
    "lucifer@gmail.com": {
        "session_time": ""
    }
}

item_details = order_details = {}


class Admin:
    def __init__(self):
        pass

    def login(self, email, password):

        if email not in user_details:
            pprint("Email not registered")
            return

        if user_details[email].get("access", "user") != "admin":
            pprint("You don't have admin access.")
            return

        if user_details[email].get("password", "") != password:
            pprint("Login Failed. Please check your credentials.")
            return

        login_details[email] = {
            "session_time": datetime.now(),
            "status": "logged_in"
        }

        pprint("Admin Login Succeeded -> {} and Session starts at -> {}".format(email, datetime.now()))
        return

    def logout(self, email):
        if email in login_details:
            pprint("Logged out successfully -> {}".format(email))
            login_details[email].update({"status": "logged_out"})

        return


class Item:
    def __init__(self):
        pass

    def create_item(self, item_name, quantity, price, discount, stock):

        item_id = len(item_details) + 1

        item_details[item_id] = {
            "item_id": item_id,
            "item_name": item_name,
            "quantity": quantity,
            "price":  price,
            "discount": discount,
            "stock": stock
        }

        pprint("Item details for itemID [{}] has been added successfully -> {}".format(item_id, item_details[item_id]))
        return

    def update_item(self, item_id, item_name, quantity, price, discount, stock):
        item_details[item_id] = {
            "item_id": item_id,
            "item_name": item_name,
            "quantity": quantity,
            "price": price,
            "discount": discount,
            "stock": stock
        }

        pprint("Item details for itemID [{}] has been update successfully -> {}".format(item_id, item_details[item_id]))
        return

    def remove_item(self, item_id):


        pprint("Item removed from item details for itemID [{}] successfully".format(item_id))
        return

    def get_all_item(self):
        all_items = []
        for item in item_details.values():
            all_items.append(str(item["item_id"]) + ". " + item["item_name"] + " (" + str(item["quantity"]) + ") " + item["price"])

        pprint(all_items)
        return


class User:
    def __init__(self):
        pass

    def login(self, email, password):
        if email not in user_details:
            pprint("Email not registered")
            return

        if user_details[email].get("access", "user") == "admin":
            pprint("You don't have user access.")
            return

        if user_details[email].get("password", "") != password:
            pprint("Login Failed. Please check your credentials.")
            return

        login_details[email] = {
            "session_time": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            "status": "logged_in"
        }

        pprint("User Login Succeeded -> {} and Session starts at -> {}".format(email, datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
        return

    def logout(self, email):
        if email in login_details:
            pprint("Logged out successfully -> {}".format(email))
            login_details[email].update({"status": "logged_out"})

        return

    def register(self, name, mobile_num, email, password, address):
        """
        Full Name
        Phone Number
        Email
        Address
        Password
        """
        user_details[email] = {
            "email": email,
            "password": password,
            "access": "user",
            "name": name,
            "mobile_num": mobile_num,
            "address": address
        }

        pprint("User registered for email [{}] successfully -> {}".format(email, user_details[email]))
        return

    def update_profile(self, name, mobile_num, email, password, address):
        user_details[email].update({
            "email": email,
            "password": password,
            "access": "user",
            "name": name,
            "mobile_num": mobile_num,
            "address": address
        })
        pprint("User profile details updated for email [{}] successfully -> {}".format(email, user_details[email]))
        return


class Order:
    def __init__(self):
        pass

    def list_orders_by_user(self, email):

        user_order_details = []

        if email in order_details:

            for order_info in order_details[email]:
                order_info.update(item_details[order_info["item_id"]])
                user_order_details.append(order_info)

        pprint("Orders done by user [{}] -> {}".format(email, json.dumps(user_order_details)))
        return

    def list_all_orders(self, email):
        pprint(order_details.values())
        return

    def list_order_history(self, email):
        pprint(order_details[email].values())
        return

    def order_item(self, email, item_ids):
        orders = order_details[email] if email in order_details else []
        for item_id in item_ids:
            orders.append({"item_id": item_id, "order_time": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})

        order_details[email] = orders

        pprint("Order(s) has been placed successfully {} -> {}".format(email, orders))
        return