import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def scrap_senti_strength(driver, sentence):
    driver.get("http://sentistrength.wlv.ac.uk/")
    time.sleep(2)
    driver.execute_script(
        "document.getElementById(\"mainContent\").getElementsByTagName(\"form\")[6].getElementsByTagName(\"input\")[0].maxLength = 300;")
    main_content = driver.find_element_by_id("mainContent")
    forms = main_content.find_elements_by_name("2")
    spanish_form = forms[4]
    spanish_form_ps = spanish_form.find_elements_by_tag_name("p")
    input_area = spanish_form_ps[0].find_element_by_tag_name("input")
    input_area.clear()
    input_area.send_keys(sentence)
    input_area.send_keys(Keys.RETURN)
    time.sleep(3)

    content = driver.find_element_by_class_name("content")
    result = content.find_elements_by_tag_name("p")
    res = result[1].text.split()
    return int(res[-5]), int(res[-1])


def main():
    with open('sentence_input.txt', 'r', encoding='utf-8') as file:
        sentences = file.readlines()
    sentences = list(map(lambda x: x[:-1], sentences))
    driver = webdriver.Chrome()
    with open('sentence_output', 'w', encoding='utf-8') as file:
        for sentence in sentences:
            sentence_value = scrap_senti_strength(driver, sentence)
            file.write("(" + str(sentence_value[0]) + "," + str(sentence_value[1]) + ")" + "\n")


if __name__ == '__main__':
    main()
