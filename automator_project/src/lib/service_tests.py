from hal_rest import *
run_tests("prebuild util tests", "http://staging.halicea.com",[
  ("Get Configurations:", lambda:execute_request(None, "/svc/branded_apps/config")),
  ("Get Publishers:", lambda:execute_request(None, "/svc/branded_apps/publishers")),
  ("Get Supported Platforms:", lambda:execute_request(None, "/svc/branded_apps/platforms")),
  ("Get Resource Types:", lambda:execute_request(None, "/svc/branded_apps/resource_types")),
  ("Get Supported Authentication Types:", lambda:execute_request(None, "/svc/branded_apps/authentication_types")),
  ("Get Supported Application Types:", lambda:execute_request(None, "/svc/branded_apps/application_types")),

])
