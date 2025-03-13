from crawler import looping_adress_crawler
from scraper import create_data_frame

if __name__ == '__main__':
    url = 'https://www.boliga.dk/resultat?searchTab=0&page='
    filename = 'addresses.txt'
    looping_adress_crawler(url, filename)
    df = create_data_frame(filename)
    df.to_csv('boligpriser.csv', index=False)
    print(df)