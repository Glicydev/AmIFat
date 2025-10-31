from classes.BColors import BColors

class Displayer:

  def __init__(self):
    pass

  def error_message(message):
    print(BColors.FAIL + f"[ERROR] {message}" + BColors.ENDC)

  def warning_message(message):
    print(BColors.WARNING + f"[WARNING] {message}" + BColors.ENDC)

  def info_message(message):
    print(BColors.OKBLUE + f"[INFO] {message}" + BColors.ENDC)

  def success_message(message):
    print(BColors.OKGREEN + f"[SUCCESS] {message}" + BColors.ENDC)