import twitter
import pickle
import logging
import sys

import app.common as common

# Configure the logging for this run
logging.basicConfig(filename='../app.log',
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='a',
                    level=logging.INFO)
logging.info('START')

# Setup Twitter access
auth = common.get_auth()
api = twitter.Api(consumer_key=auth[0],
                  consumer_secret=auth[1],
                  access_token_key=auth[2],
                  access_token_secret=auth[3])

with open('../data/post_order.pkl', 'rb') as f:
    try:
        min_psim_post_queue = pickle.load(f)
    except Exception as e:
        logging.error(print(e))

if len(min_psim_post_queue) == 0:
    logging.error("Post queue is empty! Terminating script.")
    sys.exit()

media = min_psim_post_queue.pop()
logging.info("Posting image {} to Twitter. Next image will be {}".format(media, min_psim_post_queue[-1]))
media_id = api.UploadMediaSimple('../data/panels/' + media)
api.PostUpdate(status='', media=media_id)
logging.info("Successfully posted [media_id = {}]".format(media_id))


with open('../data/post_order.pkl', 'wb') as f:
    try:
        pickle.dump(min_psim_post_queue, f)
    except Exception as e:
        logging.warning('Post queue did not save properly. '
                        'The next time the script it executed it may post a duplicate image.')
        logging.error(print(e))

logging.info("END")
