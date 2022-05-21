import sys
from streamlit import cli as stcli

if __name__ == '__main__':
    sys.argv = ['streamlit', 'run', 'app.py', '--global.developmentMode', 'false', '--server.port', '8501']
    sys.exit(stcli.main())