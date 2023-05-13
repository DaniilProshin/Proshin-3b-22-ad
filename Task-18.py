class GeometricFigure:
    def __init__(self, square, perimeter):
        self.square = square
        self.perimetr = perimeter

    def info(self):
        print(f"Square - {self.square}, Perimeter - {self.perimetr}")


figure1 = GeometricFigure(60, 25)
figure1.info()
