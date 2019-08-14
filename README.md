# PyEvol

World with creatures controlled by Neural Network and evolving with Genetic Algorithm

## Setup development environnement

```
cd ~
mkdir dev; cd dev
mkdir venv repo

python3 -m pip install --user virtualenv
virtualenv venv/pyevol

source venv/pyevol/bin/activate

pip install kivy pymunk

git clone .../pymunk
cd pymunk
python setup.py build_ext --inplace
```
