import subprocess
import json
from datasets import load_dataset

class RetailStoreData:
    """
    KoAlpacaData 데이터 처리 클래스
    # download data from internet
    # Print sample
    # Sample dataset
    # 
    """
    # def __init__(self, download_folder):
    #     self.download_folder = download_folder
    #     self.download()
    def __init__(self, data_file_name, download_folder=None, split_rate=None, is_split=False, is_download=False):
        self.download_folder = download_folder
        self.data_file_name = data_file_name
        self.raw_dataset = None
        self.train_dataset = None
        self.val_dataset = None
        self.split_rate = split_rate
        if is_download:
            self.download()
        else:
            print("Existing data is used")
            pass
        self.load_data_json()
        
        if is_split:
            self.split_train_test()
        else:
            self.set_train_dataset()
            
        # self.split_train_test()


    def download(self):
        '''
        다운로드 데이터
        '''
        pass

    def load_data_json(self):
        '''
        다운로드 데이타를 변수에 로딩
        '''
        data_file_path = f"{self.download_folder}/{self.data_file_name}"
        print("data_file_path: ", data_file_path)
        with open(data_file_path, 'r') as f:
            self.raw_dataset = json.load(f)

    def set_train_dataset(self):
        self.train_dataset = self.raw_dataset

            
    def split_train_test(self):
        length = len(self.raw_dataset)
        train_end = int(length * self.split_rate)

        print("train_end: ", train_end)
        self.train_dataset = self.raw_dataset[0:train_end]
        self.val_dataset = self.raw_dataset[train_end:]

    def show_sample_dataset(self, dataset, show_num):
        print("Size of dataset: ", len(dataset))
        print(dataset[:show_num])

    def sample_dataset(self, dataset, sample_size, sample_json_file):
        ''''
        인자로 제공된 데이터 셋에서 샘플 사이즈 만큼을 제공 함.
        '''
        sample_dataset = dataset[0:sample_size]
        sample_dataset = json.dumps(sample_dataset)
        print("Size of sample dataset: ", len(sample_dataset))
        with open(sample_json_file, "w") as outfile:
            outfile.write(sample_dataset)    
        dataset = load_dataset("json", data_files=sample_json_file, split='train')

        return dataset




    
    
        
