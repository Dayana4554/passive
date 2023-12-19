import argparse
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from time import sleep
import socket
import requests
from selenium.webdriver.support import expected_conditions as EC


def search_full_name(full_name):
   
    words = full_name.split()
   
    driver = webdriver.Chrome()
    # Create an instance of the Chrome web driver with the specified options
    driver.get('https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui=' + words[0] + '+' + words[1] + '+&ou=&univers=pagesblanches&idOu=')
    

    try:
        accept_cookies_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'didomi-notice-agree-button'))
        )    
        accept_cookies_button.click()
    except:
        adress = "Not Found"
        num = "Not Found"

    results_div = driver.find_element(By.XPATH, '//*[@id="part-095296712800000000"]')
    results = results_div.text

    new = results.split("\n")
    id = new[0].split(" ")

    index = new[1].find(" Voir le plan")
    if index != -1:
        place = new[1][:index].strip()  # Extract the substring before "Voir le plan" and remove leading/trailing whitespace
 
    reponses = driver.find_element(By.XPATH, "//*[@id='part-095296712800000000']/div[2]/button")
    reponses.click()


    temp = driver.find_element(By.XPATH,"//*[@id='part-095296712800000000']/div[2]")
    tel = (temp.text).split("\n")



    lastplace = place.split(",")
    result = "First name: " +  id[1] + "\nLast name: " + id[0] + "\nAddress: " + lastplace[0] + "\n" + lastplace[1][1:] + "\nNumber: " + tel[2]


    driver.quit()

    return result

def search_ip_address(ip_address):
    reponse = requests.get("http://ip-api.com/json/" + ip_address).json()
    return "ISP: " + str(reponse['isp'])  + "\n" + "City Lat/Lon : (" + str(reponse['lat']) + ") / (" + str(reponse['lon']) + ")"
   

def search_username(username):
    # Set up Chrome options to run in headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run the browser in headless mode
    chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration (necessary in headless mode)

    # Create an instance of the Chrome web driver with the specified options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://checkmarks.com/')


    # Find the input field and enter the username
    username_input = driver.find_element(By.XPATH, '//input[@name="checkusername"]')
    username_input.send_keys(username)

    sleep(1)

    # Find the button and click it
    button = driver.find_element(By.XPATH, '//button[@name="checkusername"]')
    button.click()

    sleep(5)
    

    # Now you can find and print the results
    results_div = driver.find_element(By.XPATH, '//*[@id="results"]')
    results = results_div.text
    
    new = results.split("\n")

    results_list = []
    for i in new:
        temp = i.split(" ")
        t = temp[0].capitalize()
        if temp[3] == "unavailable":
            results_list.append(f"{t} : yes")
        else:
            results_list.append(f"{t} : no")
       

    # Close the browser
    driver.quit()


    return "\n".join(results_list)



def save_to_file(result, filename):
    # Replace this with actual logic to save the result to a file
    file = open(filename, 'w')
    file.write(result)
    file.close()
    print(f"Saved in {filename}")

def main():
    # Définir le parser d'arguments

    print("Welcome to passive v1.0.0\nOPTIONS:\n    -fn         Search with full-name\n    -ip         Search with ip address\n    -u          Search with username\n")
    input("$> passive ")
    parser = argparse.ArgumentParser(
        description="Welcome to passive v1.0.0",
        epilog="OPTIONS:\n"
               "    -fn         Search with full-name\n"
               "    -ip         Search with ip address\n"
               "    -u          Search with username"
    )

    # Ajouter les options
    parser.add_argument("-fn", metavar="FULL_NAME", help="Search with full name")
    parser.add_argument("-ip", metavar="IP_ADDRESS", help="Search with IP address")
    parser.add_argument("-u", metavar="USERNAME", help="Search with username")

    # Analyser les arguments de la ligne de commande
    args = parser.parse_args()

    # Récupérer les valeurs des arguments
    full_name = args.fn
    ip_address = args.ip
    username = args.u

    # Afficher les valeurs récupérées
    if full_name is not None:
        result1 = search_full_name(full_name)
        if result1 is not None:
            print(result1)
            save_to_file(result1, 'result1.txt')
    elif ip_address is not None:
        result2 = search_ip_address(ip_address)
        if result2 is not None:
            print(result2)
            save_to_file(result2, 'result2.txt')
    elif username is not None:
        result3 = search_username(username)
        if result3 is not None:
            print(result3)
            save_to_file(result3, 'result3.txt')

if __name__ == "__main__":
    main()