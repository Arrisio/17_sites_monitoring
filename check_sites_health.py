import whois
import requests
from datetime import datetime
import argparse

def load_urls4check(path):
    with open(path, 'r', encoding='UTF8') as file_handler:
        print(file_handler.readlines())


def is_server_respond_with_200(url):
    return requests.get(url)

def get_domain_expiration_date(domain_name):
    w = whois.whois(domain_name)
    return w.expiration_date.isoformat()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', action='store',
        dest='filepath',
        help='Filepath to urls list',
        required=True
    )
    return parser.parse_args()


if __name__ == '__main__':
    url = 'https://aaaservice.jet.su'
    try:
        load_urls4check(parse_arguments().filepath)
    except (FileNotFoundError, UnicodeDecodeError) as read_urls_error:
        exit("Can't read file with urls:\n{}".format(read_urls_error))
    # print(get_domain_expiration_date(url))
    # print(is_server_respond_with_200(url))
#