import pstats, cProfile, io
from pstats import SortKey

def heavy_function():
    for x in range(0,1000):
        for y in range(0,100):
            for z in range(0,100):
                z += x + y

def main():
    pr = cProfile.Profile()
    pr.enable()

    # … code to be profiled comes here …
    heavy_function()
    # … end code to be profiled …

    pr.disable()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr).strip_dirs().sort_stats(sortby)
    ps.print_stats()


if __name__ == '__main__':
    main()



