from pandas import read_csv

def convert_csv_to_parquet(year: int, dataset: str):
    try:
        print('Converting csv to parquet.')
        csv_df = read_csv(f'{dataset}{year}.csv')
        csv_df.to_parquet(f'{dataset}{year}.parquet')
        print('Conversion successful!')
    except Exception as e:
        print('CSV to parquet conversion failed :', e)

years = [
    '2011','2012','2013',
    '2014','2015','2016',
    '2017','2018','2019',
    '2020','2021',]

datasets_to_convert = [
    'tax_zip_code_',
    'data_dict',]

for year in years:
    convert_csv_to_parquet(year=year, dataset=datasets_to_convert[0])
    convert_csv_to_parquet(year=year, dataset=datasets_to_convert[1])