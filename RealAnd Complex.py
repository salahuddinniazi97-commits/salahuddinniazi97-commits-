class Numbers():
    def __init__(self,real,imaginary):
        self.real = real
        self.imag = imaginary

    
    def Show_numbers(self):
        print(self.real , "i +" ,self.imag ,"j")


nums1 = Numbers(2,3)
nums1.Show_numbers()