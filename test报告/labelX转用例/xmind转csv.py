import json
import xmind
from xmind2testcase.zentao import xmind_to_zentao_csv_file


def main():
    # 在这里输入要转换的xmind文件，运行即可在同一文件夹下生成csv文件。
    xmind_file = '/Users/smai/Desktop/sh/MS存储改造用例.xmind'
    print('Start to convert XMind file: %s' % xmind_file)

    zentao_csv_file = xmind_to_zentao_csv_file(xmind_file)
    print('Convert XMind file to zentao csv file successfully: %s' % zentao_csv_file)

    print('Finished conversion, Congratulations!')


if __name__ == '__main__':
    main()
