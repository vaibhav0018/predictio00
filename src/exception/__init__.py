import sys
import traceback

class CustomException(Exception):
    def __init__(self, error_message: Exception, error_details: sys):
        self.error_message = self.get_detailed_error_message(error_message, error_details)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_details: sys) -> str:
        _, _, exc_tb = error_details.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        try_block_line_number = exc_tb.tb_lineno
        exception_block_line_number = exc_tb.tb_frame.f_lineno

        detailed_message = (
            f"Error occurred in execution of:\n"
            f"[{file_name}] at try block line number: [{try_block_line_number}]\n"
            f"and exception block line number: [{exception_block_line_number}]\n"
            f"Error message: [{error_message}]"
        )

        return detailed_message

    def __str__(self):
        return self.error_message

    def __repr__(self):
        return f'{self.__class__.__name__}({self.error_message})'
