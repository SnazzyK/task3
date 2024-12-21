from pages.dynamic_content_page import DynamicContentPage


def test_img(driver, config_reader):
    driver.get(config_reader.get_data_key("URL-9"))
    dc = DynamicContentPage(driver)
    dc.wait_for_open()
    while True:

        image_sources = driver.get_elements("div", "large-2 columns")

        if len(set(image_sources)) < len(image_sources):
            break
        else:
            driver.refresh()
