## happy path
* chitchat_greet
  - action_hello_world
* mood_great
  - utter_happy

## sad path 1
* chitchat_greet
  - action_hello_world
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* chitchat_greet
  - action_hello_world
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
