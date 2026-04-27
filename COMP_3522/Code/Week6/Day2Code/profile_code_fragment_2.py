import pstats, cProfile, io

def profile(fnc):
    """
    An implementation of a function decorator that wraps a function in
    a code that profiles it.
    """
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()

        # wrapped function starts
        retval = fnc(*args, **kwargs) #fnc is whatever function has the @profile tag
        # wrapped function ends

        pr.disable()
        sortby = pstats.SortKey.CALLS
        ps = pstats.Stats(pr).strip_dirs().sort_stats(sortby)
        ps.print_stats()
        return retval

    return inner

#profile function is called first, passing in heavy_function as its parameter
@profile
def heavy_function(low, high):
    for x in range(low, high):
        for y in range(low, high):
            for z in range(low, high):
                z += x + y

def main():
    heavy_function(0,300) #when heavy_function is executed it's first wrapped in the profile function, then executed

    #p = profile(heavy_function) #equivalent if removing @profile decorator above heavy_function
    #p(0,300)

if __name__ == '__main__':
    main()



