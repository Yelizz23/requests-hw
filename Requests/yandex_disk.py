import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_link(self, disk_file_path):
        link_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'True'}
        res = requests.get(url=link_url, headers=headers, params=params)
        return res.json()

    def upload_file(self, disk_file_path, filename):
        response = self.get_link(disk_file_path=disk_file_path)
        url = response.get('href', '')

        if url:
            response = requests.put(url=url, data=open(filename, 'rt'))

            response.raise_for_status()
            print(response.status_code)
            if response.status_code == 201:
                print('Файл успешно загружен!')
            else:
                print(f'Ошибка: {response.status_code}')


if __name__ == '__main__':
    token = ''
    disk_file_path = '/Request/file.txt'
    uploader = YaUploader(token)
    result = uploader.upload_file(disk_file_path, 'file.txt')
