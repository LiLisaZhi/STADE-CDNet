
class DataConfig:
    data_name = ""
    root_dir = ""
    label_transform = ""
    def get_data_config(self, data_name):
        self.data_name = data_name
        if data_name == 'LEVIR':
            self.label_transform = "norm"
            self.root_dir = '/where'
        elif data_name == 'DSIFN':
            self.label_transform = "norm"
            self.root_dir = '/where'
        elif data_name == 'WHU':
            self.label_transform = "norm"
            self.root_dir = '/where'
        elif data_name == 'CDD':
            self.label_transform = "norm"
            self.root_dir = '/where'
        elif data_name == 'TYPO':
            self.label_transform = "norm"
            self.root_dir = '/where'
        elif data_name == 'quick_start_LEVIR':
            self.root_dir = '/where'
        elif data_name == 'quick_start_DSIFN':
            self.root_dir = '/where'
        else:
            raise TypeError('%s has not defined' % data_name)
        return self




if __name__ == '__main__':
    data = DataConfig().get_data_config(data_name='LEVIR')
    print(data.data_name)
    print(data.root_dir)
    print(data.label_transform)

