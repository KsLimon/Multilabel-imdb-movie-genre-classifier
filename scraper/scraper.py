from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

def main():
    url = "https://www.imdb.com/search/title/?num_votes=10000%2C&sort=user_rating%2Cdesc&title_type=feature&fbclid=IwAR1i0nrqbnIun7kmWd7QJj5GFwZ6HFHXYIgnbFD7wh5RNX5ZuQ2NBJ_XxEE"

    driver = webdriver.Chrome('chromedriver')
    driver.get(url)

    c=1
    movie_data = []

    for trip in range(190):
        print(trip)
        main_div = driver.find_element(By.CLASS_NAME, "lister-list")

        for i in range(1,50):
            xpath_title = f"//div[{i}]/div[3]/h3/a"
            xpath_d = f"//div[{i}]/div[3]/p[2]"
            xpath_genre = f"//div[{i}]/div[3]/p[1]"

            title = main_div.find_element(By.XPATH, xpath_title).text
            desc = main_div.find_element(By.XPATH, xpath_d).text

            to_the_g = main_div.find_element(By.XPATH, xpath_genre)
            genre = to_the_g.find_element(By.CLASS_NAME, "genre").text

            movie_data.append({
                "title": title,
                "description": desc,
                "genres": genre
            })
        
        c+=50
        nxt_url = f"https://www.imdb.com/search/title/?title_type=feature&num_votes=10000,&sort=user_rating,desc&start={c}&ref_=adv_nxt"
        driver.get(nxt_url)
    
    driver.close()

    df = pd.DataFrame(data=movie_data, columns=movie_data[0].keys())
    df.to_csv("Movie_details.csv", index=False)


    return

if __name__ == '__main__':
    main()
