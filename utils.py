import re
from email.parser import Parser

def extract_ip(header_value):
    return re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', header_value)

def parse_email_header(raw_header):
    header = Parser().parsestr(raw_header)
    received_headers = header.get_all("Received")

    ip_addresses = []
    if received_headers:
        for received in received_headers:
            ip_addresses.extend(extract_ip(received))

    return {
        'From': header.get('From'),
        'To': header.get('To'),
        'Subject': header.get('Subject'),
        'Date': header.get('Date'),
        'Return-Path': header.get('Return-Path'),
        'Message-ID': header.get('Message-ID'),
        'Received-Headers': received_headers,
        'IP-Addresses': list(set(ip_addresses)),
    }
