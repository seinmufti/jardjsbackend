### Program to survey a list of frames (windows, doors) to calculate total cost and items required

from .jard import Jard


def main():
    slide_windows = [
        {"strbluprnt": "slide window", "w": 149.5, "h": 175.7},
        {"strbluprnt": "slide window", "w": 147.6, "h": 236.8},
        {"strbluprnt": "slide window", "w": 190.7, "h": 192.8},
        {"strbluprnt": "slide window", "w": 152.5, "h": 187.7},
        {"strbluprnt": "slide window", "w": 152.5, "h": 187.7},
        {"strbluprnt": "slide window", "w": 151.5, "h": 214},
        {"strbluprnt": "slide window", "w": 151.5, "h": 214},
        {"strbluprnt": "slide window", "w": 167.3, "h": 187.8},
        {"strbluprnt": "slide window", "w": 156.5, "h": 177},
        {"strbluprnt": "slide window", "w": 140.3, "h": 174.7},
        {"strbluprnt": "slide window", "w": 140.3, "h": 174.7},
    ]

    jard = Jard()
    jard.slide_window(slide_windows)


if __name__ == "__main__":
    main()
