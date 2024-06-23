import random
import string


class random_generator:

    @staticmethod
    def get_gst_number():
        # gst_pattern = re.compile(r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$')
        gst_prefix = ''.join(random.choices('0123456789', k=2))
        gst_mid = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5))
        gst_year = ''.join(random.choices('0123456789', k=4))
        gst_month = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1))
        gst_day = ''.join(random.choices('0123456789', k=1))
        gst_suffix = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1))

        gst_number = f"{gst_prefix}{gst_mid}{gst_year}{gst_month}{gst_day}{'Z'}{gst_suffix}"
        return gst_number

    @staticmethod
    def get_pan_number():
        # pan_pattern = re.compile(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$')
        pan_prefix = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5))
        pan_middle = ''.join(random.choices('0123456789', k=4))
        pan_suffix = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1))

        pan_number = f"{pan_prefix}{pan_middle}{pan_suffix}"
        return pan_number

    @staticmethod
    def get_address():
        address_length = random.randint(3, 42)
        address = ''.join(random.choices(string.ascii_letters + string.digits, k=address_length))
        return address

    @staticmethod
    def get_city():
        city_length = random.randint(3, 42)
        city = ''.join(random.choices(string.ascii_letters, k=city_length))
        return city

    @staticmethod
    def get_state():
        state_length = random.randint(3, 42)
        state = ''.join(random.choices(string.ascii_letters, k=state_length))
        return state

    @staticmethod
    def get_pincode():
        first_digit = str(random.randint(1, 9))
        next_two_digits = ''.join(random.choices(string.digits, k=2))
        last_three_digits = ''.join(random.choices(string.digits, k=3))
        pincode = first_digit + next_two_digits + last_three_digits
        return pincode

    @staticmethod
    def get_mobile():
        mobile_number = str(random.randint(6, 9))
        for _ in range(9):
            mobile_number += str(random.randint(0, 9))
        return mobile_number

    @staticmethod
    def get_email():
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        domain = ''.join(random.choices(string.ascii_lowercase, k=8)) + '.com'
        email = f"{username}@{domain}"
        return email

