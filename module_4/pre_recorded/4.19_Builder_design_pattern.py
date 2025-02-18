class Computer:
    def __init__(self, builder):
        self.cpu = builder.cpu
        self.ram = builder.ram
        self.gpu = builder.gpu
        self.hdd = builder.hdd

    def __str__(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}, GPU: {self.gpu}, HDD: {self.hdd}"


class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.gpu = None
        self.hdd = None
    
    def set_cpu(self, cpu):
        self.cpu = cpu
        return self
    def set_ram(self, ram):
        self.ram = ram
        return self
    def set_gpu(self, gpu):
        self.gpu = gpu
        return self
    def set_hdd(self, hdd):
        self.hdd = hdd
        return self

    def build(self):
        return Computer(self)
    
builder = ComputerBuilder()
computer = builder.set_cpu("i7").set_gpu("Nvidia").set_hdd("1TB").build()
print(computer)