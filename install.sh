#necessário python3.8 ou superior
yum install -y centos-release-scl
yum install -y rh-python38
python3 -m pip install --upgrade pip setuptools wheel
pip3 install openai-whisper


sudo yum install -y https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm
sudo yum install -y https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-7.noarch.rpm
sudo yum install -y ffmpeg ffmpeg-devel
ffmpeg -version

