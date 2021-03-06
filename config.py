# -*- coding: utf-8 -*-
import os

# CREDENTIALS
TOKEN = os.getenv('TG_TOKEN')  # restart the main script MANUALLY after this field is changed
ADMIN_PASSWORD = os.getenv('ADMIN_PW')  # to use special bot commands

# GROUPS
CHAT_GROUP = os.getenv('TG_CHAT_GROUP')

# INSTA_CREDENTIALS
INSTA_USERNAME = os.getenv('INSTA_USER')
INSTA_PASSWORD = os.getenv('INSTA_PW')
INSTA_USERNAME2 = os.getenv('INSTA_USER2')
INSTA_PASSWORD2 = os.getenv('INSTA_PW2')
INSTA_USERNAME3 = os.getenv('INSTA_USER3')
INSTA_PASSWORD3 = os.getenv('INSTA_PW3')
# INSTA_USERNAME4 = os.getenv('INSTA_USER4')
# INSTA_PASSWORD4 = os.getenv('INSTA_PW4')
# INSTA_USERNAME5 = os.getenv('INSTA_USER5')
# INSTA_PASSWORD5 = os.getenv('INSTA_PW5')
# INSTA_USERNAME6 = os.getenv('INSTA_USER6')
# INSTA_PASSWORD6 = os.getenv('INSTA_PW6')

# SWITCH VARS
fake_positive = True # If true, check & 45 & final response always positive
testing_times = False # If true, testing times are activated

# TIMES
if testing_times:
    ROUNDS_INTERVAL = 1 * 2 * 60  # interval between rounds, seconds TESTING
    DROP_WINDOW = 1 * 60  # drop window before each round_start, seconds TESTING
    ROUND_TIME = 1 * 0.1 * 60  # round_start time, seconds TESTING
    DROP_ANNOUNCE = 0.5 * 60 # drop_announcement time, seconds TESTING
    DROP_ENDS_SOON = DROP_WINDOW * 5 // 6 # drop_alert time TESTING
    CHECK_RESPONSE_DELETION_TIME = 5 * 60

else:
    ROUNDS_INTERVAL = 23 * 60 * 60  # interval between rounds, seconds
    DROP_WINDOW = 30 * 60  # drop window before each round_start, seconds
    ROUND_TIME = 1 * 60 * 60  # round_start time, seconds
    DROP_ANNOUNCE = 1 * 60 * 60 # drop_announcement time, seconds
    DROP_ENDS_SOON = DROP_WINDOW * 5 // 6 # drop_alert time
    CHECK_RESPONSE_DELETION_TIME = 5 * 60



BAD_USER_BAN_TIME = 15 * 24 * 60 * 60 # user ban time after bad behavior
# BAD_USER_BAN_TIME = 1 * 60 * 60 # user ban time after bad behavior TESTING

# PATH
CONFIG_NAME = 'config.py'  # this file's name
#FOLDER_PATH = '/home/Bot'  # this folder's full path
FOLDER_PATH = '/'  # this folder's full path

# DATABASE SETTINGS
DATABASE_URL = os.getenv('DATABASE_URL')

T_ROUND = {'NAME': 'round',
           'FIELDS':
               {
                   'STARTS_AT': 'starts_at',
                   'IS_FINISHED': 'is_finished',
                   'GROUP_ID': 'group_id',
                   'IN_PROGRESS': 'in_progress'
               }
           }
T_USER = {'NAME': 'participant',
          'FIELDS':
              {
                  'TG_NAME': 'tg_name',
                  'INSTA_LINK': 'insta_link',
                  'IS_BANNED': 'is_banned',
                  'BAN_WARNS': 'ban_warnings',
                  'USER_ID': 'user_id',
                  'FULL_NAME': 'full_name'
              }
          }
T_U_R = {'NAME': 'user_and_round',
         'FIELDS':
             {
                 'USER_ID': 'user_id',
                 'ROUND_ID': 'round_id'
             }
         }
