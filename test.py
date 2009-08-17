import sys, os, re, unittest

# Run all tests in t/

def regressionTest():
    path = os.path.abspath(os.path.dirname(sys.argv[0])) + '/t'
    files = os.listdir(path)
    test = re.compile("^t_.+\.py$", re.IGNORECASE)
    files = filter(test.search, files)
    filenameToModuleName = lambda f: 't.'+os.path.splitext(f)[0]
    moduleNames = map(filenameToModuleName, files)
    modules = map(__import__, moduleNames)
    modules = map(lambda name: sys.modules[name], moduleNames)
    load = unittest.defaultTestLoader.loadTestsFromModule
    return unittest.TestSuite(map(load, modules))

suite = regressionTest()

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite)
