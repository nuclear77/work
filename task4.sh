#!/bin/bash

email_examples=(
    "valid@example.com"
    "invalid_email.com"
    "name@domain-with-dash.com"
    "too_long_usernameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee@example.com"
    "username@too_long_domaineeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee.com"
    "username@domain..com"
    "username@-domain.com"
    "username@domain-.com"
    "username@domain.com-"
    "u$ername@domain.com"
    "username@domain.c"
    "username@domain.123"
)

is_valid_email() {
    local email=$1

    pattern="\b[A-Za-z0-9._+-]{1,64}@[A-Za-z0-9.-]{1,255}\.[A-Za-z]{2,}\b"

    if [[ $email =~ $pattern ]]; then
        echo "Валидный: $email"
    else
        echo "Невалидный: $email"
    fi
}

for email in "${email_examples[@]}"; do
    is_valid_email "$email"
done
