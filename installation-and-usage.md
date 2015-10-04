# installation

checkout:
```
cd ~/workspace
git clone https://github.com/worldveil/dejavu.git
cd dejavu
```

install python 3:
```
brew install python3
```

create virtualenv for python3:
```
virtualenv -p python3 .
```

activate virtualenv:
```
source bin/activate
```

```
brew install portaudio
pip3 install pyaudio
```

```
brew install ffmpeg
pip3 install pydub
```

```
pip3 install numpy
pip3 install scipy
pip3 install matplotlib
```

install x11 which is needed by mathplotlib from http://xquartz.macosforge.org/landing/

```
brew install mysql
pip3 install mysqlclient
```

```
pip3 install git+git://github.com/WarrenWeckesser/wavio.git
```

```
mysql.server start
mysql -u root
```

in mysql:
```
CREATE DATABASE IF NOT EXISTS dejavu;
```

# usage

this should now run without errors:
```
python3 example.py
```

inspect the database that was filled with songs and fingerprints by `example.py`:
```
mysql -u root dejavu
```
in mysql:
```
show tables;
show columns from songs;
show columns from fingerprints;
select * from songs;
select count(*) from fingerprints;
select count(*) from fingerprints where song_id = 1;
```

to clear the database:
```
delete from songs;
delete from fingerprints;
```

```
python3 run_tests.py --secs 5 --temp ./temp_audio --log-file ./results/dejavu-test.log --padding 8 --seed 42 --results ./results ./mp3
```
