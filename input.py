import argparse
from pathlib import Path


def valid_directory(path_str: str) -> Path:
    path = Path(path_str)

    if not path.is_absolute():
        raise argparse.ArgumentTypeError("絶対パスを指定してください")

    if not path.exists():
        raise argparse.ArgumentTypeError("指定されたパスは存在しません")

    if not path.is_dir():
        raise argparse.ArgumentTypeError("ディレクトリを指定してください")

    return path


def non_empty(value: str) -> str:
    if not value.strip():
        raise argparse.ArgumentTypeError("空文字は指定できません")
    return value.strip()


def valid_extension(ext: str) -> str:
    ext = ext.strip()

    if not ext.startswith("."):
        raise argparse.ArgumentTypeError("拡張子は . から始めてください")

    if len(ext) == 1:
        raise argparse.ArgumentTypeError("拡張子が不正です")

    return ext.lower()


def get_args() -> argparse.Namespace:
    """コンソール入力の引数を取得する

    Command:
        python main.py --root-dir C:/Users/ --file-name 収支管理 --extension .xlsx

    Discription:
        --root-dir: (例)'C:/Users/'
        --file-name: (例)'収支管理'
        --extension: (例)'.xlsx', '.pdf'

    Returns:
        args: list[str, str, str]
    """
    parser = argparse.ArgumentParser(description="ファイル検索プログラム")

    parser.add_argument(
        "--root-dir",
        type=valid_directory,
        required=True,
        help="検索対象のルートディレクトリ絶対パス",
    )

    parser.add_argument(
        "--file-name",
        type=non_empty,
        required=True,
        help="検索対象のファイル名称",
    )

    parser.add_argument(
        "--extension",
        type=valid_extension,
        required=False,
        help="(任意)検索対象のファイル拡張子",
    )

    return parser.parse_args()
