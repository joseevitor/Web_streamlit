import sys
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "runner.py"]
sys.exit(stcli.main())

