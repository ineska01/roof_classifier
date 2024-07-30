hi, after clonning 

python -m venv venv

.\venv\Scripts\Activate 
Deactivate - to deactivate venv

pip install -r requirements.txt

for streamlit 

streamlit run main.py

to install tox locally use
python -m pip install tox

to format code
tox -e format

to do a static test - lint
tox -e linter

to commit
git commit -m ""