from subprocess import CalledProcessError, check_call
import os
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def add_unix_user(request):
#     userPass = request.POST.get('userPass')
#     userId = request.POST.get('userId')

#     try:
#         output = subprocess.check_output(
#             'useradd -p $(openssl passwd -1 ' + userPass + ') -m -s /bin/bash -g hosting-users '
#             + userId,
#             shell=True,
#             stderr=subprocess.STDOUT,
#         )
#         print(output)  # Print the command output for debugging purposes
#     except subprocess.CalledProcessError as e:
#         error_output = e.output.decode('utf-8')
#         print(error_output)  # Print the error output for debugging purposes
#         return JsonResponse({'status': 'error', 'message': 'Error adding Unix user: ' + error_output})

#     return JsonResponse({'status': 'success', 'message': 'Unix user added'})

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
    password = request.POST.get('nim')
    nim = request.POST.get('nim')
    print(password)
    print(nim)
    try:
        command = '/usr/sbin/useradd -p ' + str(password) + ' -m -s /bin/bash -g hosting-users ' + str(nim)
        run_command_with_sudo(command)
    except CalledProcessError:
        return JsonResponse({'status': 'error', 'message': 'Error adding Unix user'})

    return JsonResponse({'status': 'success', 'message': 'Unix user added'})

# @csrf_exempt
# def add_unix_user(request):
#     userPass = request.POST.get('userPass')
#     userId = request.POST.get('userId')

#     try:
#         command = '/usr/sbin/useradd -p ' + str(userPass) + ' -m -s /bin/bash -g hosting-users ' + str(userId)
#         run_command_with_sudo(command)
#         return JsonResponse({'status': 'success', 'message': 'Unix user added'})
#     except CalledProcessError as e:
#         return JsonResponse({'status': 'error', 'message': f'Error adding Unix user: {str(e)}'})


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

# import json
# from django.http import JsonResponse
# # from .models import Container 
# from django.views.decorators.csrf import csrf_exempt
# import subprocess
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @csrf_exempt
# def update_containers(request):
#     if request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8')).get('data')
#         print(data)  # Periksa nilai data
#         # Proses data yang diterima dari Django A
#         # Misalnya, perbarui nilai status_job pada objek Container
#         updated_values = []
#         for container_data in data:
#             container_id = container_data.get('id')
#             status_job = container_data.get('status_job')

#             # # Lakukan operasi yang sesuai pada objek Container
#             # container = Container.objects.get(id=container_id)
#             # container.status_job = status_job
#             # container.save()

#             # Buat entri yang mengandung nilai terbaru
#             updated_values.append({
#                 'id': container_id,
#                 'status_job': 1
#             })
        

#         # Kembalikan nilai yang diperbarui ke Django A
#         response_data = {
#             'updated_values': updated_values
#         }

#         return JsonResponse(response_data)
#     else:
#         return JsonResponse({'message': 'Invalid request method.'}, status=400)


# @api_view(['POST'])
# def create_folders(request):
#     users = request.data.get("users")

#     for user in users:
#         nim = user.get("nim")

#         # Eksekusi perintah shell untuk membuat folder dengan nama NIM
#         command = f"mkdir {nim}"
#         subprocess.run(command, shell=True)

#     return Response({"message": "Folders created successfully."})

# # @csrf_exempt
# # def update_containers(request):
# #     if request.method == 'POST':
# #         data = json.loads(request.body.decode('utf-8')).get('data')
# #         print(data)  # Periksa nilai data
# #         # Proses data yang diterima dari Django A
# #         # Misalnya, perbarui nilai status_job pada objek Container
# #         updated_values = []
# #         for container_data in data:
# #             container_id = container_data.get('id')
# #             status_job = container_data.get('status_job')

# #             # # # Lakukan operasi yang sesuai pada objek Container
# #             # container = Container.objects.get(id=container_id)
# #             # container.status_job = status_job
# #             # container.save()

# #             # Buat entri yang mengandung nilai terbaru
# #             updated_values.append({
# #                 'id': container_id,
# #                 'status_job': 1
# #             })
# #         # Send the updated values to Django 1 for saving
# #         url = "http://127.0.0.1:8000/api/save-containers/"  # Replace with the URL endpoint of Django 1
# #         headers = {
# #             "Content-Type": "application/json"
# #         }
# #         payload = {
# #             "data": updated_values
# #         }
# #         json_payload = json.dumps(payload)

# #         response = requests.post(url, data=json_payload, headers=headers)
# #         if response.status_code == 200:
# #             return JsonResponse({'message': 'Data processed and sent to Django 1.'})
# #         else:
# #             return JsonResponse({'message': 'Failed to send data to Django 1.'}, status=500)
# #     else:
# #         return JsonResponse({'message': 'Invalid request method.'}, status=400)



