import os, requests

print("Welcome to Siris's Flight Club.\nWe find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
new_user_email = input("What is your email?\n")
new_user_email_check = input("Please type your email again.\n")

if new_user_email == new_user_email_check:
    print("You're in the club!")
    email = new_user_email  # It's better to use 'new_user_email' as it's already checked for equality.

    # Corrected payload structure
    payload = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }

    USERS_POST_ENDPOINT = os.environ.get('USERS_POST_ENDPOINT')
    SHEETY_BEARER_TOKEN = os.environ.get('SHEETY_BEARER_TOKEN', 'Sheety Bearer Token does not exist')
    headers = {"Authorization": f"Bearer {SHEETY_BEARER_TOKEN}", "Content-Type": "application/json"}



    users_post_response = requests.post(url=USERS_POST_ENDPOINT, headers=headers,
                                        json=payload)  # to pass the payload with the proper 'json' parameter structure
    print(users_post_response.text)

else:
    print("Those 2 entered emails do not match. Please try again.")


