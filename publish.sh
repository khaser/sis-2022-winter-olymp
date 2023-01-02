cd init
python3 init.py
cd ../
sudo docker build ./ -t $1 && sudo docker push $1
