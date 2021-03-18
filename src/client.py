"""
Run me!
(from root directory)
conda activate twitterbot
python src\\client.py --config configs\\config.ini
"""
# builtin packages
import argparse
import configparser

# external packages
import twitter

# bot packages below

# create argparser to take config.ini
parser = argparse.ArgumentParser()
parser.add_argument('--config', help='configuration file')


if __name__ == '__main__':
    #load configs
    args = parser.parse_args()
    config = configparser.ConfigParser()
    config.read(args.config)

    # example: activate api
    keys = config['Twitter Keys']

    api = twitter.Api(
        consumer_key=keys['API_Key'],
        consumer_secret=keys['API_Secret_Key'],
        access_token_key=keys['Access_Token'],
        access_token_secret=keys['Access_Token_Secret'],
        tweet_mode="extended",
    )

    # api.dosomething()

    

