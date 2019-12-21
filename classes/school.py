class School:
    def __init__(self, SIIR_code, SIRUES_code, name = '?', locality = '?', region = '?'):
        
        self.SIIR_code       = SIIR_code
        self.SIRUES_code     = SIRUES_code
        self.name            = name.lower()
        self.locality        = locality.lower()
        self.region          = region

    def __str__(self):
        return str(self.SIIR_code + ' ' + self.SIRUES_code + ' ' + self.name + ' ' + self.locality
                     + ' ' + self.region)

# remove zero padding from SIIR_code
def remove_left_zeros(code):
    i = 0
    while code[i] == '0':
        i += 1
    return code[i:]
