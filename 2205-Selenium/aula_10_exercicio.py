from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located
)

url = 'https://selenium.dunossauro.live/aula_10_a.html'

browser = Firefox()

browser.get(url)

wdw = WebDriverWait(browser, 30)

# WebDriverWait
## until
## until_not



# expected_conditions
## InvalidSelectorException
## NoAlertPresentException
## NoSuchElementException
## NoSuchFrameException
## StaleElementReferenceException
## WebDriverException
## WebElement
## alert_is_present
## all_of
## any_of
## element_attribute_to_include
## element_located_selection_state_to_be
## element_located_to_be_selected
## element_selection_state_to_be
## element_to_be_clickable
## element_to_be_selected
## frame_to_be_available_and_switch_to_it
## invisibility_of_element
## invisibility_of_element_located
## new_window_is_opened
## none_of
## number_of_windows_to_be
## presence_of_all_elements_located
## presence_of_element_located
## re
## staleness_of
## text_to_be_present_in_element
## text_to_be_present_in_element_attribute
## text_to_be_present_in_element_value
## title_contains
## title_is
## url_changes
## url_contains
## url_matches
## url_to_be
## visibility_of
## visibility_of_all_elements_located
## visibility_of_any_elements_located
## visibility_of_element_located

# WEBDRIVER
## CONTEXT_CHROME
## CONTEXT_CONTENT
## add_cookie
## application_cache
## back
## bidi_connection
## binary
## capabilities
## caps
## close
## command_executor
## context
## create_web_element
## current_url
## current_window_handle
## delete_all_cookies
## delete_cookie
## desired_capabilities
## error_handler
## execute
## execute_async_script
## execute_script
## file_detector
## file_detector_context
## find_element
## find_element_by_class_name
## find_element_by_css_selector
## find_element_by_id
## find_element_by_link_text
## find_element_by_name
## find_element_by_partial_link_text
## find_element_by_tag_name
## find_element_by_xpath
## find_elements
## find_elements_by_class_name
## find_elements_by_css_selector
## find_elements_by_id
## find_elements_by_link_text
## find_elements_by_name
## find_elements_by_partial_link_text
## find_elements_by_tag_name
## find_elements_by_xpath
## firefox_profile
## forward
## fullscreen_window
## get
## get_cookie
## get_cookies
## get_full_page_screenshot_as_base64
## get_full_page_screenshot_as_file
## get_full_page_screenshot_as_png
## get_log
## get_pinned_scripts
## get_screenshot_as_base64
## get_screenshot_as_file
## get_screenshot_as_png
## get_window_position
## get_window_rect
## get_window_size
## implicitly_wait
## install_addon
## log_types
## maximize_window
## minimize_window
## mobile
## name
## orientation
## page_source
## pin_script
## pinned_scripts
## print_page
## profile
## quit
## refresh
## save_full_page_screenshot
## save_screenshot
## service
## session_id
## set_context
## set_page_load_timeout
## set_script_timeout
## set_window_position
## set_window_rect
## set_window_size
## start_client
## start_session
## stop_client
## switch_to
## timeouts
## title
## uninstall_addon
## unpin
## window_handles


