#   
## Steps
- Make sure `netifaces` and `python-decouple` are installed, if not run following command
    ```
    pip install netifaces python-decouple
    ```
- Clone repo
    ```
    git clone <URL of REPO>
    cd <directory name>  # raspberrypi-send-ip
    ```
- Rename username `pi` and path to `sendmail.py` file in ifup_script
- Copy environment file
    ```
    cp .env.example .env
    ```
- Change environmant variable in `.env` file
- Run install script
    ```
    chmod +x install.sh
    sudo ./install.sh
    ```