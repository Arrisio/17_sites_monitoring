import whois
import requests
from datetime import datetime, timedelta
import argparse


def load_urls4check(path):
    with open(path, 'r', encoding='UTF8') as file_handler:
        for url in file_handler.read().splitlines():
            yield (
                url,
                is_server_respond_with_200(url),
                get_domain_expiration_date(url)
            )


def is_server_respond_with_200(url):
    try:
        return requests.get(url).ok
    except requests.exceptions.ConnectionError:
        return


def get_domain_expiration_date(domain_name):
    today_plus_month = datetime.today() + timedelta(days=+30)
    expiration_date = whois.whois(domain_name).expiration_date

    if isinstance(expiration_date, list):
        expiration_date = max(
            [date.replace(tzinfo=None) for date in expiration_date]
        )
        return expiration_date > today_plus_month

    elif isinstance(expiration_date, datetime):
        return expiration_date.replace(tzinfo=None) > today_plus_month


def print_url_statuses(url_statuses):
    print('Domains statuses:')
    row_template = '{:<60} | {:^20} | {:^20}'
    horizontal_line = '-' * 100
    print(row_template.format('Url', 'Is URL ok', 'Domain status'))
    print(horizontal_line)

    for url, url_status, domain_status in url_statuses:
        print(
            row_template.format(
                url,
                'yes' if url_status else 'no',
                'error' if domain_status is None
                else 'OK' if domain_status else 'expired'
            )
        )


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
    try:
        print_url_statuses(load_urls4check(parse_arguments().filepath))
    except (FileNotFoundError, UnicodeDecodeError) as read_urls_error:
        exit("Can't read file with urls:\n{}".format(read_urls_error))
