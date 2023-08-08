import os

import pytest

if __name__ == '__main__':
    # pytest.main(['-sv', './scripts', '-n=2', 'reruns=2'])
    pytest.main()
    os.system("allure generate temp -o reports --clean")
    # './scripts/test_login.py::TestLogin::test_login', './scripts/test_login.py::test_outclass',

    #注意目录位置，all.py和pytest.ini都要放在项目的根目录下