class Rectangle:
    # Method to set dimensions of the rectangle
    def setDim(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    # Method to calculate and return the area of the rectangle
    def getArea(self):
        return self.length * self.breadth

# Main program to create rectangle objects and compare their areas
def main():
    # Create two rectangle objects
    rect1 = Rectangle()
    rect2 = Rectangle()

    # Input dimensions for the first rectangle
    length1 = float(input("Enter the length of the first rectangle: "))
    breadth1 = float(input("Enter the breadth of the first rectangle: "))
    rect1.setDim(length1, breadth1)
    
    # Input dimensions for the second rectangle
    length2 = float(input("Enter the length of the second rectangle: "))
    breadth2 = float(input("Enter the breadth of the second rectangle: "))
    rect2.setDim(length2, breadth2)
    
    # Get the areas of both rectangles
    area1 = rect1.getArea()
    area2 = rect2.getArea()

    # Print the areas of the rectangles
    print(f"Area of the first rectangle: {area1}")
    print(f"Area of the second rectangle: {area2}")

    # Compare the areas
    if area1 > area2:
        print("The first rectangle has a larger area.")
    elif area2 > area1:
        print("The second rectangle has a larger area.")
    else:
        print("Both rectangles have the same area.")

# Run the program
if __name__ == "__main__":
    main()
