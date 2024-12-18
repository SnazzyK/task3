from pages.Scroll_Page import ScrollPage

COUNT = 23


def test_scroll(driver, config_reader):
    driver.get(config_reader.get_data_key("URL-10"))
    scroll = ScrollPage(driver)

    while True:
        count_elem = driver.get_elements("div", "jscroll-added")

        if len(count_elem) == COUNT:
            print(len(count_elem))
            break
        else:
            scroll.scroll_to_bottom()
