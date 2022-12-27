from pathlib import Path
import time
import paramiko
import cv2
import shutil

def upload_png(sftp, png_path):
  png_name = Path(png_path).name
  remote_path = f'/home/userdata/{png_name}'
#   local_path = f'/Users/_{get_datetime()}.squlite3'

#   sftp.get(remote_path, local_path) 
  sftp.put(png_path, remote_path)
  print(f"uploaded {png_name} to {remote_path}")
  
  return remote_path

def download_mp4(sftp, png_path):
    remote_path = f'/home/userdata/{Path(png_path).stem}.mp4'
    local_path = f'./generated_mp4/{Path(png_path).stem}.mp4'
    sftp.get(remote_path, local_path)
    shutil.copyfile(local_path, "./generated.mp4")
    print(f"downloaded {remote_path} to {local_path}")


def get_ssh_and_sftp():
    host = {write your host} 
    port = {write your port}
    username = # example
    password = # example

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password, port=port)

    sftp = ssh.open_sftp()
    
    return ssh, sftp


def exec_deepfake(ssh, remote_path):
    ssh.exec_command(f'python3 /home/userdata/deepfake.py --source_image={remote_path}')
    
    return 


if __name__ == "__main__":
    img_dir = Path('./')
    
    ssh, sftp = get_ssh_and_sftp()
    
    png_list = list(img_dir.glob('*.jpg'))
    
    old_png_list = png_list
    num_old = len(old_png_list)
    
    # while True:
    for i in range(1000):
        new_png_list = list(img_dir.glob('*.jpg'))
        num_new = len(new_png_list)
        if num_new > num_old:
            # ssh, sftp = get_ssh_and_sftp()

            added_png = list(set(new_png_list) - set(old_png_list))[0]
            remote_path = upload_png(sftp, added_png)
            exec_deepfake(ssh, remote_path)
            print("SSH command is executed")
            time.sleep(100)
            download_mp4(sftp, added_png)
            
            old_png_list = new_png_list
            num_old = num_new
            # sftp.close()
            # ssh.close()


        time.sleep(5)
            
    sftp.close()
    ssh.close()

