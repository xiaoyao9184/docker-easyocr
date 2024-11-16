import easyocr
from easyocr.config import recognition_models, detection_models
from logging import getLogger

LOGGER = getLogger(__name__)

for detect_network in detection_models:
    try:
        LOGGER.warning('')
        LOGGER.warning('Progress detect_network: %s', detect_network)
        easyocr.Reader([], gpu=False, recognizer=False, detect_network=detect_network)
    except Exception as e:
        LOGGER.error('Failed to load detect_network %s: %s', detect_network, e)

# fix https://github.com/JaidedAI/EasyOCR/issues/1315
recognition_models['gen1']['tamil_g1']['characters'] = '0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZஃஅஆஇஈஉஊஎஏஐஒஓஔகஙசஜஞடணதநனபமயரறலளழவஷஸஹாிீுூெேைொோௌ்'
for recog_network in [m for g in recognition_models for m in recognition_models[g]]:
    try:
        LOGGER.warning('')
        LOGGER.warning('Progress recog_network: %s', recog_network)
        easyocr.Reader([], gpu=False, detector=False, recog_network=recog_network)
    except Exception as e:
        LOGGER.error('Failed to load recog_network %s: %s', recog_network, e)
