#e2e checkout using selenium webdriver python

Install :
install Python 
install pip = py -m pip install --upgrade pip
test file is under Tests Folder, so run virtual environment first
    create  virtual env named technical_test = py -m venv technical_test (if on your folder there is no technical_test folder) 
	activate virtual env = .\technical_test\Scripts\Activate 
	if cannot activate virtual env = Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
install selenium = pip install selenium
install pytest = pip install pytest
install webdriver-manager = pip install webdriver-manager
install pytest-html = pip install pytest-html

How to run : 
Run langsung dari ROOT di folder D:\WORK\Training\Technical Test - PT Altech Omega Andalan tanpa perlu masuk ke dalam folder \Tests
-> Run with markerName :
pytest -m checkout .\technical_test\Tests
pytest -m login .\technical_test\Tests
untuk report tambahkan --html=report_name.html di akhir
-> Run without markerName:
pytest test_login.py --html=hasil_test_login.html
pytest test_checkout.py --html=hasil_test_checkout.html


#DOCKER
-> create Doclerfile
-> BUILD
docker build -t myname:version .
-> Check Image
docker images
docker image ls 
-> RUN 
docker run -it imagename bash
-> PUSH to DOCKER hub
1. Tag Your Docker Image
docker tag [local-image-name]:[tag] [username]/[repository-name]:[tag]
2. Push the Image to Docker Hub
Push the Image to Docker Hub


