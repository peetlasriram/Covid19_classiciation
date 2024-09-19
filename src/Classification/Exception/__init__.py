import logging
import sys
def error_detail_message(error,error_details:sys):
    _,_,exc_tab=error_details.exc_info()
    fie_path=exc_tab.tb_frame.f_code.co_filename
    error_message="error occure inthe python:[{0}] and line number:{1} and message[{2}]".format(fie_path,exc_tab.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__ (self,message,error_detail:sys):
        super().__init__(message)
        self.message=error_detail_message(message,error_details=error_detail)
    def __str__(self):
        return self.message
        