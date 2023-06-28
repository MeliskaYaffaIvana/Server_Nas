from subprocess import CalledProcessError
import os
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def run_command_with_sudo(command):
    sudo_command = 'sudo ' + command
    sudo_password_bytes = b'1234'
    sudo_password = sudo_password_bytes.decode()

    try:
        process = subprocess.Popen(sudo_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
        # sudo_password_bytes = (sudo_password + '\n').encode()
        output, error = process.communicate(input=sudo_password + '\n')
        
        
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, command, output=output, stderr=error)
        
        return output.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

@csrf_exempt
def add_unix_user(request):
    nim = request.POST.get('nim')
    id = request.POST.get('id')
    print(id)
    print(nim)
    try:
        command = '/usr/sbin/useradd -p ' + str(nim) + ' -m -s /bin/bash -g hosting-users ' + str(id)
        run_command_with_sudo(command)
    except CalledProcessError:
        return JsonResponse({'status': 'error', 'message': 'Error adding Unix user'})

    return JsonResponse({'status': 'success', 'message': 'Unix user added'})



def add_folder(request):
    folder = request.GET.get('folder')
    if folder:
        if os.path.exists(folder):
            response = {'error': 'Folder already exists.'}
        else:
            try:
                subprocess.run(f'mkdir {folder}', shell=True, check=True)
                response = {'message': 'Folder created successfully.'}
            except subprocess.CalledProcessError:
                response = {'error': 'Failed to create folder.'}
    else:
        response = {'error': 'Folder parameter is missing.'}
    return JsonResponse(response)
