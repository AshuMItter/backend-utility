# try:
#     raise ValueError("Some Error")
#     # some code that may raise an exception
# except Exception as ex:
#     # handle any other exception
#     print(f"Exception Raised {ex} - caught at Exception excpet block ")   
# except (ValueError) as e:
#     print(f"Value error Raised {e}- Caught at ValueError Except Block")
#     # handle the ValueError


try:
    raise TypeError("Type Error")
    # some code that may raise an exception
# This will catch all the errors
except ValueError:
    print('A ValueError occurred')   # This will never be executed
except TypeError:
    print('A TypeError occurred')  
except Exception as e:
    print(f'An error occurred: {e} at Exception except')   # This will never be executed

