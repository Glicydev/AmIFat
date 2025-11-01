class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[38;2;255;165;0m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    COLOR_GRADIENT = [
      '\033[91m',  # rouge
      '\033[33m',  # orange
      '\033[93m',  # jaune
      '\033[33m',  # orange clair ou jaune foncé
      '\033[92m'   # vert
    ]

    
    @staticmethod
    def getColorFromVal(val, min, max):
      nb_colors = len(BColors.COLOR_GRADIENT)
      in_val = val - min
      val_range = max - min
      
      for i in range(nb_colors - 1, -1, -1):
        if in_val <= val_range / i:
          return BColors.COLOR_GRADIENT[i]
      