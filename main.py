from window import Window
from line import Line
from point import Point

def main():
    window = Window(800, 600)
    line1 = Line(Point(50, 50), Point(100, 100))
    line2 = Line(Point(200, 200), Point(500, 500))

    window.draw_line(line1, "black")
    window.draw_line(line2, "black")

    window.wait_for_close()

main()