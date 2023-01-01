cd init
./init.py
cd ../
sudo docker build ./ -t $1 && sudo docker push $1
