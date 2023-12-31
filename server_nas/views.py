# from subprocess import CalledProcessError
import subprocess
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_unix_user(request):
    nim = request.POST.get('nim')
    print(nim)
    try:
        subprocess.check_call(
            'useradd -p $(openssl passwd -1 ' + str(nim) + ') -m -s /bin/bash -g hosting-users '
            + str(nim), #+ ' && quotatool -u ' + self.userId + ' -bq 450M -l 500M /home',
            shell=True)
    except subprocess.CalledProcessError:
        return JsonResponse({'status': 'error', 'message': 'Error adding Unix user'})
    else:
        return JsonResponse({'status': 'success', 'message': 'Unix user added'})


@csrf_exempt
def izin_user(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        container_id = payload.get('container_id')
        nim_user = payload.get('nim_user')
        kategori_kontainer = payload.get('kategori_kontainer')
        print(container_id)
        print(nim_user)
        print(kategori_kontainer)
        # Validate the data (add your validation logic here)
        if not container_id or not nim_user or not kategori_kontainer:
            return JsonResponse({'error': 'Invalid data'}, status=400)

        # Prepare the chown command
        command = f'chown {nim_user}:hosting-users -R /home/{nim_user}/{kategori_kontainer}'
        print(command)
        try:
            # Execute the chown command using subprocess
            subprocess.run(command, shell=True, check=True)
            return JsonResponse({'status': 'success', 'message': 'Command executed successfully'})
        except subprocess.CalledProcessError as e:
            return JsonResponse({'error': f'Error executing command: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def izin_data(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        container_id = payload.get('container_id')
        nim_user = payload.get('nim_user')
        kategori_kontainer = payload.get('kategori_kontainer')
        print(container_id)
        print(nim_user)
        print(kategori_kontainer)
        # Validate the data (add your validation logic here)
        if not container_id or not nim_user or not kategori_kontainer:
            return JsonResponse({'error': 'Invalid data'}, status=400)

        # Prepare the chown command
        command = f'chown www-data:www-data -R /home/{nim_user}/{kategori_kontainer}'
        print(command)
        try:
            # Execute the chown command using subprocess
            subprocess.run(command, shell=True, check=True)
            return JsonResponse({'status': 'success', 'message': 'Command executed successfully'})
        except subprocess.CalledProcessError as e:
            return JsonResponse({'error': f'Error executing command: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)