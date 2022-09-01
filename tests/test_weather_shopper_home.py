"""
This is an example automated test WeatherShopper Home page
Our automated test will do the following:
    #Open Weathershopper.
    #Get the Temperature.
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
#import conf.example_form_conf as conf
import conf.testrail_caseid_conf as testrail_file
import pytest


@pytest.mark.GUI
def test_weather_shopper_home(test_obj):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #1. Create a test object and fill the example form.
        test_obj = PageFactory.get_page_object("weather shopper page")
        #Set start_time with current time
        start_time = int(time.time())


        # Turn on the highlighting feature
        #test_obj.turn_on_highlight()

        #1. Get the temperature text
        temp_text = test_obj.get_temperature_text()
        print(temp_text)
        test_obj.log_result(temp_text,
                            positive="Able to get text\n",
                            negative="Not able to get text \n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        # #Update TestRail
        # case_id = testrail_file.test_example_form_name
        # test_obj.report_to_testrail(case_id,test_obj.test_run_id,result_flag)
        # test_obj.add_tesults_case("Set Name", "Sets the name in the form", "test_example_form", result_flag, "Failed to set name: %s \nOn url: %s\n"%(name,test_obj.get_current_url()), [test_obj.log_obj.log_file_dir + os.sep + test_obj.log_obj.log_file_name])
       

        #13. Print out the result
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter

    except Exception as e:
        print("Exception when trying to run test: %s"%__file__)
        print("Python says:%s"%str(e))

    assert expected_pass == actual_pass, "Test failed: %s"%__file__


#---START OF SCRIPT
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()

    #Run the test only if the options provided are valid
    if options_obj.check_options(options):
        test_obj = PageFactory.get_page_object("Zero",base_url=options.url)

        #Setup and register a driver
        test_obj.register_driver(options.remote_flag,options.os_name,options.os_version,options.browser,options.browser_version,options.remote_project_name,options.remote_build_name)

        #Setup TestRail reporting
        if options.testrail_flag.lower()=='y':
            if options.test_run_id is None:
                test_obj.write('\033[91m'+"\n\nTestRail Integration Exception: It looks like you are trying to use TestRail Integration without providing test run id. \nPlease provide a valid test run id along with test run command using -R flag and try again. for eg: pytest -X Y -R 100\n"+'\033[0m')
                options.testrail_flag = 'N'
            if options.test_run_id is not None:
                test_obj.register_testrail()
                test_obj.set_test_run_id(options.test_run_id)

        if options.tesults_flag.lower()=='y':
            test_obj.register_tesults()

        test_weather_shopper_home(test_obj)

        #teardowm
        test_obj.wait(3)
        test_obj.teardown()
    else:
        print('ERROR: Received incorrect comand line input arguments')
        #print(option_obj.print_usage())
