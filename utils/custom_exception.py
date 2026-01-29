import sys

class CustomException(Exception):
    """A custom exception class that captures additional context information.
    It inherits from the built-in Exception class and adds attributes for
    the filename and line number where the exception was raised.
    """

    def __init__(self, message: str, error_detail: Exception=None):
        self.error_message = self.get_detailed_error_message(message, error_detail) #get the detailed error message
        super().__init__(self.error_message) #call the parent class constructor and treat our custom exception as a standard exception

    @staticmethod # indicates that this method does not depend on the instance itself
    def get_detailed_error_message(message: str, error_detail: Exception) -> str:
        """Generate a detailed error message including filename and line number.

        Args:
            message (str): The custom error message.
            error_detail (Exception): The original exception object.
        """
        _, _, exc_tb = sys.exc_info() #get the exception info
        filename = exc_tb.tb_frame.f_code.co_filename #get the filename where the exception occurred
        line_number = exc_tb.tb_lineno #get the line number where the exception occurred
        detailed_message = f"Error occurred in file: {filename} | Line number: {line_number} | Error message: {message}"
        
        return detailed_message
    
    def __str__(self) -> str: #print the error message when the exception is converted to a string
        return self.error_message #return the error message