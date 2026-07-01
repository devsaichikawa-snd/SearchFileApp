import logging

from input import get_args
from log_config import setup_logging

logger = logging.getLogger(__name__)


def main():
    setup_logging()
    args = get_args()

    logger.info("===== 検索実行 =====")
    logger.info("root_dir: %s", args.root_dir)
    logger.info("file_name: %s", args.file_name)
    logger.info("extension: %s", args.extension)
    logger.info("===== 検索終了 =====")


if __name__ == "__main__":
    main()
