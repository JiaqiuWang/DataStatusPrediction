"""
读入csv数据，到内存中
"""
import time
import pandas as pd


class DataProcess:

    # 类公有变量；IP地址或者写127.0.0.1

    # 构造函数
    def __init__(self, file_path):
        self.file_path = file_path

    # 析构函数
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")

# ---------------------------------------------------------------------------------------

    # 读取文本中每行的节点队
    def read_file(self):
        data = pd.read_csv(self.file_path, encoding='utf-8')
        print("data:")
        # 逐个元素判断是否为空值
        for i in range(len(data)):
            print("i:", i)
            # print("row: ", data.iloc[i])
            for j in data.columns:
                if str(data.iloc[i][j]) == "nan":
                    print("空值", data.iloc[i], j, "element：", data.iloc[i][j])
                    continue
                print(j, ":", str(data.iloc[i][j]))
            print()

# ---------------------------------------------------------------------------------------

    # 转换成格式化日期
    def read_file_like(self):
        data = pd.read_csv(self.file_path, encoding='utf-8')
        print("data:")
        # 逐个元素判断是否为空值
        for i in range(len(data)):
            print("i:", i)
            # print("row: ", data.iloc[i])
            for j in data.columns:
                if str(data.iloc[i][j]) == "nan":
                    print("空值", data.iloc[i], j, "element：", data.iloc[i][j])
                    continue
                print(j, ":", str(data.iloc[i][j]))
            print()
# ----------------------------------------------------------------------------------------------------------


def main_operation():
    """Part1: 初始化参数"""
    file_path = 'data/answered2.csv'  # 文件路径和文件名
    dp1 = DataProcess(file_path)
    dp1.read_file()

if __name__ == "__main__":
    # 记录算法运行开始时间
    start_time = time.clock()
    # main_operation
    main_operation()
    # 记录算法运行结束时间
    end_time = time.clock()
    print("Running time: %s Seconds" % (end_time - start_time))  # 输出运行时间(包括最后输出所有结果)


