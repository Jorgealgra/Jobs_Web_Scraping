from utils import *

if __name__ == '__main__':

    get_jobs = GetJobs("http://www.google.com/search?q=job+data+scientist")
    final = get_jobs.scraping_jobs(int(input(str("Introduce el número de ofertas que quieres guardar: \n"))))
    print("CSV Descargado Correctamente")
    df = pd.DataFrame(final, columns=['1','Title', 'Company','City', 'Offer_website', 'Updated','Full_Half_Time_Job', 'Google_link',
                               'Apply_link'], dtype=str)
    df.to_csv('Data/jobs_data.csv')
