# .env ファイルをロードして環境変数へ反映
from dotenv import load_dotenv
load_dotenv()

# 環境変数を参照
import os
IMAGE_PATH = os.getenv('IMAGE_PATH')
ORIGINAL_FILES_PATH = os.getenv('ORIGINAL_FILES_PATH')
OUTPUT_FILES_PATH = os.getenv('OUTPUT_FILES_PATH')
INVOICE_TEMPLATES_PATH = os.getenv('INVOICE_TEMPLATES_PATH')


# 環境変数一覧
# print(config.IMAGE_PATH)
# print(config.ORIGINAL_FILES_PATH)
# print(config.OUTPUT_FILES_PATH)
# print(config.INVOICE_TEMPLATES_PATH)