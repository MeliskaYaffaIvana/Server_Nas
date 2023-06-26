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

@csrf_exempt
def add_unix_user(request):
    userPass = request.POST.get('userPass')
    userId = request.POST.get('userId')

    try:
        subprocess.check_call(
            ['useradd', '-p', userPass, '-m', '-s', '/bin/bash', '-g', 'hosting-users', userId],
            shell=True)
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



