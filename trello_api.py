# PACKAGES
from trello import TrelloClient
import pandas as pd
import csv
from datetime import date


# TRELLO API CONNECTION
client = TrelloClient(
    api_key="67f3ec25de74237ab2268e7b0f23057a",
    # api_secret="A63b2472afdbe2211a8ddf22a20692e3bef0e30b2f9ae29d992fd6021d7d77e0",
    token="6e77a1c0f96fd81a6cd838ba34ea8bfa6efd8a6a0de17fd820b4bd7ad25af2c5",
)


# EXPLORE TRELLO DATA
# all_boards = client.list_boards()
# dev_board = all_boards[-1]
# print(dev_board)
# print(client.get_label(board_id=dev_board.board_id))
print(client.list_boards(board_filter="all"))
